def calculate_risk(weather):
    temp = weather["temperature"]
    humidity = weather["humidity"]
    wind = weather["wind_speed"]

    if temp >= 35 or humidity >= 80 or wind >= 10:
        return "HIGH RISK"

    if temp >= 30 or humidity >= 60 or wind >= 5:
        return "MEDIUM RISK"

    return "LOW RISK"
