# Task 3: List Comprehensions Practice
import csv

# Task 3: step 1

# file path related to the assignment3 folder
csv_file_path = '../csv/employees.csv'

# read the contents of the filepath into a list of lists using the csv module
with open(csv_file_path, mode='r' , newline='') as file:
    reader = csv.reader(file)
    employee_data = list(reader)

# Task 3: step 2

# create a list of the employee names, first_name + space + last_name. 
# The list comprehension should iterate through the items in the list read from the csv file.
# Print the resulting list. Skip the item created for the heading of the csv file.

full_name = [f"{row[1]} {row[2]}" for row in employee_data[1:]]
print("Full Name: ")
print(full_name)

# Task 3: step 3
# filter list to include only those names that contain the letter "e"
names_with_e = [name for name in full_name if 'e' in name.lower()]

# Print this list
print("\n Names with letter 'e': ")
print(names_with_e)

