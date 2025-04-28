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
  - `Topic_Survey_Data.csv`
  - `SanFrancisco_2016_Crime_Data.csv`
  - `SanFrancisco_GeoJSON.json`

## 📚 Tasks Completed

### Part 1: Survey Visualization

1. **Load Survey Data**: Read CSV file into a pandas DataFrame.  
   ![Survey DataFrame Screenshot](INSERT-LINK-HERE)

2. **Data Processing**: Sorted topics by "Very Interested" responses and calculated percentages.  
   ![Processed Survey Data Screenshot](INSERT-LINK-HERE)

3. **Bar Chart Creation**: Built a Matplotlib bar chart summarizing interest in data science topics.  
   - Custom colors used for different levels of interest.
   - Percentages labeled above each bar.
   ![Survey Bar Chart Screenshot](INSERT-LINK-HERE)

### Part 2: Crime Choropleth Map

4. **Load Crime Data**: Read San Francisco crime dataset and aggregated total crimes by neighborhood.  
   ![Crime Data Aggregation Screenshot](INSERT-LINK-HERE)

5. **Choropleth Map Creation**: Mapped crime counts geographically using Folium and a GeoJSON file.  
   - Centered on San Francisco
   - Zoom level: 12
   - Color scale: `'YlOrRd'`
   ![San Francisco Choropleth Map Screenshot](INSERT-LINK-HERE)

## 🖼️ Visuals

This project includes:
- Sorted and Processed Survey DataFrames
- Customized Bar Charts with Interest Percentages
- Aggregated Crime Totals by Neighborhood
- Choropleth Map showing Crime Distribution

## 📢 Note

> _This project was originally completed in 2020. Some rendering issues in GitHub's notebook viewer may occur due to older file formats or widget libraries._
