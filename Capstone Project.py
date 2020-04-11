#!/usr/bin/env python
# coding: utf-8

# # This notebook will be used mainly for the capstone project

# In[14]:


import pandas as pd


# In[15]:


import numpy as np


# In[11]:


print("Hello Capstone Project Course!")


# # Part One of Capstone : Explain your problem and your data

# ### 1. Introduction/Business Problem

# Which city is the best city to live in? This project will compare two cities, Toronto and New York City. Both cities are very diverse and are the financial capitals of their respective countries. When the two are compared, which one will be considered the best city to live in? For someone who is looking between New York City and Toronto for a job relocation, for example, this is an important question. Some things to consider for finding a new home are safety, housing market, and amenities such as restaurants, parks, and entertainment. And within both cities, which neighborhood is the best to live in? This project aims to provide insight and answer these questions based on the parameters.

# ### 2. Data

# In order to answer these questions, we will need to pull data for each aspect of the search. The data for the project will include geographical data such as neighbhorhoods and boroughs, crime data, housing data, and then data collected from Foursquare for restaurants, parks, and entertainments for both New York City and Toronto. The geographical data will need to include neighborhoods, boroughs, and postal codes for both cities in order to use maps and segment into neighbhorhoods for the rest of the data for this project.
# 
# The crime data will need to include neighborhoods/boroughs, and lists of crime categories such as assault and theft for both cities. This will provide insight for the relative safety of both cities both on the city-wide level and neighborhood level, which can be shown in a choropleth map.
# 
# Housing data is also important in terms of whether or not you can afford to live in the cities. The housing data needs to include renting prices, costs of houses, and preferably cost of living and organizes by neighborhoods or boroughs.
# 
# The data on amenities such as restaurants, parks, and entertainment (movie theaters, for example) will be found and collected using Foursquare. This is important especially on the neighbhorhood level to make a decision on which neighborhood is the best to live in based on the amenities available.
# 
# By using these data, the project aims to accumulate a score for each neighborhood and an overall score for both cities.
# 
# 

# #### Sources for the Capstone Project Data

# GEOGRAPHICAL DATA: The geographical data for Toronto: https://en.wikipedia.org/w/index.php?title=List_of_postal_codes_of_Canada:_M&oldid=945633050 New York City data will be pulled from Geopy
# 
# CRIME: Crime Data for New York - https://www1.nyc.gov/assets/nypd/downloads/excel/analysis_and_planning/historical-crime-data/seven-major-felony-offenses-2000-2019.xls. This is the overal view by types of felonies and by year. https://www.kaggle.com/adamschroeder/crimes-new-york-city/download -> the 2014 crime data set for all New York Boroughs found from https://www.kaggle.com/adamschroeder/crimes-new-york-city#Crime_Column_Description.csv
# 
# Crime data for Toronto came from the site, http://data.torontopolice.on.ca/pages/open-data
# 
# Assault: https://opendata.arcgis.com/datasets/a5029dcd67214cc594a500865f868284_0.geojson -Auto Theft:https://opendata.arcgis.com/datasets/ca9730d5840343f7bfa3f5ffd16c2f0a_0.geojson -Break and Enter:https://opendata.arcgis.com/datasets/8ab59b498f6d4eae8ec631a287550376_0.geojson -Homicide:https://opendata.arcgis.com/datasets/7826a3ef2eff4d64a7f70e909de007b5_0.geojson -Robbery:https://opendata.arcgis.com/datasets/9115accc55f24938b4eb573dd222c33b_0.geojson -Theft Over: https://opendata.arcgis.com/datasets/19d66b66abe749e7b5be1a86e272f8ea_0.geojson
# HOUSING PRICES: Housing prices for New York Housing dataset (rental): ('C:\Users\Amanda\Desktop\NYC Housing Data\clean2.csv') from https://www.kaggle.com/ted8080/nyc-housing-dataset-extrinsic-factors
# 
# Housing prices for Toronto Apartmental rentals : ('C:\Users\Amanda\Desktop\Toronto Housing Data\Toronto Apartment Rental\Toronto_apartment_rentals_2018') from https://www.kaggle.com/rajacsp/toronto-apartment-price House sales : ('C:\Users\Amanda\Desktop\Toronto Housing Data\Ontario House Sales\properties.csv') from https://www.kaggle.com/mnabaee/ontarioproperties
# 
# AMENITIES: Restaurants Boutiques Entertainmnet (Movie Theaters, Bowling, Bars, etc) Will be found on Foursquare

# # Part Two of Capstone: The Data Manipulation and Analysis

# ## Pull All The Data and Preprocess Them

# In[16]:


#import all the libraries
import numpy as np # library to handle data in a vectorized manner
import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import json # library to handle JSON files
get_ipython().system("conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab *already downloaded")
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe
# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors
# import k-means from clustering stage
from sklearn.cluster import KMeans
get_ipython().system("conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab")
import folium # map rendering library
print('Libraries imported.')


# ### Geographical Data - Toronto

# In[18]:


get_ipython().system('pip install lxml')
import lxml


# In[19]:


# Download and explore the Toronto Dataset
url='https://en.wikipedia.org/w/index.php?title=List_of_postal_codes_of_Canada:_M&oldid=945633050'

Tordf = pd.read_html(url)
Tordf = Tordf[0]
print('imported dataframe has', Tordf['Postcode'].count(), 'postcodes entries')

Tordf.head(5)


# In[20]:


#Preprocessing
#Toronto - Get rid of the "Not assigned" / Replace
Tordf = Tordf[Tordf["Borough"] != "Not assigned"]

#Replace the N/A values of Neighborhood with the Borough Value
Tordf["Neighbourhood"].replace("Not assigned", Tordf["Borough"], inplace=True)

Tordf.head(5)


# In[21]:


#Now combine all the neighbourhoods with the same postal codes
Tordf = Tordf.groupby(["Postcode","Borough"])["Neighbourhood"].apply(list)
Tordf = Tordf.sample(frac=1).reset_index()
Tordf["Neighbourhood"] = Tordf["Neighbourhood"].str.join(', ')
Tordf.head(5)


# In[22]:


# Check to make sure there are 103 lines and 3 columns at this point
Tordf.shape


# In[23]:


#Need to get the Latitudes and Longitudes for the Postal codes
get_ipython().system('pip install geocoder')
import geocoder

Torlat_list = []
Torlng_list = []
for i in range(Tordf.shape[0]):
    Toraddress ='{}, Toronto, Ontario'.format(Tordf.at[i,'Postcode'])
    g=geocoder.arcgis(Toraddress)
    Torlat_list.append(g.latlng[0])
    Torlng_list.append(g.latlng[1])
    
Tordf['Latitude'] = Torlat_list
Tordf['Longitude'] = Torlng_list
    
Tordf.head(5)   


# In[24]:


# Get Latitude and Longitude for Toronto
Toraddress = 'Toronto, Ontario'
geolocator = Nominatim(user_agent="Toronto_explorer")
Tlocation = geolocator.geocode(Toraddress)
Tlatitude = Tlocation.latitude
Tlongitude = Tlocation.longitude
print('The geographical coordinate of Toronto are {}, {}.'.format(Tlatitude,Tlongitude))


# In[25]:


# Create map of Toronto with the neighbourhoods imposed on it
# create map of Toronto using latitude and longitude values
map_toronto = folium.Map(location=[Tlatitude, Tlongitude], zoom_start=10)

# add markers to map
for lat, lng, borough, neighbourhood in zip(Tordf['Latitude'], Tordf['Longitude'], Tordf['Borough'], Tordf['Neighbourhood']):
    label ='{}, {}'.format(neighbourhood, borough) 
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
    
map_toronto


# In[26]:


## The Scarborough of Toronto *Will use later on

Scarborough_data = Tordf[Tordf['Borough'] == 'Scarborough'].reset_index(drop=True)
Scarborough_data.head(5)


# In[27]:


#Get the geographical coordinates of Scarborough
SCARaddress = 'Scarborough, ON'

SCARgeolocator = Nominatim(user_agent="ny_explorer")
SCARlocation = geolocator.geocode(SCARaddress)
SCARlatitude = SCARlocation.latitude
SCARlongitude = SCARlocation.longitude
print('The geograpical coordinate of Manhattan are {}, {}.'.format(SCARlatitude, SCARlongitude))


# In[28]:


#create a map
map_Scarborough = folium.Map(location=[SCARlatitude, SCARlongitude], zoom_start=11)

# add markers to map
for lat, lng, label in zip(Scarborough_data['Latitude'], Scarborough_data['Longitude'], Scarborough_data['Neighbourhood']):
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_Scarborough)  
    
map_Scarborough


# ### Geographical Data - New York City

# In[29]:


# Download and explore the new York City dataset
get_ipython().system("wget -q -O 'newyork_data.json' https://cocl.us/new_york_dataset")
print('Data downloaded!')


# In[30]:


with open('newyork_data.json') as json_data:
    newyork_data = json.load(json_data)


# In[ ]:


#take a look at the data
#newyork_data


# In[31]:


#the relevant data is in the features key, which is basically a list of neighborhoods
NY_data = newyork_data['features']


# In[32]:


NY_data[0]


# In[33]:


# Transform the NY Data into a Pandas dataframe
# define the dataframe columns
column_names = ['Borough', 'Neighborhood', 'Latitude', 'Longitude'] 

# instantiate the dataframe
NYdf = pd.DataFrame(columns=column_names)

# Make sure the columns are correct
NYdf


# In[34]:


# Then let's loop through the data and fill the dataframe one row at a time
for data in NY_data:
    borough = neighborhood_name = data['properties']['borough'] 
    neighborhood_name = data['properties']['name']
        
    neighborhood_latlon = data['geometry']['coordinates']
    neighborhood_lat = neighborhood_latlon[1]
    neighborhood_lon = neighborhood_latlon[0]
    
    NYdf = NYdf.append({'Borough': borough,
                        'Neighborhood': neighborhood_name,
                        'Latitude': neighborhood_lat,
                        'Longitude': neighborhood_lon}, ignore_index=True)


# In[35]:


# Examine the resulting dataframe
NYdf.head(5)


# In[36]:


# Make sure that the dataset has all 5 boroughs and 306 neighborhoods
print('The dataframe has {} boroughs and {} neighborhoods.'.format(
        len(NYdf['Borough'].unique()),
        NYdf.shape[0]
    )
)


# In[37]:


# Use geopy library to get the latitude and longitude values of New York City
# In order to define an instance of the geocoder, we need to define a user_agent. We will name our agent ny_explorer
NYaddress = 'New York City, NY'

geolocator = Nominatim(user_agent="ny_explorer")
NYlocation = geolocator.geocode(NYaddress)
NYlatitude = NYlocation.latitude
NYlongitude = NYlocation.longitude
print('The geograpical coordinate of New York City are {}, {}.'.format(NYlatitude, NYlongitude))


# In[38]:


# Create a map of New York with neighborhoods superimposed on top
# create map of New York using latitude and longitude values
map_newyork = folium.Map(location=[NYlatitude, NYlongitude], zoom_start=10)

# add markers to map
for lat, lng, borough, neighborhood in zip(NYdf['Latitude'], NYdf['Longitude'], NYdf['Borough'], NYdf['Neighborhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_newyork)  
    
map_newyork


# In[39]:


#The Borough of Manhatten of New York City
manhattan_data = NYdf[NYdf['Borough'] == 'Manhattan'].reset_index(drop=True)
manhattan_data.head()


# In[40]:


#Get the geographical coordinates of Manhatten
MANaddress = 'Manhattan, NY'

MANgeolocator = Nominatim(user_agent="ny_explorer")
MANlocation = geolocator.geocode(MANaddress)
MANlatitude = MANlocation.latitude
MANlongitude = MANlocation.longitude
print('The geograpical coordinate of Manhattan are {}, {}.'.format(MANlatitude, MANlongitude))


# In[41]:


# create map of Manhattan using latitude and longitude values
map_manhattan = folium.Map(location=[MANlatitude, MANlongitude], zoom_start=11)

# add markers to map
for lat, lng, label in zip(manhattan_data['Latitude'], manhattan_data['Longitude'], manhattan_data['Neighborhood']):
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_manhattan)  
    
map_manhattan


# ### Foursquare Set Up

# In[42]:


# Define Foursquare Credentials and Version
CLIENT_ID = '5SZD033DFFP1BYV0EJNAO10QIFGX1T2MCSY2JMTQOP5BAYAH'
CLIENT_SECRET = 'WPMLWHCCGOSDK0GXBULP30WM0XEKVC5Y5NQYFZBBU0UA3YLJ'
VERSION = '20180604'
LIMIT = 30
print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)


# ### Amenities Data - Toronto

# #### Create a function to repeat the process for each neighborhood in Scarborough

# In[43]:


def getNearbyVenues(names, latitudes, longitudes, radius=500):
    venues_list=[]
    for name, lat, lng in zip(names, latitudes, longitudes):
        print(name)
            
        # create the API request URL
        url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
            CLIENT_ID, 
            CLIENT_SECRET, 
            VERSION, 
            lat, 
            lng, 
            radius, 
            LIMIT)
            
        # make the GET request
        results = requests.get(url).json()["response"]['groups'][0]['items']
        
        # return only relevant information for each nearby venue
        venues_list.append([(
            name, 
            lat, 
            lng, 
            v['venue']['name'], 
            v['venue']['location']['lat'], 
            v['venue']['location']['lng'],  
            v['venue']['categories'][0]['name']) for v in results])

    nearby_venues = pd.DataFrame([item for venue_list in venues_list for item in venue_list])
    nearby_venues.columns = ['Neighborhood', 
                  'Neighborhood Latitude', 
                  'Neighborhood Longitude', 
                  'Venue', 
                  'Venue Latitude', 
                  'Venue Longitude', 
                  'Venue Category']
    
    return(nearby_venues)


# In[44]:


#code to run the above function and append into a new dataframe
scar_venues = getNearbyVenues(names=Scarborough_data['Neighbourhood'],
                                   latitudes=Scarborough_data['Latitude'],
                                   longitudes=Scarborough_data['Longitude']
                                  )


# In[45]:


#check the dataframe
print(scar_venues.shape)
scar_venues.head(5)


# In[46]:


#Check how many venues were returned
scar_venues.groupby('Neighborhood').count()


# In[47]:


#How many unique categories of venues curated
print('There are {} uniques categories.'.format(len(scar_venues['Venue Category'].unique())))


# In[48]:


#### Analyze Each Scarborough Neighborhood
# one hot encoding
scar_onehot = pd.get_dummies(scar_venues[['Venue Category']], prefix="", prefix_sep="")

# add neighborhood column back to dataframe
scar_onehot['Neighborhood'] = scar_venues['Neighborhood'] 

# move neighborhood column to the first column
fixed_columns = [scar_onehot.columns[-1]] + list(scar_onehot.columns[:-1])
scar_onehot = scar_onehot[fixed_columns]

scar_onehot.head(5)


# In[49]:


#Examine the new dataframe size
scar_onehot.shape


# In[50]:


#group the neighbhorhood by taking the mean of frequency of occurrence
scar_grouped = scar_onehot.groupby('Neighborhood').mean().reset_index()
scar_grouped


# In[51]:


#confirm the new size
scar_grouped.shape


# ##### Let's print each neighborhood along with the top 5 most common venues

# In[57]:


Scar_num_top_venues = 5

for hood in scar_grouped['Neighborhood']:
    print("----"+hood+"----")
    temp = scar_grouped[scar_grouped['Neighborhood'] == hood].T.reset_index()
    temp.columns = ['venue','freq']
    temp = temp.iloc[1:]
    temp['freq'] = temp['freq'].astype(float)
    temp = temp.round({'freq': 2})
    print(temp.sort_values('freq', ascending=False).reset_index(drop=True).head(Scar_num_top_venues))
    print('\n')


# #### Let's put that into a pandas dataframe

# In[58]:


#First, let's write a function to sort the venues in descending order.
def return_most_common_venues(row, Scar_num_top_venues):
    row_categories = row.iloc[1:]
    row_categories_sorted = row_categories.sort_values(ascending=False)
    
    return row_categories_sorted.index.values[0:Scarnum_top_venues]


# In[59]:


#Now let's create the new dataframe and display the top 10 venues for each neighborhood.
Scarnum_top_venues = 10

indicators = ['st', 'nd', 'rd']

# create columns according to number of top venues
columns = ['Neighborhood']
for ind in np.arange(Scarnum_top_venues):
    try:
        columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
    except:
        columns.append('{}th Most Common Venue'.format(ind+1))

# create a new dataframe
Scarneighborhoods_venues_sorted = pd.DataFrame(columns=columns)
Scarneighborhoods_venues_sorted['Neighborhood'] = scar_grouped['Neighborhood']

for ind in np.arange(scar_grouped.shape[0]):
    Scarneighborhoods_venues_sorted.iloc[ind, 1:] = return_most_common_venues(scar_grouped.iloc[ind, :], Scarnum_top_venues)

Scarneighborhoods_venues_sorted.head()


# #### Cluster Neighborhoods

# In[60]:


#Run k-means to cluster the neighborhood into 5 clusters.
# set number of clusters
kclusters = 5

scar_grouped_clustering = scar_grouped.drop('Neighborhood', 1)

# run k-means clustering
SCARkmeans = KMeans(n_clusters=kclusters, random_state=0).fit(scar_grouped_clustering)

# check cluster labels generated for each row in the dataframe
SCARkmeans.labels_[0:10] 


# In[63]:


#Let's create a new dataframe that includes the cluster as well as the top 10 venues for each neighborhood
# add clustering labels
Scarneighborhoods_venues_sorted.insert(0, 'Cluster Labels', SCARkmeans.labels_)

scar_merged = Scarborough_data

# merge toronto_grouped with toronto_data to add latitude/longitude for each neighborhood
scar_merged = scar_merged.join(Scarneighborhoods_venues_sorted.set_index('Neighborhood'), on='Neighbourhood', how = 'right')

#scar_merged.dropna(axis=0, inplace = True) #drop any NaN values
#scar_merged.reset_index(drop=True) #reset index

scar_merged.head(20) # check the last columns!


# In[95]:


# Visualize the resulting clusters
# create map
SCARmap_clusters = folium.Map(location=[SCARlatitude, SCARlongitude], zoom_start=11)

# set color scheme for the clusters
x = np.arange(kclusters)
ys = [i + x + (i*x)**2 for i in range(kclusters)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array] #the values in rainbow are string


# add markers to the map
markers_colors = []
for lat, lon, poi, cluster in zip(scar_merged['Latitude'], scar_merged['Longitude'], scar_merged['Neighbourhood'], scar_merged['Cluster Labels']):
    label = folium.Popup(str(poi) + ' Cluster ' + str(cluster), parse_html=True)
    folium.CircleMarker(
        [lat, lon],
        radius=5,
        popup=label,
        color=rainbow[cluster-1],
        fill=True,
        fill_color=rainbow[cluster-1],
        fill_opacity=0.7).add_to(SCARmap_clusters)
       
SCARmap_clusters


# #### Examine Clusters

# ##### Cluster 1 - Fast Food/Pizza - Food/Restaurants

# In[94]:


scar_merged.loc[scar_merged['Cluster Labels'] == 0, scar_merged.columns[[1] + list(range(5, scar_merged.shape[1]))]]


# ##### Cluster 2 - Auto Garage

# In[66]:


scar_merged.loc[scar_merged['Cluster Labels'] == 1, scar_merged.columns[[1] + list(range(5, scar_merged.shape[1]))]]


# ##### Cluster 3 - Trail

# In[67]:


scar_merged.loc[scar_merged['Cluster Labels'] == 2, scar_merged.columns[[1] + list(range(5, scar_merged.shape[1]))]]


# ##### Cluster 4 - Coffee Shop

# In[68]:


scar_merged.loc[scar_merged['Cluster Labels'] == 3, scar_merged.columns[[1] + list(range(5, scar_merged.shape[1]))]]


# ##### Cluster 5 - Home Service

# In[69]:


scar_merged.loc[scar_merged['Cluster Labels'] == 4, scar_merged.columns[[1] + list(range(5, scar_merged.shape[1]))]]


# In[ ]:





# ### Amenities Data - New York City

# In[70]:


#### Use the getNearbyVenues function to repeat the same process to all the neighborhoods in Manhattan
manhattan_venues = getNearbyVenues(names=manhattan_data['Neighborhood'],
                                   latitudes=manhattan_data['Latitude'],
                                   longitudes=manhattan_data['Longitude']
                                  )


# In[71]:


#check the size of the resulting dataframe
print(manhattan_venues.shape)
manhattan_venues.head(5)


# In[72]:


#How many venues for each neighborhood
manhattan_venues.groupby('Neighborhood').count()


# In[73]:


#How many unique categories are curated
print('There are {} uniques categories.'.format(len(manhattan_venues['Venue Category'].unique())))


# #### Analyze Each Neighbhorhood

# In[74]:


# one hot encoding
manhattan_onehot = pd.get_dummies(manhattan_venues[['Venue Category']], prefix="", prefix_sep="")

# add neighborhood column back to dataframe
manhattan_onehot['Neighborhood'] = manhattan_venues['Neighborhood'] 

# move neighborhood column to the first column
fixed_columns = [manhattan_onehot.columns[-1]] + list(manhattan_onehot.columns[:-1])
manhattan_onehot = manhattan_onehot[fixed_columns]

manhattan_onehot.head(5)


# In[75]:


#Examine new dataframe size
manhattan_onehot.shape


# In[76]:


#group rows by neighborhood and by taking the mean of the frequency of occurrence of each category
manhattan_grouped = manhattan_onehot.groupby('Neighborhood').mean().reset_index()
manhattan_grouped


# In[77]:


#check new dataframe size
manhattan_grouped.shape


# In[78]:


#print the neighborhoods by their 5 most common values
num_top_venues = 5

for hood in manhattan_grouped['Neighborhood']:
    print("----"+hood+"----")
    temp = manhattan_grouped[manhattan_grouped['Neighborhood'] == hood].T.reset_index()
    temp.columns = ['venue','freq']
    temp = temp.iloc[1:]
    temp['freq'] = temp['freq'].astype(float)
    temp = temp.round({'freq': 2})
    print(temp.sort_values('freq', ascending=False).reset_index(drop=True).head(num_top_venues))
    print('\n')


# In[79]:


# Use return_most_common_venues function and create a new dataframe
num_top_venues = 10

indicators = ['st', 'nd', 'rd']

# create columns according to number of top venues
columns = ['Neighborhood']
for ind in np.arange(num_top_venues):
    try:
        columns.append('{}{} Most Common Venue'.format(ind+1, indicators[ind]))
    except:
        columns.append('{}th Most Common Venue'.format(ind+1))

# create a new dataframe
MANneighborhoods_venues_sorted = pd.DataFrame(columns=columns)
MANneighborhoods_venues_sorted['Neighborhood'] = manhattan_grouped['Neighborhood']

for ind in np.arange(manhattan_grouped.shape[0]):
    MANneighborhoods_venues_sorted.iloc[ind, 1:] = return_most_common_venues(manhattan_grouped.iloc[ind, :], num_top_venues)

MANneighborhoods_venues_sorted.head(5)


# #### Cluster Neighborhoods

# In[84]:


#run kmeans to cluster the neighbhorhoods
# set number of clusters
kclusters = 5

manhattan_grouped_clustering = manhattan_grouped.drop('Neighborhood', 1)

# run k-means clustering
kmeans = KMeans(n_clusters=kclusters, random_state=0).fit(manhattan_grouped_clustering)

# check cluster labels generated for each row in the dataframe
kmeans.labels_[0:10] 


# In[86]:


# create a new dataframe that includes the cluster as well as the top 10 venues for each neighborhood.
# add clustering labels
#MANneighborhoods_venues_sorted.insert(0, 'Cluster Labels', kmeans.labels_)

manhattan_merged = manhattan_data

# merge toronto_grouped with toronto_data to add latitude/longitude for each neighborhood
manhattan_merged = manhattan_merged.join(MANneighborhoods_venues_sorted.set_index('Neighborhood'), on='Neighborhood', how = 'right')

manhattan_merged.head() # check the last columns!


# In[88]:


#visualize the resulting clusters
# create map
map_clusters = folium.Map(location=[MANlatitude, MANlongitude], zoom_start=11)

# set color scheme for the clusters
x = np.arange(kclusters)
ys = [i + x + (i*x)**2 for i in range(kclusters)]
colors_array = cm.rainbow(np.linspace(0, 1, len(ys)))
rainbow = [colors.rgb2hex(i) for i in colors_array]

# add markers to the map
markers_colors = []
for lat, lon, poi, cluster in zip(manhattan_merged['Latitude'], manhattan_merged['Longitude'], manhattan_merged['Neighborhood'], manhattan_merged['Cluster Labels']):
    label = folium.Popup(str(poi) + ' Cluster ' + str(cluster), parse_html=True)
    folium.CircleMarker(
        [lat, lon],
        radius=5,
        popup=label,
        color=rainbow[cluster-1],
        fill=True,
        fill_color=rainbow[cluster-1],
        fill_opacity=0.7).add_to(map_clusters)
       
map_clusters


# ##### Cluster 1 - Restaurants

# In[89]:


manhattan_merged.loc[manhattan_merged['Cluster Labels'] == 0, manhattan_merged.columns[[1] + list(range(5, manhattan_merged.shape[1]))]]


# ###### Cluster 2 - Parks and Restaurants

# In[90]:


manhattan_merged.loc[manhattan_merged['Cluster Labels'] == 1, manhattan_merged.columns[[1] + list(range(5, manhattan_merged.shape[1]))]]


# ##### Cluster 3 - Gym / Fitness

# In[91]:


manhattan_merged.loc[manhattan_merged['Cluster Labels'] == 2, manhattan_merged.columns[[1] + list(range(5, manhattan_merged.shape[1]))]]


# ##### Cluster 4 - Theater

# In[92]:


manhattan_merged.loc[manhattan_merged['Cluster Labels'] == 3, manhattan_merged.columns[[1] + list(range(5, manhattan_merged.shape[1]))]]


# ##### Cluster 5

# In[93]:


manhattan_merged.loc[manhattan_merged['Cluster Labels'] == 4, manhattan_merged.columns[[1] + list(range(5, manhattan_merged.shape[1]))]]


# In[ ]:




