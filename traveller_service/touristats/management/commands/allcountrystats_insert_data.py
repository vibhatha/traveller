from django.core.management.base import BaseCommand
from touristats.models import TimeFrame, AllCountryStats
import pandas as pd
from tqdm import tqdm
import sys

class Command(BaseCommand):
    """Insert tourist arrival statistics from CSV file into the database.

    This command processes a CSV file containing monthly tourist arrival data and
    inserts it into the AllCountryStats model. The CSV should have a 'Country' column
    and twelve month columns (January through December).

    The command handles:
        - Data cleaning (removing commas, handling invalid values)
        - TimeFrame creation/linking
        - Automatic country_id generation
        - Data type conversion

    Examples:
        Insert data for year 2023:
            >>> python manage.py allcountrystats_insert_data 2023 /path/to/data.csv

    CSV Format Expected:
        Country,January,February,March,April,May,June,July,August,September,October,November,December
        India,5000,6000,4500,...
        China,3000,3500,4000,...

    Args:
        year (int): The year for which the data is being inserted
        file_path (str): Path to the CSV file containing the arrival data

    Returns:
        None. Prints success message with number of records inserted.

    Raises:
        FileNotFoundError: If the specified CSV file doesn't exist
        ValueError: If the CSV format is invalid or required columns are missing
    """

    help = 'Insert AllCountryStats data from CSV'

    def add_arguments(self, parser):
        parser.add_argument('year', type=int)
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        year = options['year']
        file_path = options['file_path']
        
        data = pd.read_csv(file_path)
        total_rows = len(data)
        
        self.stdout.write(f"Starting import for {total_rows} countries...")
        
        # Create progress bar for countries
        for index, row in tqdm(data.iterrows(), total=total_rows, desc="Importing data"):
            country_name = row['Country']
            sys.stdout.write(f"\rProcessing {country_name} ({index + 1}/{total_rows})")
            sys.stdout.flush()
            
            for month_num, month in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 
                          'July', 'August', 'September', 'October', 'November', 'December'], 1):
                arrival_value = pd.to_numeric(str(row[month]).replace(',', ''), errors='coerce')
                arrival_value = 0 if pd.isna(arrival_value) else arrival_value
                
                timeframe, _ = TimeFrame.objects.get_or_create(
                    year=year,
                    month=month_num
                )
                
                AllCountryStats.objects.create(
                    timeframe=timeframe,
                    country=country_name,
                    passengers=arrival_value,
                    days_of_stay=0,
                    purpose_of_visit='Not Specified'
                )

        # Add a newline at the end
        sys.stdout.write('\n')
        self.stdout.write(self.style.SUCCESS(
            f'Successfully imported data for {total_rows} countries in year {year}'
        ))
