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

1. Tourism Accomodation Investment 
2. Tourism General Investment 

### Revenue

1. Tourism Revenue

### Food

1. Registered Restaurants
2. Food Quality Distribution

### Location/Sites

1. Attraction Types
2. Attraction Statistics 

### People

1. Arrival Statistics
2. Age Statistics

### Misc Services

1. Distribution of other tourism services

## Development

See [DEVELOP.md](DEVELOP.md)
