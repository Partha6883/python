# import requests
# city = input("Enter City:")
# url = f"https://wttr.in/{city}?format=j1"
# response = requests.get(url)
# data = response.json()
# temp = data["current_condition"][0]["temp_C"]
# print("_____________Current_Weather______________")
# print("Temparature:",temp,"C")
# feels_like= data["current_condition"][0]["FeelsLikeC"]
# print("Feels like:",feels_like,"C")
# humidity = data["current_condition"][0]["humidity"]
# print("Humidity:",humidity,"%")

"*********************************************************"

import requests
city = input("Enter City:")
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()
current = data["current_condition"][0]
print("---------Current_Weather----------")
print("tempature:",current["temp_C"],"C")
print("Humidity:",current["humidity"])
print("Visibility:",current["visibility"])
print("Feels_like:",current["FeelsLikeC"],"C")
print("Weather:",current["weatherDesc"][0]["value"])

print("-----------Hourly_Forecast-------------")
hourly = data["weather"][0]["hourly"]
for hour in hourly:
    print(
        f"Time: {hour['time']}  |  "
        f"Dew_PointC: {hour['DewPointC']}C  |  "
        f"chance_of_rain: {hour['chanceofrain']}  |  "
        f"Wind_ChillC: {hour['WindChillC']}C"
    )

"************************************************************"
 