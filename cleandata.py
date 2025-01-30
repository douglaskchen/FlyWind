import json
import numpy as np

def clean_value(value):
    if isinstance(value, str) and value.lower() == "nan":
        return 0  # Replace "NaN" string with a default value, e.g., 0

    if isinstance(value, (int, float, np.float32, np.float64)):
        if np.isnan(value):
            return 0  # Replace NaN with a default value, e.g., 0
        return round(value, 2)  # Round to 2 decimal places if it's a float

    return value

def clean_data(data):
    if isinstance(data, list):
        return [clean_data(item) for item in data]
    if isinstance(data, dict):
        return {k: clean_data(v) if isinstance(v, (dict, list)) else clean_value(v) for k, v in data.items()}
    return clean_value(data)

# Input and output file paths
input_file = '/home/douglas/repos/FlyWind/wind.json'  # Update the path if needed
output_file = '/home/douglas/repos/FlyWind/cleaned_wind.json'

# Load the original JSON data
with open(input_file, 'r') as f:
    data = json.load(f)

# Clean the data (replace NaNs and round values)
cleaned_data = clean_data(data)

# Wrap the cleaned data in the "FlyWind" structure
wrapped_data = {
    "FlyWind": {
        "cleaned_wind.json": cleaned_data
    }
}

# Save the wrapped and cleaned data to the output file
with open(output_file, 'w') as f:
    json.dump(wrapped_data, f, indent=4)  # Save with indentation for readability

print(f"Cleaned and wrapped data has been saved to {output_file}")