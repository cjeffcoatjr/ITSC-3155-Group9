import requests
from Data import States as states

response = requests.get("https://corona.lmao.ninja/v2/states")
if response.status_code == 200:
    stateDict = response.text
    for state in states.states_full:
        abbrev = states.states_abbrev[state]
        stateDict = stateDict.replace(state, abbrev)
    stateDict = stateDict.replace("West VA", "WV")  # Fix some funsies

    # print(stateDict)

else:
    print("Error, server responded with status code of " + str(response.status_code))
    exit(-1)
