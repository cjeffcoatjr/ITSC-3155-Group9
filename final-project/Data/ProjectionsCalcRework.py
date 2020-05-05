# index 0 = 30 days ago
from statistics import mean
import requests
from Data import States as states
from Data import ProjectionsData as projections
from Data import Choropleth as current
import pandas as pd  # Load data frame and tidy it.

response = requests.get("https://corona.lmao.ninja/v2/states")
if response.status_code == 200:
    stateDict = response.json()
    for state in stateDict:
        if state['state'] not in states.forbidden_states:
            state['state'] = states.states[state['state']]


else:
    print("error, server responded with status code of" + str(response.status_code))
    exit(-1)
cur = sorted(stateDict, key = lambda j: j['state'])




def calculate(data):
    k = 1
    dailyGrowth = []
    past = data[0]
    present = data[k]
    i = 1
    while(i < len(data) - 1):
        if past == 0:
            past = 1
        rate = ((present - past)/past) + 1
        dailyGrowth.append(rate)

        past = present
        k = k + 1
        present = data[k]
        i = i + 1

    lastWeek = dailyGrowth[22:29]

    lastWeekGrowthRate = mean(lastWeek)

    lastMonthGrowthRate = mean(dailyGrowth)

    stats = [lastWeekGrowthRate, lastMonthGrowthRate]

    return stats


def future(rate, data, state, type):
    today = data[29]
    futures = []
    tommorow = 0
    i = 1
    total = []
    k =0
    total.append(cur[k][type])
    while i < 31:


        futures.append(today * rate ** i)
        i = i + 1
        k= k + 1


    out = [futures[0], futures[14], futures[29]]
    return out



deaths = []
cases = []

abrev = list(states.states.values())

response = projections.response
# for state in states.stateList:
#     abbrev = states.states[state]
#     response = response.replace(state, abbrev)
# response = response.replace("West VA", "WV")  # Fix some funsies

masterList = {}
#response = projections.response
i = 0
for el in abrev:
    cases = response[el]["cases"]
    deaths = response[el]["deaths"]
    ratesCase = calculate(cases)
    outWeekCase = future(ratesCase[0], cases, el, 'cases')
    outMonthCase = future(ratesCase[1], cases, el, 'cases')
    ratesDeath = calculate(deaths)
    outWeekDeath = future(ratesDeath[0], deaths, el, 'deaths')
    outMonthDeath = future(ratesDeath[1], deaths, el, 'deaths')
    #access by masterlist[state Abrev][type of future calc avg and deaths vs cases] 0 - 3][future points 0 = 1 day ahead, 1 = 14 days ahead, 2 = 30 days ahead]
    futureData = [outWeekCase, outMonthCase, outWeekDeath, outMonthDeath]
    masterList[el] = futureData

for el in abrev:
    print("State of " + el)
    print("Cases in 14 days")
    print(masterList[el][0][1])
    print("Cases in 30 days")
    print(masterList[el][0][2])
    print("Deaths in 14 days")
    print(masterList[el][2][1])
    print("deaths in 30 days")
    print(masterList[el][2][2])


