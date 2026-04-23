import pandas as pd

# Task 1 - Create a DataFrame from a dictionary
# Create dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Convert the dictionary into a DataFrame using Pandas.
task1_data_frame= pd.DataFrame(data)

# Print the DataFrame to verify its creation.
print(task1_data_frame)


# Task1 - Add a new column
# Make a copy of the dataFrame
task1_with_salary = task1_data_frame.copy()

# Add a column called Salary
task1_with_salary['Salary'] = [70000, 80000, 90000]

# Print the new DataFrame
print(task1_with_salary)

# Task1 - Modify an existing column
# Make a copy of task1_with_salary in a variable named task1_older
task1_older = task1_with_salary.copy()

# Increment the Age column by 1 for each entry
task1_older['Age'] = task1_older['Age'] + 1

# Print the modified DataFrame
print(task1_older)

# Task1 - Save the DataFrame as a CSV file
# Save the task1_older DataFrame to a file named employees.csv
task1_older.to_csv('employees.csv', index= False)

# Look at the contents of the CSV file 
print("CSV file created!")


# Task 2: Loading Data from CSV and JSON
# Task 2: Read data from a CSV file
# # Load the CSV file from Task 1 into a new DataFrame saved to a variable task2_employees
task2_employees  = pd.read_csv('employees.csv')

# Print it and run the tests to verify the contents
print(task2_employees)

# Task 2: Read data from a JSON file

# Create a JSON file (additional_employees.json). 
# # json
# [
#     {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
#     {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
# ]
# Load this JSON file into a new DataFrame and assign it to the variable json_employees
# Change this line in assignment4.py
#json_employees = pd.read_json('assignment4/additional_employees.json')
json_employees = pd.read_json('additional_employees.json')

# Print the DataFrame to verify it loaded correctly and run the tests
print(json_employees)

# Task 2: Combine DataFrames
# Combine the data 'assignment4/additional_employees.json'  and task2_employees, 
# save it as more_employees
more_employees = pd.concat([task2_employees, json_employees], ignore_index= True)

# Print the combined Dataframe and run the tests
print(more_employees)

# Task 3: Data Inspection - Using Head, Tail, and Info Methods
# Task 3:Use the head() 

# Assign the first three rows of the more_employees DataFrame to the variable first_three
first_three = more_employees.head(3)

# Print the variable
print(first_three)

# Task 3: Use the tail() method

# Assign the last two rows of the more_employees DataFrame to the variable last_two
last_two = more_employees.tail(2)

# Print the variable
print(last_two)

# Task 3: Get the shape of a Dataframe

# Assign the shape of the more_employees DataFrame to the variable employee_shape
employee_shape = more_employees.shape

# Print the variable
print(employee_shape)

# Task 3: Use the info() method

# Print a concise summary 
more_employees.info()


# Task 4: Data Cleaning

# Task 4: Create a DataFrame from dirty_data.csv

# Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data
dirty_data = pd.read_csv('dirty_data.csv')

# Print dirty_data
print(dirty_data)

# Create a copy of the dirty data
clean_data = dirty_data.copy()

# Task 4: Remove duplicate rows and print
clean_data = clean_data.drop_duplicates()
print(clean_data)

# Task 4: Convert Age to numeric
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

# handle missing values and print
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age']).mean()
print(clean_data)

# Task 4 - Convert Salary to numeric, replace known placeholders (unknown, n/a) with NaN and print
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], pd.NA) 
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors= 'coerce')
print(clean_data)


# Task 4 - Fill missing numeric values
# Fill Age which the mean
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())

# Salary with the median
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())

print(clean_data)


# Task 4 - Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')

clean_data['Hire Date'] = clean_data['Hire Date'].fillna(method='ffill')
print(clean_data)

# Task 4 - Strip extra whitespace and standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

print(clean_data)



























