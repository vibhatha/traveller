import pandas as pd

class BaseTrendAnalyzer:
    def __init__(self, data_frame):
        self.data_frame = data_frame
        

    def transform_data(self, year):
        # Ensure all monthly columns are numeric
        months = ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December']
        
        for month in months:
            # Convert each month's data to numeric, coercing errors to NaN
            self.data_frame[month] = pd.to_numeric(self.data_frame[month].str.replace(',', ''), errors='coerce')
        
        # Drop the 'Total' column if it exists
        if 'Total' in self.data_frame.columns:
            self.data_frame = self.data_frame.drop(columns=['Total'])
        
        # Filter out rows where 'Country' is empty or NaN
        self.data_frame = self.data_frame[self.data_frame['Country'].notna() & self.data_frame['Country'].str.strip().astype(bool)]
        
        # Add a Year column if not present
        if 'Year' not in self.data_frame.columns:
            self.data_frame['Year'] = year  # Adjust this logic to dynamically assign years if needed
        
        # Convert wide format to long format
        self.data_frame = self.data_frame.melt(id_vars=['Country', 'Year'], 
                                               value_vars=months,
                                               var_name='Month', value_name='Arrivals')
        
        # Map month names to numbers for sorting
        month_order = months
        self.data_frame['Month'] = pd.Categorical(self.data_frame['Month'], categories=month_order, ordered=True)

        # Convert Arrivals to numeric, coercing errors to NaN
        self.data_frame['Arrivals'] = pd.to_numeric(self.data_frame['Arrivals'], errors='coerce')

        # Handle NaN values in Arrivals only
        self.data_frame['Arrivals'].fillna(0, inplace=True)

class MonthlyTrendAnalyzer(BaseTrendAnalyzer):
    def analyze_trend(self, year):
        self.transform_data(year)

        # Group by year, month, and country, then sum the arrivals
        trend = self.data_frame.groupby(['Year', 'Month', 'Country'])['Arrivals'].sum().reset_index()
        return trend