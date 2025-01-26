from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from touristats.utils.model_util import verified_model


class TimeFrame(models.Model):
    year = models.IntegerField()
    month = models.IntegerField(null=True, blank=True)

    class Meta:
        unique_together = ["year", "month"]

    def __str__(self):
        return f"{self.year}" + (f"-{self.month}" if self.month else "")


class AllCountryStats(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.CharField(max_length=100)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    passengers = models.IntegerField()
    days_of_stay = models.IntegerField(default=0)
    purpose_of_visit = models.CharField(max_length=100, default="Not Specified")

    class Meta:
        unique_together = ["country_id", "timeframe"]

    def __str__(self):
        return f"""
        Country: {self.country},
        Year: {self.timeframe.year},
        Month: {self.timeframe.month},
        Passengers: {self.passengers}
        """


@receiver(pre_save, sender=AllCountryStats)
def generate_country_id(sender, instance, **kwargs):
    """
    Generate a unique country_id if not already set.
    Format: Simplified country name in uppercase with spaces replaced by underscores
    Example: "United States of America" -> "UNITED_STATES_OF_AMERICA"
    """
    if not instance.country_id:
        # Convert country name to uppercase and replace spaces with underscores
        country_id = instance.country.upper().replace(" ", "_")
        # Remove any special characters
        country_id = "".join(e for e in country_id if e.isalnum() or e == "_")
        instance.country_id = country_id


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 22 2025",
)
class AccomodationCategorization(models.Model):
    """
    The accomodation categories are like 1-5 start hotels, eco-lodges, guest-houses,
    hostels, etc. The stats are recorded with number of rooms per each establishment.

    Vefification History:
      1st Normalization Done (Jan 22 2025).

    Example
    --------
    2023 Report on : Year in Review
    Table 07: SLTDA registered accommodation establishments,2022 & 2023
    """

    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    categorization = models.CharField(max_length=100)
    establishments = models.IntegerField()
    rooms = models.IntegerField()

    def __str__(self):
        return f"""
        Categorization: {self.categorization},
        Establishments: {self.establishments},
        Rooms: {self.rooms}
    """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class RegisteredRestaurants(models.Model):
    """
    Registered Restaurants

    Example:
    --------
    2018 Q1 Report on: Year in Review
    Geographical Distribution of SLTDA Registered Restaurants
    """

    restaurant_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    district = models.CharField(max_length=100)
    establishments = models.IntegerField()

    def __str__(self):
        return f"District: {self.district}, Establishments: {self.establishments}"


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class TourismAccomodationInvestment(models.Model):
    """
    Tourism Accomodation Investment

    Example:
    --------

    2018 Q1 Report on: Year in Review
    Page 5: TOURISM ACCOMMODATION INVESTMENTS

    2023 Report on: Year in Review
        Number of investment projects received and approved
            Table: 19 Investment projects received and approved
    """

    investment_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    number_of_projects = models.IntegerField()
    number_of_rooms = models.IntegerField()
    total_investment = models.IntegerField()
    foreign_investment = models.IntegerField()
    local_investment = models.IntegerField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Total Investment: {self.total_investment},
        Foreign Investment: {self.foreign_investment},
        Local Investment: {self.local_investment}
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 22 2025",
)
class RoomDistribution(models.Model):
    """
    Per District the number of rooms and projects.

    Vefification History:
      1st Normalization Done (Jan 22 2025).

    Example:
    --------
    2023 Report on : Year in Review
    Table 18: Investment Projects received since 2010 to 31st December 2023
    """

    room_distribution_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    project_status = models.CharField(max_length=100, default="Not Specified")
    district = models.CharField(max_length=100)
    number_of_rooms = models.IntegerField()
    number_of_projects = models.IntegerField()
    investment = models.FloatField(default=0.0)

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Project Status: {self.project_status},
        Number of Rooms: {self.number_of_rooms},
        Number of Projects: {self.number_of_projects}
        """


class UnmanagedModel(models.Model):
    class Meta:
        abstract = True
        managed = False


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 22 2025",
)
class AccomodationTypeDistribution(UnmanagedModel):
    """
    NOTE: THIS CAN BE INFERRED BY AccomodationCategorization ENTITY.

    Vefification History:
      1st Normalization Done (Jan 22 2025).

    Distribution of the type of accomodation facilities used by tourists.
    Categories: With Friends, Apartment, Botique Hotels, Guest House, Home Stay, Hotels
    Example
    --------
    2018 Q1 Report on : Year in Review
    Page 7: Type of Accommodation Facilities Used
    """

    accomodation_type_distribution_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    type_of_accomodation = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Type of Accomodation: {self.type_of_accomodation},
        Percentage: {self.percentage} %
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 22 2025",
)
class RoomQualityDistribution(models.Model):
    """
    Distribution of the quality of rooms used by tourists.
    NOTE: THIS HAS BEEN OMITTED FROM THE NEWER DATASETS.

    Vefification History:
      1st Normalization Done (Jan 22 2025).

    Example
    --------
    2018 Q1 Report on : Year in Review
    Page 7: Quality of Rooms Pie-Chart
    """

    room_quality_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    room_quality = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Room Quality: {self.room_quality},
        Percentage: {self.percentage} %
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class FoodQualityDistribution(models.Model):
    """
    Distribution of the quality of food used by tourists.
    NOTE: THIS HAS BEEN OMITTED FROM THE NEWER DATASETS.

    Example
    --------
    2018 Q1 Report on : Year in Review
    Page 7: Quality of Food Pie-Chart
    """

    food_quality_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    food_quality = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Food Quality: {self.food_quality},
        Percentage: {self.percentage} %
        """


class ServiceQualityDistribution(models.Model):
    service_quality_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    service_quality = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Service Quality: {self.service_quality},
        Percentage: {self.percentage} %
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class AirConnectivityDistribution(models.Model):
    """
    Distribution of the air connectivity of tourists.

    Example:
    --------
    2024 Report on: Year in Review
    Page 24: Contribution of Airlines on tourist arrivals to Sri Lanka
    """

    air_connectivity_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    airline = models.CharField(max_length=100)
    number_of_passengers = models.IntegerField()
    percentage = models.FloatField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Airline: {self.airline},
        Number of Passengers: {self.number_of_passengers},
        Percentage: {self.percentage} %
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class PrimaryFinalPortOfDeparture(models.Model):
    """
    Distribution of the primary final port of departure of tourists.

    Example:
    --------
    2023 Report on : Year in Review
    Table 14: Main final departure airports to Sri Lanka
    """

    route_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    rank = models.IntegerField()
    port_of_departure = models.CharField(max_length=100)
    number_of_passengers = models.IntegerField()
    destination = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Port of Departure: {self.port_of_departure},
        Number of Passengers: {self.number_of_passengers},
        Percentage: {self.percentage} %
        """


class DistributionOfTourismServices(models.Model):
    """

    District
    Camping Sites
    Eco lodge
    Restaurants
    Tourist friendly
    eating places
    Tourist Shops
    Water Sports
    Spice Garden
    Travel agencies
    Spa

    Example
    --------
    2023 Report on : Year in Review
    Table: 13 Distribution of other tourism services by districts
    """

    service_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Service: {self.service},
        District: {self.district},
        Service Type: {self.service_type},
        Percentage: {self.percentage} %
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class TourismIncome(models.Model):
    """
    Tourism Income

    Example:
    --------
    2024 Report on: Year in Review
    Table 7 : Tourism income

    2023 Report on: Year in Review
    Page 33: Tourism income

    """

    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    number_of_tourists = models.IntegerField()
    average_expenditure_month = models.FloatField()
    average_expenditure_day = models.FloatField()
    total_value = models.FloatField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Month: {self.timeframe.month},
        Number of Tourists: {self.number_of_tourists},
        Average Expenditure Month: {self.average_expenditure_month},
        Average Expenditure Day: {self.average_expenditure_day},
        Total Value: {self.total_value}
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class Attraction(models.Model):
    """
    Attraction: Tourist attractions.

    Example:
    --------
    2023 Report on: Year in Review
    Table: 13 Distribution of other tourism services by districts
    """

    attraction_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    location_type = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Location: {self.location},
        Location Type: {self.location_type},
        District: {self.district}
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class TourismIncomeClassification(models.Model):
    """
    Tourism Income Classification by Attraction

    Example:
    --------
    2024 Report on: Year in Review
    Table 7 : Tourism income
    """

    income_classification_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    local_revenue = models.FloatField()
    foreign_revenue = models.FloatField()
    number_of_local_visitors = models.IntegerField()
    number_of_foreign_visitors = models.IntegerField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Attraction: {self.attraction},
        Local Revenue: {self.local_revenue},
        Foreign Revenue: {self.foreign_revenue},
        Number of Local Visitors: {self.number_of_local_visitors},
        Number of Foreign Visitors: {self.number_of_foreign_visitors}
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class AgeCategoryDistribution(models.Model):
    """
    Age Category Distribution

    Example:
    --------
    2023 Report on: Year in Review
    Table: 02: Tourist arrivals by age category, 2023
    """

    age_category_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    age_category = models.CharField(max_length=100)
    percentage = models.FloatField()

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Age Category: {self.age_category},
        Percentage: {self.percentage} %
        """


class QualityMetrics(models.Model):
    METRIC_TYPES = [
        ("ROOM", "Room Quality"),
        ("FOOD", "Food Quality"),
        ("SERVICE", "Service Quality"),
    ]

    metric_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    metric_type = models.CharField(max_length=20, choices=METRIC_TYPES)
    quality_level = models.CharField(max_length=100)
    percentage = models.FloatField()

    class Meta:
        unique_together = ["timeframe", "metric_type", "quality_level"]

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Metric Type: {self.metric_type},
        Quality Level: {self.quality_level},
        Percentage: {self.percentage} %
        """


class CategoryDistribution(models.Model):
    category_id = models.CharField(max_length=100, primary_key=True)
    CATEGORY_TYPES = [
        ("ACCOMMODATION", "Accommodation Type"),
        ("AGE", "Age Category"),
    ]

    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    category_type = models.CharField(max_length=20, choices=CATEGORY_TYPES)
    category_value = models.CharField(max_length=100)
    percentage = models.FloatField()

    class Meta:
        unique_together = ["timeframe", "category_type", "category_value"]

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Category Type: {self.category_type},
        Category Value: {self.category_value},
        Percentage: {self.percentage} %
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class TourismInvestment(models.Model):
    """
    Tourism Investment

    Example:
    --------
    2023 Report on: Year in Review
    Table 18: Investment Projects received since 2010 to 31st December 2023
    """

    investment_id = models.CharField(max_length=100, primary_key=True)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    district = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    number_of_projects = models.IntegerField()
    number_of_rooms = models.IntegerField()
    total_investment = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Status: {self.status},
        Number of Projects: {self.number_of_projects},
        Number of Rooms: {self.number_of_rooms},
        Total Investment: {self.total_investment},
        """


@verified_model(
    version="1.0",
    description="Initial version of the model",
    verified_by="Vibhatha",
    data_source="SLTDA",
    date="Jan 24 2025",
)
class AttractionStats(models.Model):
    """
    Attraction Stats

    Example:
    --------
    2023 Report on: Year in Review
    Table:15 Visitors to wildlife parks, 2024 and the following.
    """

    attraction_id = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    timeframe = models.ForeignKey(TimeFrame, on_delete=models.CASCADE)
    visitors = models.JSONField(default=dict)  # Store visitor counts and income in JSON

    def __str__(self):
        return f"""
        Year: {self.timeframe.year},
        Attraction: {self.attraction_id},
        Visitors: {self.visitors}
        """
