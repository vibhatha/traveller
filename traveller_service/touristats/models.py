from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class TimeFrame(models.Model):
    year = models.IntegerField()
    month = models.IntegerField(null=True, blank=True)
    
    class Meta:
        unique_together = ['year', 'month']

    def __str__(self):
        return f"{self.year}" + (f"-{self.month}" if self.month else "")


class AllCountryStats(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.CharField(max_length=100)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    passengers = models.IntegerField()
    days_of_stay = models.IntegerField(default=0)
    purpose_of_visit = models.CharField(max_length=100, default='Not Specified')

    class Meta:
        unique_together = ['country_id', 'timeframe']

    def __str__(self):
        return f"Country: {self.country}, Year: {self.timeframe.year}, Month: {self.timeframe.month}, Passengers: {self.passengers}"

@receiver(pre_save, sender=AllCountryStats)
def generate_country_id(sender, instance, **kwargs):
    """
    Generate a unique country_id if not already set.
    Format: Simplified country name in uppercase with spaces replaced by underscores
    Example: "United States of America" -> "UNITED_STATES_OF_AMERICA"
    """
    if not instance.country_id:
        # Convert country name to uppercase and replace spaces with underscores
        country_id = instance.country.upper().replace(' ', '_')
        # Remove any special characters
        country_id = ''.join(e for e in country_id if e.isalnum() or e == '_')
        instance.country_id = country_id


class AccomodationCategorization(models.Model):
    category_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    categorization = models.CharField(max_length=100)
    establishments = models.IntegerField()
    rooms = models.IntegerField()

    def __str__(self):
        return f"Categorization: {self.categorization}, Establishments: {self.establishments}, Rooms: {self.rooms}"


class RegisteredRestaurants(models.Model):
    restaurant_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    district = models.CharField(max_length=100)
    establishments = models.IntegerField()

    def __str__(self):
        return f"District: {self.district}, Establishments: {self.establishments}"


class TourismAccomodationInvestment(models.Model):
    investment_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    number_of_projects = models.IntegerField()
    number_of_rooms = models.IntegerField()
    total_investment = models.IntegerField()
    foreign_investment = models.IntegerField()
    local_investment = models.IntegerField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Total Investment: {self.total_investment}, Foreign Investment: {self.foreign_investment}, Local Investment: {self.local_investment}"


class RoomDistribution(models.Model):
    room_distribution_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    project_status = models.CharField(max_length=100)
    number_of_rooms = models.IntegerField()
    number_of_projects = models.IntegerField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Project Status: {self.project_status}, Number of Rooms: {self.number_of_rooms}, Number of Projects: {self.number_of_projects}"
    

class AccomodationTypeDistribution(models.Model):
    accomodation_type_distribution_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    type_of_accomodation = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Type of Accomodation: {self.type_of_accomodation}, Percentage: {self.percentage} %"


class RoomQualityDistribution(models.Model):
    room_quality_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    room_quality = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Room Quality: {self.room_quality}, Percentage: {self.percentage} %"


class FoodQualityDistribution(models.Model):
    food_quality_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    food_quality = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Food Quality: {self.food_quality}, Percentage: {self.percentage} %" 
    

class ServiceQualityDistribution(models.Model):
    service_quality_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    service_quality = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Service Quality: {self.service_quality}, Percentage: {self.percentage} %"


class AirConnectivityDistribution(models.Model):
    air_connectivity_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    airline = models.CharField(max_length=100)
    number_of_passengers = models.IntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Airline: {self.airline}, Number of Passengers: {self.number_of_passengers}, Percentage: {self.percentage} %"


class PrimaryFinalPortOfDeparture(models.Model):
    route_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    rank = models.IntegerField()
    port_of_departure = models.CharField(max_length=100)
    number_of_passengers = models.IntegerField()
    destination = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Port of Departure: {self.port_of_departure}, Number of Passengers: {self.number_of_passengers}, Percentage: {self.percentage} %"
    

class DistributionOfTourismServices(models.Model):
    service_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Service: {self.service}, District: {self.district}, Percentage: {self.percentage} %"   
    
class TourismIncome(models.Model):
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    number_of_tourists = models.IntegerField()
    average_expenditure_month = models.FloatField()
    average_expenditure_day = models.FloatField()
    total_value = models.FloatField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Month: {self.timeframe.month}, Number of Tourists: {self.number_of_tourists}, Average Expenditure Month: {self.average_expenditure_month}, Average Expenditure Day: {self.average_expenditure_day}, Total Value: {self.total_value}"


class AgeCategoryDistribution(models.Model):
    age_category_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    age_category = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Age Category: {self.age_category}, Percentage: {self.percentage} %" 
    

class AttractionTypeDistribution(models.Model):
    attraction_type_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    location_type = models.CharField(max_length=100)
    number_of_foreign_visitors = models.IntegerField()
    number_of_local_visitors = models.IntegerField()
    local_visitor_income = models.FloatField()
    foreign_visitor_income = models.FloatField()

    def __str__(self):
        return f"Year: {self.timeframe.year}, Location: {self.location}, Location Type: {self.location_type},Number of Foreign Visitors: {self.number_of_foreign_visitors}, Number of Local Visitors: {self.number_of_local_visitors}, Local Visitor Income: {self.local_visitor_income}, Foreign Visitor Income: {self.foreign_visitor_income}"

class QualityMetrics(models.Model):
    METRIC_TYPES = [
        ('ROOM', 'Room Quality'),
        ('FOOD', 'Food Quality'),
        ('SERVICE', 'Service Quality'),
    ]
    
    metric_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    metric_type = models.CharField(max_length=20, choices=METRIC_TYPES)
    quality_level = models.CharField(max_length=100)
    percentage = models.FloatField()

    class Meta:
        unique_together = ['timeframe', 'metric_type', 'quality_level']

class CategoryDistribution(models.Model):
    category_id = models.CharField(max_length=100, primary_key=True)
    CATEGORY_TYPES = [
        ('ACCOMMODATION', 'Accommodation Type'),
        ('AGE', 'Age Category'),
    ]
    
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPES)
    category_value = models.CharField(max_length=100)
    percentage = models.FloatField()

    class Meta:
        unique_together = ['timeframe', 'category_type', 'category_value']

class TourismInvestment(models.Model):
    investment_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    number_of_projects = models.IntegerField()
    number_of_rooms = models.IntegerField()
    total_investment = models.DecimalField(max_digits=15, decimal_places=2)
    foreign_investment = models.DecimalField(max_digits=15, decimal_places=2)
    local_investment = models.DecimalField(max_digits=15, decimal_places=2)

class AttractionStats(models.Model):
    attraction_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    location_type = models.CharField(max_length=100)
    visitors = models.JSONField(default=dict)  # Store visitor counts and income in JSON
