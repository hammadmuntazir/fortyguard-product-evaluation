import os
import time
import json
import requests
from dotenv import load_dotenv

# 1. Load API key
load_dotenv()
API_KEY = os.getenv("FORTYGUARD_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")

# 2. API configuration
BASE_URL = "https://api.fortyguard.com/v1"
SUBMIT_URL = f"{BASE_URL}/heatmap"

headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json"
}

# 3. Define a small San Francisco study area
payload = {
    "polygon_aoi": {
        "type": "Polygon",
        "coordinates": [[
            [-122.4300, 37.7700],
            [-122.4200, 37.7700],
            [-122.4200, 37.7800],
            [-122.4300, 37.7800],
            [-122.4300, 37.7700]
        ]]
    },
    "date_time": {
        "start_date": "2026-11-10",
        "filter_type": 3
    },
    "granularity": 100,
    "analytic_type": "tcm"
}

# 4. Submit heatmap request
print("Submitting heatmap request...")

try:
    response = requests.post(
        SUBMIT_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    print("HTTP Status:", response.status_code)
    response.raise_for_status()

    response_data = response.json()

except requests.exceptions.RequestException as error:
    raise RuntimeError(f"API request failed: {error}")

except ValueError:
    raise RuntimeError("API returned an invalid JSON response.")

# 5. Extract activity ID
data = response_data.get("data", {})
activity_id = data.get("activity_id")

if not activity_id:
    print(json.dumps(response_data, indent=4))
    raise RuntimeError("Activity ID not found in API response.")

print("Task submitted successfully.")
print("Activity ID:", activity_id)

# 6. Check task status
status_url = f"{BASE_URL}/status/{activity_id}"

print("\nChecking task status...")

for attempt in range(24):
    try:
        status_response = requests.get(
            status_url,
            headers={"api-key": API_KEY},
            timeout=30
        )

        # A 404 immediately after submission may be temporary.
        if status_response.status_code == 404 and attempt < 3:
            print("Activity not available yet. Retrying...")
            time.sleep(5)
            continue

        status_response.raise_for_status()
        status_data = status_response.json().get("data", {})
        status = status_data.get("status", "").lower()

    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Status request failed: {error}")

    print(f"Attempt {attempt + 1}: {status or 'Unknown status'}")

    if status in ("completed", "succeeded"):
        print("\nHeatmap generated successfully!")

        with open("heatmap_result.json", "w", encoding="utf-8") as file:
            json.dump(status_response.json(), file, indent=4)

        print("Result saved to heatmap_result.json")
        break

    elif status in ("failed", "error"):
        raise RuntimeError(
            f"Heatmap generation failed. Activity ID: {activity_id}"
        )

    elif status in ("processing", "pending", "queued"):
        time.sleep(5)

    else:
        raise RuntimeError(f"Unexpected task status: {status}")

else:
    raise TimeoutError(
        f"Task did not complete within the polling window. "
        f"Activity ID: {activity_id}"
    )

