
import json

# 1. Load previously saved API response
with open("heatmap_result.json", "r", encoding="utf-8") as file:
    result = json.load(file)

# 2. Extract heatmap data
data = result["data"]["result"]
features = data["map_data"]["features"]
stats = data["stats_data"]["temperature_stats"]

# 3. Check total features
print("Total tiles:", len(features))

# 4. Check required properties
required_properties = [
    "tile_id",
    "average_temperature",
    "min_temperature",
    "max_temperature"
]

all_properties_valid = all(
    all(key in feature.get("properties", {}) for key in required_properties)
    for feature in features
)

print("All required properties present:", all_properties_valid)

# 5. Check missing temperature values
temperatures = [
    feature["properties"].get("average_temperature")
    for feature in features
]

missing_temperatures = sum(
    value is None for value in temperatures
)

print("Missing temperatures:", missing_temperatures)

# 6. Validate temperature ranges
invalid_tiles = []

for feature in features:
    properties = feature["properties"]

    minimum = properties["min_temperature"]
    average = properties["average_temperature"]
    maximum = properties["max_temperature"]

    if not (minimum <= average <= maximum):
        invalid_tiles.append(properties["tile_id"])

print("Invalid temperature ranges:", invalid_tiles)

# 7. Compare calculated mean with API mean
calculated_mean = sum(temperatures) / len(temperatures)

print("Calculated mean:", calculated_mean)
print("API mean:", stats["mean"])

mean_matches = abs(calculated_mean - stats["mean"]) < 0.000001

print("Mean validation passed:", mean_matches)

# 8. Overall result
validation_passed = (
    len(features) > 0
    and all_properties_valid
    and missing_temperatures == 0
    and len(invalid_tiles) == 0
    and mean_matches
)

print("\nOverall validation:", validation_passed)

