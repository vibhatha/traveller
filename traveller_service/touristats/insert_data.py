import pandas as pd
from touristats.models import AllCountryStats

def insert_arrival_data(year, file_path):
    data = pd.read_csv(file_path)

    # Iterate over the DataFrame and create Arrival objects
    for index, row in data.iterrows():
        for month in ['January', 'February', 'March', 'April', 'May', 'June', 
                      'July', 'August', 'September', 'October', 'November', 'December']:
            # Convert the arrival value to numeric, handling commas and potential invalid values
            arrival_value = pd.to_numeric(str(row[month]).replace(',', ''), errors='coerce')
            # Replace NaN with 0 if conversion failed
            arrival_value = 0 if pd.isna(arrival_value) else arrival_value
            
            AllCountryStats.objects.create(
                country=row['Country'],
                year=year,
                month=month,
                passengers=arrival_value
            )

# Example usage
year = 2019
file_path = '../data/arrival/all_countries/all_country_arrivals_' + str(year) + '.csv'
insert_arrival_data(year, file_path)

# AllCountryStats.objects.all().delete()
