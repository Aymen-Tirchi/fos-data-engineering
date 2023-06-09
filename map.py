import csv
import folium


def main():
    data = []

    with open('transformed_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    map = folium.Map()

    for row in data:
        city = row['city']
        latitude = float(row['latitude'])
        longitude = float(row['longitude'])
        temperature = float(row['temperature'])

        marker = folium.Marker(location=[latitude, longitude], popup=f"City: {city}<br>Temperature: {temperature}")
        marker.add_to(map)

    map.save('temperature_map.html')


main()
