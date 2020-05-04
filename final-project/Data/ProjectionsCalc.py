# index 0 = 30 days ago
from statistics import mean

k = 1
data = []
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
