# traveller

Traveller is a navigation on tourism related aspects of Sri Lanka. 

## Nature of Data

The data is collected from reports that have been published by the Sri Lanka Tourism Development Authority (SLTDA). It consists of a variety of data that have been collected. The reports are given in both annual and quarterly formats. Each data set will give a summarised view of the tourism data. 

Tourism data collection contains the following major components:

1. Transport
2. Accommodation
3. Investment
4. Revenue
5. Food
6. Location/Sites
7. People
8. Misc Services (e.g. Spa, Water Sports, etc.)

### Transport 

1. Air Connectivity - month : Integar, year : Integar, airline : CharField, number_of_passengers : Integar, percentage : FloatField 
2. Primary Final Ports (Prior to Arrival in Sri Lanka) - month : Integar, year : Integar, route_id : CharField, rank : Integar, port_of_departure : CharField, number_of_passengers : Integar, destination : CharField, percentage : FloatField 


### Accommodation (Verified)

1. Accomodation Categories - month : Integar, year : Integar, country : CharField, categorization : CharField, establishments : Integar, rooms : Integar 
2. Room Distribution 
3. Accomodation Type Distribution 
4. Room Quality Distribution 


### Investment

1. Tourism Accomodation Investment - month : Integar, year : Integar, status : CharField, number_of_projects : Integar, number_of_rooms : Integar, total_investment : Integar, foreign_investment : Integar, local_investment : Integar 
2. Tourism General Investment - month : Integar, year : Integar, district : CharField, status : CharField, number_of_projects : Integar, number_of_rooms : Integar, total_investment : Integar, foreign_investment : Integar, local_investment : Integar 

### Revenue

1. Tourism Revenue - 

### Food

1. Registered Restaurants - month : Integar, year : Integar, restaurant_id : CharField, district : CharField, establishments : Integar 
2. Food Quality Distribution - month : Integar, year : Integar, food_quality_id : CharField, food_quality : CharField, percentage : FloatField 

### Location/Sites

1. Attraction Types - 
2. Attraction Statistics - month : Integar, year : Integar, attraction_id : CharField, visitors : JSONField 

### People

1. Arrival Statistics 
2. Age Statistics

### Misc Services

1. Distribution of other tourism services - 

## Development

See [DEVELOP.md](DEVELOP.md)


### data entry specification 

1. If data is unknown - None 
2. If data is not applicable - NA
