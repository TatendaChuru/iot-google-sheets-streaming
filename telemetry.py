import time
import random
from datetime import datetime
import gspread

# Authenticate with Google Sheets using your local credentials file
gc = gspread.service_account(filename="credentials.json")

# Open the Google Sheet by its exact title
sheet = gc.open("IoT Telemetry Data").sheet1

print("Successfully connected to Google Sheets! Pushing telemetry data every 5 minutes...")

# Loop to stream data rows every 5 minutes (300 seconds)
try:
    while True:
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(40.0, 70.0), 2)
        status = "Active"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        row = [temperature, humidity, status, timestamp]
        sheet.append_row(row)
        print(f"[{timestamp}] Appended row: {row}")

        # Wait 5 minutes (300 seconds) before pushing the next data point
        time.sleep(300)

except KeyboardInterrupt:
    print("\nData streaming stopped.")