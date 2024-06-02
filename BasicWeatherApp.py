import requests, json

# API Key
api_key = "920bae5097c287703c2e2331401e3ed8"

# base_url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Allow user to enter city name
city_name = input("Enter city name : ")

# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get requests module
# return complete_url
response = requests.get(complete_url)

# json converted to python data
x = response.json()

# Now x contains list of nested dictionaries, if city weather details are given or city not found
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_condition = z[0]["description"]

    # print following values
    print(" Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n Humidity (in percentage) = " +
          str(current_humidity) +
          "\n Weather condition = " +
          str(weather_condition))

else:
    print(" City Not Found ")