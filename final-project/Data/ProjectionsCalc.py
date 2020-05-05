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
    print(lastWeekGrowthRate)

    lastMonthGrowthRate = mean(dailyGrowth)

    stats = [lastWeekGrowthRate, lastMonthGrowthRate]

    return stats


def future(rate, data, state, type):
    today = data[29]
    futures = []
    tommorow = 0
    i = 0
    total = []
    total.append(cur[i][type])
    while i < 30:

        print(today)
        tommorow = round(today * rate)
        futures.append(tommorow)
        print(tommorow)
        total.append(total[i] + tommorow)
        today = tommorow
        i = i + 1


    out = [futures[0], futures[14], futures[29], total[0], total[14], total[29]]
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
print("first")
print(masterList["NY"][0][0])
print("second")
print(masterList["NY"][0][3])

print(masterList["NY"][0][2])
print(masterList["NY"][0][5])
print(masterList["NY"][0][4])
print(masterList["NY"][2][2])

