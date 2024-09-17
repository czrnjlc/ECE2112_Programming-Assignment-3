# Importing the pandas library to work with data
import pandas as pd

# Reading the 'cars.csv' file into a DataFrame and storing it in variable 'x'
x = pd.read_csv('cars.csv')

# Displaying the contents of the DataFrame 'x'
x

# Display the first five rows of the DataFrame 'x'
x.head()

# Display the last five rows of the DataFrame 'x'
x.tail()