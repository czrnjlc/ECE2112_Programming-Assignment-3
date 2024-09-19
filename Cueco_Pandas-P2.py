#---------------------------------------------------------------------
# Course: ECE 2112
# Title: Programming Assignment 3

# Name: Czarina Julia C. Cueco
# Year & Section: 2ECEB
#---------------------------------------------------------------------

# Importing the pandas library to work with data
import pandas as pd

# Reading the 'cars.csv' file into a DataFrame and storing it in variable 'x'
x = pd.read_csv('cars.csv')

# Displaying the contents of the DataFrame 'x'
x

# Select the first 5 rows of the DataFrame 'x'
first_five_rows = x.head()

# Use iloc to select odd-numbered columns (1st, 3rd, 5th, etc.)
# Note: In Python, column indexing starts from 0, so we select even indices
odd_columns = first_five_rows.iloc[:, [i for i in range(first_five_rows.shape[1]) if i % 2 == 0]]

# Display the resulting DataFrame containing the selected odd columns
odd_columns

# Filter the DataFrame 'x' to select rows where the 'Model' column is equal to 'Mazda RX4'
x.loc[x['Model']=='Mazda RX4']

# Filter the DataFrame 'x' to select rows where the 'Model' column is equal to 'Camaro Z28'
# and return only the 'Model' and 'cyl' columns for those rows
x.loc[x['Model']=='Camaro Z28',['Model','cyl']]

# Define a list of car models to filter
car_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']

# Use the loc method to select rows where the 'Model' column matches any of the car models in the list
# and retrieve the 'Model', 'cyl', and 'gear' columns for those rows
x.loc[x['Model'].isin(car_models), ['Model', 'cyl', 'gear']]

