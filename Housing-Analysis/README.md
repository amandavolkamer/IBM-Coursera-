# House Sales

Analyze and predict housing prices using features such as square footage, number of bedrooms, number of floors, and more.

## 📄 Project Overview

This project was completed as part of the IBM Data Science Professional Certificate on Coursera.  
The goal was to apply data wrangling, exploratory data analysis, and machine learning techniques to predict house prices based on various property features.

- **Dataset**: House sales in King County, USA (including Seattle) for homes sold between May 2014 and May 2015.
- **Tech Stack**: Python, Pandas, Seaborn, Scikit-learn

## 🔧 Skills Demonstrated

- Data Wrangling
- Exploratory Data Analysis (EDA)
- Data Visualization
- Linear Regression Modeling
- Model Evaluation
- Ridge Regression
- Pipeline Construction
- Polynomial Transformation

## 📁 Files

- `House_Sales.ipynb`: Jupyter Notebook containing full analysis, visualizations, and modeling
- Dataset: House Sales data (external)

## 🏠 Dataset Features

- `id`: Unique identifier for the house
- `date`: Date the house was sold
- `price`: Target variable - Sale price of the house
- `bedrooms`, `bathrooms`: Number of rooms
- `sqft_living`, `sqft_lot`: Square footage of living area and lot
- `floors`, `waterfront`, `view`, `condition`, `grade`
- `sqft_above`, `sqft_basement`
- `yr_built`, `yr_renovated`
- `zipcode`, `lat`, `long`
- `sqft_living15`, `sqft_lot15`: Living area and lot size in 2015

## 📚 Tasks Completed

1. **Data Types**: Displayed data types for each column.
   - ![Data Types Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/350388b0e3a0e8163c5641f92fb85028d69c715f/Housing-Analysis/Images/Data%20Types%20Screenshot.png)
2. **Data Cleaning**: Dropped unnecessary columns and summarized dataset.
   - ![Data Cleaning Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/350388b0e3a0e8163c5641f92fb85028d69c715f/Housing-Analysis/Images/Data%20Cleaning%20Screenshot.png)
3. **Floor Value Analysis**: Counted unique floor values.
   - ![Floor Value Analysis Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/350388b0e3a0e8163c5641f92fb85028d69c715f/Housing-Analysis/Images/Floor%20Value%20Analysis%20Screenshot.png)
4. **Outlier Detection**: Created boxplots for waterfront property prices.
   - ![Boxplot Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/350388b0e3a0e8163c5641f92fb85028d69c715f/Housing-Analysis/Images/Boxplot%20Screenshot.png)
5. **Feature Correlation**: Visualized correlation between `sqft_above` and `price`.
   - ![Correlation Plot Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/350388b0e3a0e8163c5641f92fb85028d69c715f/Housing-Analysis/Images/Correlation%20Plot%20Screenshot.png)
6. **Simple Linear Regression**: Predicted `price` using `sqft_living` and calculated R².
   - ![Simple Linear Regression Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/350388b0e3a0e8163c5641f92fb85028d69c715f/Housing-Analysis/Images/Simple%20lr%20Screenshot.png)
7. **Multiple Linear Regression**: Predicted `price` using multiple features.
   - ![Multiple Linear Regression Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/350388b0e3a0e8163c5641f92fb85028d69c715f/Housing-Analysis/Images/Multiple%20lr%20Screenshot.png)
8. **Pipeline Construction**: Built data processing and modeling pipeline.
   - ![Pipeline Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/350388b0e3a0e8163c5641f92fb85028d69c715f/Housing-Analysis/Images/Pipeline%20Screenshot.png)
9. **Ridge Regression**: Applied Ridge regression (α = 0.1) and evaluated model.
   - ![Ridge Regression Screentshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/350388b0e3a0e8163c5641f92fb85028d69c715f/Housing-Analysis/Images/Ridge%20Regression%20Screenshot.png)
10. **Polynomial Features**: Performed 2nd order polynomial transform and applied Ridge regression.
    - ![Polynomial Regression Screenshot](https://github.com/amandavolkamer/IBM-Data-Science-Coursera-Projects/blob/350388b0e3a0e8163c5641f92fb85028d69c715f/Housing-Analysis/Images/Polynomial%20Regression%20Screenshot.png)

## 🖼️ Visuals

This project includes:
- Data Type Tables
- Statistical Summaries
- Value Count DataFrames
- Boxplots for Price Outliers
- Regression Plots
- R² Scores for model evaluations

## 📢 Note

> _This project was originally completed in 2020. Some rendering issues in GitHub's notebook viewer may occur due to older file formats or widget libraries._
