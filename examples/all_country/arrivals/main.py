from traveller.data.loader import DataLoader
import pandas as pd
from traveller.data.trend_analyzer import MonthlyTrendAnalyzer
from traveller.plot.plotter import TrendPlotter

year = 2019
file_path = "data/arrival/all_countries/all_country_arrivals_" + str(year) + ".csv"
data_loader = DataLoader(file_path)
data_loader.load_data()
data = data_loader.get_data()


if data is not None:
    df = data.to_pandas()
    monthly_trend_analyzer = MonthlyTrendAnalyzer(df)
    trend = monthly_trend_analyzer.analyze_trend(2019)

    trend_plotter = TrendPlotter()
    trend_plotter.plot_trend(trend, 'Month', 'Arrivals', 'Monthly Tourist Arrivals by Country', 'Month', 'Arrivals', 'Year')