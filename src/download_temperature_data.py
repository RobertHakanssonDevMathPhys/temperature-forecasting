import requests
import json


url = "https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/1/station/99450/period/latest-months/data.json"

print("Hämtar temperaturdata från SMHI...")

response = requests.get(url)

print("Statuskod:", response.status_code)

if response.status_code != 200:
    print("Kunde inte hämta data.")
    exit()

try:
    data = response.json()
    print("JSON tolkades korrekt!")

    # Spara som fil
    with open("temperature_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Data sparad som temperature_data.json")

except Exception as e:
    print("JSON kunde inte tolkas:", e)
    print("Råtext:")
    print(response.text[:500])