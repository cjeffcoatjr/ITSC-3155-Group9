import requests

response = requests.get("https://corona.lmao.ninja/v2/states")
if response.status_code == 200:
    stateDict = response.json()
else:
    print("error, server responded with status code of" + str(response.status_code))
