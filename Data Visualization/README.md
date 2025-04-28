# Topic Survey – Visualization

Visualize survey responses about data science topics and create a choropleth map of crime in San Francisco.

## 📄 Project Overview

This project was completed as part of the IBM Data Science Professional Certificate on Coursera.  
The goal was to apply data visualization techniques to summarize survey data and to map crime rates geographically using a choropleth.

- **Datasets**: Data Science Topic Survey results and San Francisco Crime data
- **Tech Stack**: Python, Pandas, Matplotlib, Folium, GeoJSON

## 🔧 Skills Demonstrated

- Data Wrangling
- Data Aggregation
- Bar Chart Visualization
- Choropleth Mapping
- GeoJSON Handling
- Data Normalization and Formatting

## 📁 Files

- `Topic_Survey_Visualization.ipynb`: Jupyter Notebook containing the full analysis, bar chart creation, and choropleth mapping
- Datasets:
  - `Topic_Survey_Data.csv`: The survey results have been saved in a csv file and can be downloaded here: https://cocl.us/datascience_survey_data
  - `SanFrancisco_2016_Crime_Data.csv`: This data can be downloaded here: https://cocl.us/sanfran_crime_dataset
  - `SanFrancisco_GeoJSON.json`:  The JSN file can be downloaded here:  https://cocl.us/sanfran_geojson

## 📚 Tasks Completed

### Part 1: Survey Visualization

1. **Load Survey Data**: Read CSV file into a pandas DataFrame.  
   ![Survey DataFrame Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/4c2e425fb7d87ef92a24e74d1c1bfc58dabfbf04/Data%20Visualization/Images/Load%20Dataframe%20Screenshot%20-%20Part%201.png)

2. **Bar Chart Creation**: Built a Matplotlib bar chart summarizing interest in data science topics.  
   - Custom colors used for different levels of interest.
   - Percentages labeled above each bar.
   ![Survey Bar Chart Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/4c2e425fb7d87ef92a24e74d1c1bfc58dabfbf04/Data%20Visualization/Images/Survey%20Bar%20Chart%20Screenshot%20-%20Part%201.png)

### Part 2: Crime Choropleth Map

3. **Load Crime Data**: Read San Francisco crime dataset and aggregated total crimes by neighborhood.  
   ![Crime Data Aggregation Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/4c2e425fb7d87ef92a24e74d1c1bfc58dabfbf04/Data%20Visualization/Images/Crime%20Data%20Aggregation%20-%20Part%202.png)

4. **Choropleth Map Creation**: Mapped crime counts geographically using Folium and a GeoJSON file.  
   - Centered on San Francisco
   - Zoom level: 12
   - Color scale: `'YlOrRd'`
   ![San Francisco Choropleth Map Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/4c2e425fb7d87ef92a24e74d1c1bfc58dabfbf04/Data%20Visualization/Images/San%20Francisco%20Choropleth%20Map%20Screenshot%20-%20Part%202.png)

## 🖼️ Visuals

This project includes:
- Sorted and Processed Survey DataFrames
- Customized Bar Charts with Interest Percentages
- Aggregated Crime Totals by Neighborhood
- Choropleth Map showing Crime Distribution

## 📢 Note

> _This project was originally completed in 2020. Some rendering issues in GitHub's notebook viewer may occur due to older file formats or widget libraries._
