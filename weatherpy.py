import csv
import matplotlib.pyplot as plt
import requests
from random import uniform
from citipy import citipy
import pandas as pd
import numpy as np
from config import api_key


# Save config information.

url = "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"
# Build partial query URL

query_url = f"{url}appid={api_key}&units={units}&q="

# numpy.random.uniform(low=0.0, high=1.0, size=None)
i=0
cities=[i]
temp=[]

lat = np.random.uniform(low=-90.0, high=90.0,size=1300)
long = np.random.uniform(low=-180.0, high=180.0,size=1300)

# append list of cities
for x in range(10):
    city=citipy.nearest_city(lat[x],long[x])
    cityname=city.city_name
    cities.append(cityname)
    i=i+1
    response = requests.get(query_url + cities[i]).json()
    temp.append(response["main"]["temp"])
    
    
print(temp)
    
    
