# Weather ETL (Extract, Transform, Load)

This project is an ETL (Extract, Transform, Load) pipeline that retrieves current weather data for a list of cities in Algeria and saves the data to various output files. The ETL process is automated using a cron job that updates the weather data every 10 minutes.

## Features

- Retrieves current weather data using the Open-Meteo API.
- Uses geocoding to obtain latitude and longitude coordinates for cities using the Nominatim API.
- Supports custom list of cities stored in a JSON file.
- Saves the weather data to multiple output files (root folder):
  - raw_data_.json: Contains the raw weather data for all cities.
  - transformed_data.csv: Contains the transformed weather data in CSV format.
  - temperature_map.html: Displays an interactive map with temperature data.

## Prerequisites

- Docker installed on your system.

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/Aymen-Tirchi/fos-data-engineering
```

2. Build the Docker image:

```bash
docker build -t cron-job .
```

3. Run the Docker container:

```bash
docker run cron-job
```
