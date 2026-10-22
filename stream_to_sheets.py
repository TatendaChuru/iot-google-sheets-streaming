import time
import random
from datetime import datetime
import gspread

# 1. Authenticate with Google Sheets using your service account JSON file
gc = gspread.service_account(filename="credentials.json")

# 2. Open your Google Sheet by name
# Make sure your Google Sheet is titled exactly "IoT Telemetry Data"
# and shared with your service account email address!
sheet = gc.open("IoT Telemetry Data").sheet1

print("Successfully connected to Google Sheets! Pushing telemetry data...")

# 3. Stream data loop
try:
    while True:
        # Generate simulated IoT telemetry data
        temperature = round(random.uniform(20.0, 30.0), 2)
        humidity = round(random.uniform(40.0, 70.0), 2)
        status = "Active"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create row payload
        row = [temperature, humidity, status, timestamp]

        # Append row to the Google Sheet
        sheet.append_row(row)
        print(f"[{timestamp}] Appended row: {row}")

        # Wait 5 seconds before pushing the next data point
        time.sleep(5)

except KeyboardInterrupt:
    print("\nData streaming stopped by user.")