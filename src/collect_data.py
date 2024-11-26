import requests
import pandas as pd
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def collect_weather_data():
    # Replace with your API key from OpenWeatherMap
    API_KEY = os.getenv('OPENWEATHER_API_KEY')
    if not API_KEY:
        raise ValueError("Please set OPENWEATHER_API_KEY in .env file")
        
    CITY = "London"  # Example city
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    data_list = []
    current_date = datetime.now()
    
    # Collect data for the last 5 days
    for i in range(5):
        params = {
            'q': CITY,
            'appid': API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            
            weather_data = {
                'date': current_date.strftime('%Y-%m-%d'),
                'time': current_date.strftime('%H:%M:%S'),
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'weather_condition': data['weather'][0]['main']
            }
            
            data_list.append(weather_data)
        else:
            print(f"Error fetching data: {response.status_code}")
            print(response.text)
        
        current_date -= timedelta(days=1)
    
    df = pd.DataFrame(data_list)
    os.makedirs('data/raw', exist_ok=True)
    df.to_csv('data/raw/raw_data.csv', index=False)
    print("Data collected and saved to data/raw/raw_data.csv")

if __name__ == "__main__":
    collect_weather_data()