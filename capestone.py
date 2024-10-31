import pandas as pd

# Percorsi dei file caricati (con barre normali)
file_paths = {
    "taxi_licenses": "C:/Users/fbadaloni/Downloads/4. CAPSTONE/taxi_licenses_europe_cities_extended.xlsx",
    "urban_incidents": "C:/Users/fbadaloni/Downloads/4. CAPSTONE/urban_incidents_fatalities_europe_cities_extended.xlsx",
    "urban_pollution": "C:/Users/fbadaloni/Downloads/4. CAPSTONE/urban_pollution_data_europe_cities.xlsx",
    "bike_lane_sharing": "C:/Users/fbadaloni/Downloads/4. CAPSTONE/bike_lane_sharing_europe_cities_extended.xlsx",
    "bus_tram_lines": "C:/Users/fbadaloni/Downloads/4. CAPSTONE/bus_tram_lines_europe_cities_extended.xlsx",
    "demography": "C:/Users/fbadaloni/Downloads/4. CAPSTONE/demography_europe_cities_extended.xlsx",
    "metro_network": "C:/Users/fbadaloni/Downloads/4. CAPSTONE/metro_network_europe_cities_extended.xlsx",
    "ride_sharing": "C:/Users/fbadaloni/Downloads/4. CAPSTONE/ride_sharing_availability_europe_cities_extended.xlsx"
}

# Caricamento dei file in un dizionario di DataFrames
dataframes = {name: pd.read_excel(path) for name, path in file_paths.items()}

# Creazione di una lista unica delle città da tutti i dataset
all_cities = pd.concat([df[['City']] for df in dataframes.values()]
                       ).drop_duplicates().reset_index(drop=True)
all_cities.columns = ['city']  # Rinomina la colonna a 'city' per uniformità

# Percorso del file Excel consolidato
consolidated_file_path = "C:/Users/fbadaloni/Downloads/4. CAPSTONE/Consolidated_Europe_Cities_Data_with_dim_city.xlsx"

# Scrittura del file Excel consolidato
with pd.ExcelWriter(consolidated_file_path) as writer:
    for name, df in dataframes.items():
        df.to_excel(writer, sheet_name=name, index=False)
    all_cities.to_excel(writer, sheet_name="dim_city", index=False)

print("File Excel consolidato creato con successo:", consolidated_file_path)
