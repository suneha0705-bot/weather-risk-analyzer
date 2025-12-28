import pandas as pd
from weather_fetcher import fetch_weather
from risk_engine import calculate_risk

def main():

    cities = ["Chandigarh", "Delhi", "Mumbai", "Bangalore"]

    records = []

    for city in cities:
        
        weather = fetch_weather(city)
        risk = calculate_risk(weather)
        records.append(
            {
            "City": weather["city"],
            "Temperature (°C)": weather["temperature"],
            "Humidity (%)": weather["humidity"],
            "Wind Speed (m/s)": weather["wind_speed"],
            "Condition": weather["description"],
            "Risk Level": risk
            }
        )

    df = pd.DataFrame(records)
    print("\nWeather Risk Analysis\n")
    print(df)

if __name__ == "__main__":
    main()

