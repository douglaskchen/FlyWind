import json
import numpy as np

def clean_value(value):
    # Check for string "NaN"
    if isinstance(value, str) and value.lower() == "nan":
        return 0  # Replace "NaN" string with a default value, e.g., 0

    # Check for numeric NaN values
    if isinstance(value, (int, float, np.float32, np.float64)):
        if np.isnan(value):
            return 0  # Replace NaN with a default value, e.g., 0
        return round(value, 2)  # Round to 2 decimal places if it's a float

    # Preserve other data types as they are
    return value

def clean_data(data):
    if isinstance(data, list):
        return [clean_data(item) for item in data]
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    return clean_value(data)

input_file = '/home/douglas/repos/FlyWind/wind.json'  # Update the path if needed
output_file = '/home/douglas/repos/FlyWind/cleaned_wind.json'

with open(input_file, 'r') as f:
    data = json.load(f)

cleaned_data = clean_data(data)

with open(output_file, 'w') as f:
    json.dump(cleaned_data, f, separators=(',', ':'))  # Save without indents or line breaks

print(f"Cleaned and minified data has been saved to {output_file}")


