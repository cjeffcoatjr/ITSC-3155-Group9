# index 0 = 30 days ago
from statistics import mean
from Data import States as states
from Data import Projections as projections


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


def future(rate, data):
    today = data[29]
    futures = []
    tommorow = 0
    i = 0
    while i < 30:
        tommorow = round(today * rate)
        futures.append(tommorow)
        today = tommorow
        i = i + 1

    out = [futures[0], futures[14], futures[29]]
    return out



deaths = []
cases = []

#deaths rate index 0 is last week growth rate avg, index 1 is last months avg same for cases
#deathsRate = calculate(deaths)
#casesRate = calculate(cases)

#will output anticipated deaths for tommorow, 2 weeks, and one month
#deathDataPoints = future(deathsRate[0], deaths)

abrev = list(states.states.values())

response = projections.response
# for state in states.stateList:
#     abbrev = states.states[state]
#     response = response.replace(state, abbrev)
# response = response.replace("West VA", "WV")  # Fix some funsies

print(abrev)
masterList = {}
#response = projections.response
i = 0
for el in abrev:
    cases = response[el]["cases"]
    deaths = response[el]["deaths"]
    ratesCase = calculate(cases)
    outWeekCase = future(ratesCase[0], cases)
    outMonthCase = future(ratesCase[1], cases)
    ratesDeath = calculate(deaths)
    outWeekDeath = future(ratesDeath[0], deaths)
    outMonthDeath = future(ratesDeath[1], deaths)
    #access by masterlist[state Abrev][type of future calc avg and deaths vs cases] 0 - 3][future points 0 = 1 day ahead, 1 = 14 days ahead, 2 = 30 days ahead]
    futureData = [outWeekCase, outMonthCase, outWeekDeath, outMonthDeath]
    masterList[el] = futureData

print(masterList["NY"][0][2])

