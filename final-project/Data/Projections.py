import requests
from Data import States as states

response = {}
for state in states.stateList:
    state = state.replace(" ", "%20").lower()
    tmp_response = requests.get(("https://disease.sh/v2/historical/usacounties/" + state + "?lastdays=30"))
    if tmp_response.status_code == 200:
        tmp_response = tmp_response.json()
        cases = {}
        deaths = {}
        for county in tmp_response: # Merge per-county data into per-state data
            tmp_cases = county['timeline']['cases']
            updated_cases = cases
            cases = {**tmp_cases, **updated_cases}
            tmp_deaths = county['timeline']['deaths']
            updated_deaths = deaths
            deaths = {**tmp_deaths, **updated_deaths}
        tmp_dict = {'cases': cases, 'deaths': deaths}
        response[state] = tmp_dict







