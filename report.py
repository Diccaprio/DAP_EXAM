import csv
from datetime import datetime, timedelta

# Define the file name
filename = "covid_impact_analysis.csv"

# Create sample data
start_date = datetime(2025, 5, 1)
data = []

for i in range(100):
    date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
    data.append([
        date, "Jorhat", 10000 + i * 150, 150, 500 + i * 5, 5, 
        9500 + i * 100, 200 - i, 50000 + i * 500, f"{3 + i*0.05}%", 
        8000 + i * 200, f"{80 + i*0.5}%", f"GDP -{5 - i*0.05}%", 
        f"{30 - i*0.2}%", f"{50 + i*0.5}%", 
        "No restrictions" if i > 20 else "Masks recommended"
    ])

# Define CSV headers
headers = [
    "Date", "Location", "Total Cases", "New Cases", "Total Deaths", "New Deaths",
    "Recovered Cases", "Hospitalizations", "Testing Conducted", "Positivity Rate",
    "Vaccinations Administered", "Population Vaccinated", "Economic Impact",
    "Mobility Reduction", "ICU Availability", "Government Policies"
]

# Write data to CSV file
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print(f"CSV file '{filename}' has been successfully created!")
import pandas as pd

# Read the CSV file
df = pd.read_csv("covid_impact_analysis.csv")

# Display the table
print(df)