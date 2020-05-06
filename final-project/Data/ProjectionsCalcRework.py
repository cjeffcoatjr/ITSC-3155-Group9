# index 0 = 30 days ago
from statistics import mean
import requests
from Data import States as states
from Data import ProjectionsData as projections
import pandas as pd  # Load data frame and tidy it.

response = requests.get("https://corona.lmao.ninja/v2/states")
if response.status_code == 200:
    stateDict = response.json()
    for state in stateDict:  # state
        if state['state'] not in states.forbidden_states:
            state['state'] = states.states[state['state']]
else:
    print("Error, server responded with status code of " + str(response.status_code))
    exit(-1)

cur = sorted(stateDict, key=lambda j: j['state'])


def calculate(data):
    k = 1
    daily_growth = []
    past = data[0]
    present = data[k]
    i = 1
    while i < len(data) - 1:
        if past == 0:
            past = 1
        rate = ((present - past) / past) + 1
        daily_growth.append(rate)

        past = present
        k += 1
        present = data[k]
        i += 1

    last_week = daily_growth[22:29]
    last_week_growth_rate = mean(last_week)
    last_month_growth_rate = mean(daily_growth)
    stats = [last_week_growth_rate, last_month_growth_rate]

    return stats


def future(rate, data, type):
    today = data[29]
    futures = []
    i = 1
    total = []
    k = 0
    total.append(cur[k][type])
    while i < 31:
        futures.append(round(today * rate ** i))
        i = i + 1
        k = k + 1

    out = [futures[0], futures[14], futures[29]]
    return out


deaths = []
cases = []

response = projections.response

weekly = {}
monthly = {}
total = {}
i = 0

master = []
for el in list(states.states.values()):
    cases = response[el]["cases"]
    deaths = response[el]["deaths"]

    ratesDeath = calculate(deaths)
    ratesCase = calculate(cases)
    outMonthCase = future(ratesCase[1], cases, 'cases')
    outWeekCase = future(ratesCase[0], cases, 'cases')
    outWeekDeath = future(ratesDeath[0], deaths, 'deaths')
    outMonthDeath = future(ratesDeath[1], deaths, 'deaths')
    parDict = {}
    parDict['state'] = el
    parDict['weeklyCases1Day'] = outWeekCase[0]
    parDict['weeklyCases14Day'] = outWeekCase[1]
    parDict['weeklyCases30Day'] = outWeekCase[2]
    parDict['monthlyCases1Day'] = outMonthCase[0]
    parDict['monthlyCases14Day'] = outMonthCase[1]
    parDict['monthlyCases30Day'] = outMonthCase[2]

    parDict['weeklyDeaths1Day'] = outWeekDeath[0]
    parDict['weeklyDeaths14Day'] = outWeekDeath[1]
    parDict['weeklyDeaths30Day'] = outWeekDeath[2]

    parDict['monthlyDeaths1Day'] = outMonthDeath[0]
    parDict['monthlyDeaths14Day'] = outMonthDeath[1]
    parDict['monthlyDeaths30Day'] = outMonthDeath[2]
    master.append(parDict)
    # weekly['state'] = el
    # weekly['cases'] = outWeekCase
    # weekly['deaths'] = outWeekDeath
    #
    # monthly['state'] = el
    # monthly['cases'] = outWeekCase
    # monthly['deaths'] = outWeekDeath
    #
    # total['weekly'] = weekly
    # total['monthly'] = monthly

print(total)

# for el in abrev:
#     print("State of " + el)
#     print("Cases in 14 days")
#     print(masterList[el][0][1])
#     print("Cases in 30 days")
#     print(masterList[el][0][2])
#     print("Deaths in 14 days")
#     print(masterList[el][1][1])
#     print("deaths in 30 days")
#     print(masterList[el][1][2])
