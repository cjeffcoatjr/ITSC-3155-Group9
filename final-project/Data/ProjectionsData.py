import requests
import numpy as np
from Data import States as states

response = {}
for state in states.stateList:
    tmp_state = state.replace(" ", "%20").lower()
    tmp_response = requests.get(("https://disease.sh/v2/historical/usacounties/" + tmp_state + "?lastdays=30"))
    if tmp_response.status_code == 200:
        tmp_response = tmp_response.json()
        cases = np.zeros(30)
        deaths = np.zeros(30)
        for county in tmp_response:  # Merge per-county data into per-state data
            tmp_cases = county['timeline']['cases']
            cases_nparray = np.array(list(county['timeline']['cases'].values()))
            cases = cases + cases_nparray
            tmp_deaths = county['timeline']['deaths']
            deaths_nparray = np.array(list(county['timeline']['deaths'].values()))
            deaths = deaths + deaths_nparray
        cases = cases.tolist()
        deaths = deaths.tolist()
        tmp_dict = {'cases': cases, 'deaths': deaths}
        abbrev = states.states[state]
        response[abbrev] = tmp_dict

#print(response)
