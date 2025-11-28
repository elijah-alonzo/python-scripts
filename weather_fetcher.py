import requests
import sys

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}, Temp: {data['main']['temp']}°C")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python weather_fetcher.py <city>")
    else:
        get_weather(sys.argv[1])
