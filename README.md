# traveller

Traveller is a navigation on tourism related aspects of Sri Lanka. 

## Pre-requisites

### Setup Mamba environment

```bash
mamba create -n traveller_env python=3.9
```

```bash
mamba install pandas python-dotenv django psycopg2-binary
```

### Login to the Neon PostgreSQL database

https://console.neon.tech/

## Data Collection

---

### Arrival Data

[Source](https://www.sltda.gov.lk/en/weekly-tourist-arrivals-reports-2023)

Each weekly report includes the following:
1. A summary of monthly tourist arrivals
2. Daily tourist arrival data
3. Weekly total of tourist arrivals
4. A distribution chart displaying both the total number of arrivals and the average for the month
5. Weekly distribution of tourist arrivals
6. A breakdown of the top 10 countries of origin for tourists, along with the number of arrivals from other countries


As per Jan 16th 2025, this source contains data for years 2023, 2024 and 2025. 

Download data by `scripts/download_tourism_data.sh data/urls_<year>.txt /data/<year>`

---

### Annual and quarterly report of the tourism industry

The above link shows a more comprehensive detailed annual and quarterly report of the tourism industry from 2018-2024.

Each report includes the following:

#### Tourist Arrivals to Sri Lanka 

1. Tourist arrivals by month 
2. Tourist arrivals by region
3. Tourist arrivals by age and sex 
4. Top source markets to lanka

#### Tourism Accommodation 

1. Purpose of stay 
2. Average duration of stay 
3. Tourism income 
4. SLTDA registered accommodation establishments
5. Room distribution by - 
    1. Province 
    2. District 
    3. Star category 
6. Distribution of other tourism services 

#### Air Connectivity 

1. Air connectivity to and from Sri Lanka 
2. International airlines to Sri Lanka 

#### Visitors to major tourist attractions

1. Visitors to wild life parks 
2. Visitors to conservation forests 
3. Visitors to tourist attractions administered by Central Fund 
4. Visitors to Botanical Gardens 
5. Visitors to Museums 
6. Visitors to Zoological Gardens

#### Tourist accommodation investment 

1. Tourism investment projects received 
2. Investment projects received & approved

### Annual Arrival All Country 

1. Monthly Arrival for Each Country


---

## Insert Data

```bash
python manage.py makemigrations
python manage.py migrate
```

## Drop Table or Cleanup

Make sure to delete the everything within `arrivals/migrations` folder except `__init__.py`.

Then, 

```bash
python manage.py makemigrations
python manage.py migrate
```
