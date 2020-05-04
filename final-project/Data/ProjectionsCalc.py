# index 0 = 30 days ago
from statistics import mean


def calculate(data):
    k = 1
    dailyGrowth = []
    past = data[0]
    present = data[k]
    i = 1
    while(i < len(data) - 1):
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
        tommorow = today * rate
        futures.append(tommorow)
        today = tommorow
        i = i + 1

    out = futures[1, 14, 29]
    return out



deaths = []
cases = []

#deaths rate index 0 is last week growth rate avg, index 1 is last months avg same for cases
deathsRate = calculate(deaths)
casesRate = calculate(cases)

#will output anticipated deaths for tommorow, 2 weeks, and one month
deathDataPoints = future(deathsRate[0], deaths)



