from statistics import mean
import requests
from Data import States as states
from Data import ProjectionsData as projections

response = requests.get("https://corona.lmao.ninja/v2/states")
if response.status_code == 200:
    stateDict = response.json()
    for el in stateDict:  # state
        if el['state'] not in states.forbidden_states:
            el['state'] = states.states_abbrev[el['state']]
else:
    print("Error, server responded with status code of " + str(response.status_code))
    exit(-1)

cur = sorted(stateDict, key=lambda j: j['state'])


def calculate(data):
    # index 0 = 30 days ago
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

weekly = []
monthly = []
i = 0

master = []
for el in list(states.states_abbrev.values()):
    cases = response[el]["cases"]
    deaths = response[el]["deaths"]

    ratesDeath = calculate(deaths)
    ratesCase = calculate(cases)
    outWeekCase = future(ratesCase[0], cases, 'cases')
    outMonthCase = future(ratesCase[1], cases, 'cases')
    outWeekDeath = future(ratesDeath[0], deaths, 'deaths')
    outMonthDeath = future(ratesDeath[1], deaths, 'deaths')

    parDict = {'state': el,
               'casesTomorrow': outWeekCase[0],
               'casesIn14': outWeekCase[1],
               'casesIn30': outWeekCase[2],
               'deathsTomorrow': outWeekDeath[0],
               'deathsIn14': outWeekDeath[1],
               'deathsIn30': outWeekDeath[2]}
    weekly.append(parDict)

    parDict = {'state': el,
               'casesTomorrow': outMonthCase[0],
               'casesIn14': outMonthCase[1],
               'casesIn30': outMonthCase[2],
               'deathsTomorrow': outMonthDeath[0],
               'deathsIn14': outMonthDeath[1],
               'deathsIn30': outMonthDeath[2]}
    monthly.append(parDict)

# print(weekly)
# print(monthly)
