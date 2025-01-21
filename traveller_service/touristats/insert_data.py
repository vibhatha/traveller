import pandas as pd
from touristats.models import TimeFrame, AllCountryStats

def insert_arrival_data(year, file_path):
    data = pd.read_csv(file_path)

    # Iterate over the DataFrame and create Arrival objects
    for index, row in data.iterrows():
        for month_num, month in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 
                      'July', 'August', 'September', 'October', 'November', 'December'], 1):
            # Convert the arrival value to numeric, handling commas and potential invalid values
            arrival_value = pd.to_numeric(str(row[month]).replace(',', ''), errors='coerce')
            # Replace NaN with 0 if conversion failed
            arrival_value = 0 if pd.isna(arrival_value) else arrival_value
            
            # Get or create TimeFrame for this year and month
            timeframe, _ = TimeFrame.objects.get_or_create(
                year=year,
                month=month_num
            )
            
            # Create AllCountryStats with the new structure
            AllCountryStats.objects.create(
                timeframe=timeframe,
                country=row['Country'],
                passengers=arrival_value,
                days_of_stay=0,  # Set default value or get from data if available
                purpose_of_visit='Not Specified'  # Set default value or get from data if available
            )

# Example usage
year = 2019
file_path = '../data/arrival/all_countries/all_country_arrivals_' + str(year) + '.csv'
insert_arrival_data(year, file_path)
