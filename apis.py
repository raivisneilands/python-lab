import requests

base_url = "https://aviationweather.gov/api/data/"

r = requests.get(base_url + "metar?ids=EVRA&format=json")

report_time = r.json()[0]['reportTime']
temp = r.json()[0]['temp']
wdir = r.json()[0]['wdir']
wspeed = r.json()[0]['wspd']
name = r.json()[0]['name']
cover = r.json()[0]['cover']

if cover == "OVC":
    cover = "Overcast"

print(f"Weather in: {name}. At time: {report_time}")
print(f"Current temperature: {temp} degrees celsius")
print(f"Current wind direction: {wdir}degrees")
print(f"Current wind speed: {wspeed}m/s")
print(f"Current cover: {cover}")