import requests

api_key = "dae5f6326757b1f052a57f542b1aa3b5"
city = "Sacramento"
url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()


description = json.get("weather")[0].get("description")
print("Today's forecast is", description)
temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min)
temp_max = json.get("main").get("temp_max")
print("The maximum temperature is", temp_max)