import requests
import pyttsx3

api_key = "cd27c6adead5b670929945767b5b8360"
base_url = "http://api.openweathermap.org/data/2.5/weather"

country = input("Enter a Country name : ")
engine = pyttsx3.init()
params = {
    "q": country,
    "appid": api_key,
    "units": "metric"  # Use "imperial" for Fahrenheit
}

response = requests.get(base_url, params=params)
data = response.json()

if data["cod"] == "404":
    print("City not found!")
else:
    print(f"Weather in {data['name']}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Description: {data['weather'][0]['description']}")

   
    engine.say(f"Weather in {data['name']}:")
    engine.say(f"Temperature: {data['main']['temp']} degrees Celsius")
    engine.say(f"Humidity: {data['main']['humidity']} percent")
    engine.say(f"Description: {data['weather'][0]['description']}")
    
    engine.runAndWait()
