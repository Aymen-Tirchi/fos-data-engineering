import glob
import json
import csv


def get_all_filenames():
    filenames = glob.glob("raw_data_*.json")
    return filenames


def transform_one_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        
    transformed_data = []
    for city, item in data.items():
        latitude = item[1]['latitude']
        longitude = round(float(item[1]['longitude']), 2)
        temperature = item[1]['current_weather']['temperature']
        time = item[1]['current_weather']['time']
        
        transformed_data.append({
            'city': city,
            'latitude': latitude,
            'longitude': longitude,
            'temperature': temperature,
            'time': time
        })
        
    return transformed_data


def merge_all_files(files):
    merged_data = []

    for file in files:
        transformed_data = transform_one_file(file)
        merged_data.extend(transformed_data)

    return merged_data


def drop_duplicates(data):
    unique_data = [dict(t) for t in {tuple(d.items()) for d in data}]
    print(unique_data)

    return unique_data


def main():
    files = get_all_filenames()
    merged_data = merge_all_files(files)
    unique_data = drop_duplicates(merged_data)

    with open("transformed_data.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=unique_data[0].keys())
        writer.writeheader()
        writer.writerows(unique_data)


main()
