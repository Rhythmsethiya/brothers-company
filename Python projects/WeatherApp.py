import requests
import pyttsx3
import json

url = 'https://api.weatherapi.com/v1/current.json?key=3612989a0bb543b1952175818233009&q=kolkata'

# Make the API request
r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:
    # Parse the JSON response
    data = json.loads(r.text)

    # Extract the city name from the response
    city_name = data['location']['name']

    # Initialize text to speech
    engine = pyttsx3.init()

    # Speak the city name
    engine.say(f"The current city is {city_name}")

    # Wait for the speech to finish
    engine.runAndWait()

else:
    print("Failed to retrieve data from the API")
