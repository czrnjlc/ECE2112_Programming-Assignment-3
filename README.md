# Programming Assignment 3: Python Data Analysis (PANDAS)
## Overview
This repository contains Python scripts that utilize the Pandas library to perform data manipulation tasks on a dataset of cars. The dataset is loaded from a CSV file and various operations such as subsetting, slicing, and filtering are performed to extract meaningful information.

## Files
**Cueco_Pandas-P1.py**: This script performs basic operations to load a CSV file into a DataFrame and display the first and last five rows.

**Cueco_Pandas-P2.py**: This script includes operations to:
* Display the first five rows with odd-numbered columns.
* Extract the row corresponding to the 'Mazda RX4' model.
* Find the number of cylinders for the 'Camaro Z28' model.
* Determine the number of cylinders and gear type for specific car models.

**Cueco_PA_3**: Jupyter Notebook script for data analysis, which includes Problem 1 and 2.

**cars.csv**: CSV file containing dataset of cars.

### Prerequisites
* Python 3.x
* Pandas library

## Explanation of Scripts
### Problem 1: Surname_Pandas-P1.py
**Objective:**
* To load a CSV file into a Pandas DataFrame and display the first and last five rows of the data.

### Code:
#### 1. Importing the pandas library
Imports the Pandas library, which is used for data manipulation and analysis.
```python
import pandas as pd
```
#### 2. Reading the 'cars.csv' file into a DataFrame
Reads the CSV file named cars.csv into a DataFrame called x. This DataFrame will now contain the data from the CSV file.
```python
x = pd.read_csv('cars.csv')
```
#### 3. Display the first five rows of the DataFrame
Displays the first five rows of the DataFrame x. This helps to quickly inspect the beginning of the dataset.
```python
x.head()
```
#### 4. Display the last five rows of the DataFrame
Displays the last five rows of the DataFrame x. This is useful for checking the end of the dataset and ensuring that the file was read correctly.
```python
x.tail()
```
### Problem 2: Surname_Pandas-P2.py
**Objective:**
To perform various operations on the DataFrame loaded from the CSV file, including subsetting, slicing, and filtering to extract specific information.

### Code:
#### 1. Importing Pandas Library
Imports the Pandas library.
```python
import pandas as pd
```
#### 2. Loading the Data
Reads the CSV file into a DataFrame called x.
```python
x = pd.read_csv('cars.csv')
```
#### 3. Displaying First Five Rows with Odd-Numbered Columns
  * `x.head(10)` : Retrieves the first 10 rows of the DataFrame.
  * `.iloc[1::2]` : Uses integer-location based indexing to select every other column, starting from the first column (0, 2, 4, ...).
```python
first_five_odd_rows = x.head(10).iloc[1::2]
first_five_odd_rows
```
#### 4. Displaying the Row for 'Mazda RX4'
  * `x['Model'] == 'Mazda RX4'` : Creates a boolean mask where the 'Model' column matches 'Mazda RX4'.
  * `x.loc[...]` : Filters the DataFrame to include only rows where the condition is True.
```python
x.loc[x['Model']=='Mazda RX4']
```
#### 5. Finding Number of Cylinders for 'Camaro Z28'
  * `x['Model'] == 'Camaro Z28'` : Creates a boolean mask for 'Camaro Z28'.
  * `x.loc[... , 'cyl']` : Retrieves the 'cyl' column for rows matching 'Camaro Z28'.
```python
x.loc[x['Model']=='Camaro Z28',['Model','cyl']]
```
#### 6. Number of Cylinders and Gear Type for Specific Car Models
  * `car_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']` : Defines a list of car models to filter.
  * `x['Model'].isin(car_models)` : Creates a boolean mask to filter rows where 'Model' is in the car_models list.
  * `x.loc[..., ['Model', 'cyl', 'gear']]` : Selects the 'Model', 'cyl', and 'gear' columns.
```python
car_models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
x.loc[x['Model'].isin(car_models), ['Model','cyl','gear']]
```

### Notes
* Ensure that the cars.csv file is in the same directory as the script or provide the full path to the file.
* Adjust the file names (Surname_Pandas-P1.py and Surname_Pandas-P2.py) as needed to match your surname.

### Profile
**Author:** Czarina Julia C. Cueco

*I am currently an engineering student from University of Santo Tomas, working with data analysis using Pandas in Python. This repository is part of a programming assignment, where I explore how to load and manipulate data using the Pandas library.*

### Edit History
| Date           | Description                                                                              |
|----------------|------------------------------------------------------------------------------------------|
| 2024-09-16     | Initial Creation                                                                         |
| 2024-09-16     | Updated README fixed grammatical errors                                                  |
| 2024-09-16     | Uploaded a ipynb file and Updated README improved syntax                                 |
| 2024-09-17     | Uploaded .py and csv files and Updated README improved syntax and added additional info  |
