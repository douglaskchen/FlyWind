import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_json(data1, data2, path=""):
    if isinstance(data1, dict) and isinstance(data2, dict):
        for key in data1:
            if key not in data2:
                print(f"Key '{path + key}' not in second JSON")
            else:
                compare_json(data1[key], data2[key], path + key + ".")
        for key in data2:
            if key not in data1:
                print(f"Key '{path + key}' not in first JSON")
    elif isinstance(data1, list) and isinstance(data2, list):
        for i, (item1, item2) in enumerate(zip(data1, data2)):
            compare_json(item1, item2, path + f"[{i}].")
    else:
        if data1 != data2:
            print(f"Difference at '{path}': {data1} != {data2}")

cleaned_wind_path = './cleaned_wind.json'
wind_global_path = './demowind.json'

cleaned_wind_data = load_json(cleaned_wind_path)
wind_global_data = load_json(wind_global_path)

compare_json(cleaned_wind_data, wind_global_data)
