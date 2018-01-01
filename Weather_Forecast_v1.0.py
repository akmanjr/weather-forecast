import urllib2
import json

apiKey = "622e1a17efabb99f"
myState = "CH"
myCity = "Bottmingen"

def getWeatherConditions(myState, myCity):

	myCity = myCity.replace(" ", "_")
	urlConditions = "http://api.wunderground.com/api/" + apiKey + "/conditions/q/" + myState + "/" + myCity + ".json"
	jsonObjectCondition = urllib2.urlopen(urlConditions)
	dataCondition = json.load(jsonObjectCondition)


	print("Location: "), dataCondition["current_observation"]["display_location"]["city"], ",", dataCondition["current_observation"]["display_location"]["state_name"]
	print("Current Weather: "), dataCondition["current_observation"]["temp_c"], "Celcius Degree | ", dataCondition["current_observation"]["weather"]
	print("Local Time: "), dataCondition["current_observation"]["local_time_rfc822"]
	print("Observation Time: "), dataCondition["current_observation"]["observation_time_rfc822"]

def getWeatherForecast(myState, myCity):

	myCity = myCity.replace(" ", "_")
	urlForecast = "http://api.wunderground.com/api/" + apiKey + "/forecast/q/" + myState + "/" + myCity + ".json"
	jsonObjectForecast = urllib2.urlopen(urlForecast)
	dataForecast = json.load(jsonObjectForecast)

	print ""
	print "Forecast:"
	for day in range (4):
		print dataForecast["forecast"]["simpleforecast"]["forecastday"][day]["date"]["weekday"] + ": " + dataForecast["forecast"]["simpleforecast"]["forecastday"][day]["high"]["celsius"] + " Celcius Degree | " + dataForecast["forecast"]["simpleforecast"]["forecastday"][day]["conditions"]

getWeatherConditions(myState, myCity)
getWeatherForecast(myState, myCity)
