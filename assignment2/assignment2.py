

# Task 2: Read a CSV File
import csv
import sys
import traceback
# task 10: Add a line to assignment2.py to import the os module
import os
# Add the line import custom_module
import custom_module
from datetime import datetime


def read_employees():
    # Declare an empty dict and an empty list to store the rows
    result_dict = {}
    rows_list = []
    
    try:
        # Use a with statement so the file gets closed automatically
        # Note: The path is ../csv/employees.csv as requested
        with open('../csv/employees.csv', mode='r') as file:
            reader = csv.reader(file)
            
            for i, row in enumerate(reader):
                if i == 0:
                    # Store the first row (headers) in the dict using the key "fields"
                    result_dict["fields"] = row
                else:
                    # Add all other rows to your rows list
                    rows_list.append(row)
            
            # Add the list of rows (list of lists) to the dict using key "rows"
            result_dict["rows"] = rows_list
            return result_dict

    except Exception as e:
        # Catch exception, print info using traceback, and exit
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        
        print("An exception occurred.")
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        sys.exit(1)

# Global variable to store the returned value
employees = read_employees()
print(employees)


# Task 3: Find the Column Index

# Task 3
def column_index(first_name):
    # Use the index() method of the list class to find the index of the header
    return employees["fields"].index(first_name)

# Call the function for "employee_id" and store it in a global variable
# This must be outside the function so it runs when the module is imported
employee_id_column = column_index("employee_id")


# Task 4: Find the Employee First Name

# function to retrieve the value of first_name from a row as stored in the employees dict
def first_name(row_number):

    # call column_index function to find out what column index
    first_name_col = column_index("first_name")

    # navigate to to the requested row as stored in the employees dict
    row = employees["rows"][row_number]

    # get the value at that index in the row
    name_value = row[first_name_col]

    return name_value


# Task 5: Find the Employee: a Function in a Function

# create employee_find func with integer employee_id as argument
def employee_find(employee_id):

    # create employee_match function referencing employee_is passed to employee_find function
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches=list(filter(employee_match, employees["rows"]))

    # return the rows matching employee_id
    return matches

# Task 6: Find the Employee with a Lambda

def employee_find_2(employee_id):
   
   #  the parameter passed to the lambda (a row), followed by a colon, followed by the expression that gives the result.
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches


# Task 7: Sort the Rows by last_name Using a Lambda

def sort_by_last_name():

    # find "last_name" using column_index
    last_name_index = column_index("last_name")

    # sort rows using lambda as key
    # lamba takes row and returns last_name_index
    employees["rows"].sort (key = lambda row: row[last_name_index])

    # return the sorted list of rows
    return employees["rows"]

#  Call sort_by_last_name function 
sort_by_last_name ()

# print the employees dict, to see it in sorted form
print(employees)


# Task 8: Create a dict for an Employee
def employee_dict(row):

    # get the column headers from employees["fields"]
    fields = employees["fields"]

    # The values in the dict are the corresponding values from the row.
    full_dict = dict(zip(fields, row)) 
  
    # remove  the employee_id in the dict
    if "employee_id" in full_dict:
        del full_dict["employee_id"]

    # Return the resulting dict for the employee.
    return full_dict

# call this function 
test_employee = employee_dict(employees["rows"][0])

# print the result 
print(f"Employee Dict: {test_employee}")


# Task 9: A dict of dicts, for All Employees

# Create a function called all_employees_dict
def all_employees_dict():

    # assign a dict to store the results
    all_employee = {}

    # For each key, the value is the employee dict created for that row. 
    for row in employees["rows"]:

        #Get ID from the original row (index 0)
        emp_id = row[0] 

        # Get the rest of the data from employee_dict (task 8)
        employee_data = employee_dict(row)
        
        # assign the employee data to the key in our result
        all_employee[emp_id] = employee_data
        
    # return the resulting dict of dicts
    return all_employee

# call this function 
result_all_employee = all_employees_dict()

# print the result
print(result_all_employee)


# Task 10: Use the os Module

def get_this_value():

    # returns the value of the environment variable THISVALUE
    return os.getenv('THISVALUE')

# Task 11: Creating Your Own Module

def set_that_secret(new_secret):

    # call custom_module.set_secret()
    custom_module.set_secret(new_secret)

# call set_that_secret, passing the new string
set_that_secret("abcd")

# print out custom_module.secret
print(custom_module.secret)


 # Task 12: Read minutes1.csv and minutes2.csv

# helper function
def read_csv_as_tuples(filepath):

    # open the file in read mode
    with open(filepath, mode='r') as f:

        # read each row of the file as dictionary
        reader = csv.DictReader(f)

        # Convert each row (dict) to a tuple of its values
        rows = [tuple(row.values()) for row in reader]

        # returns a dictionary containing both the headers and the actual data rows
        return {"fields": reader.fieldnames, "rows": rows}

def read_minutes():
    # Pathing: ../csv/ means go "up" one folder then into "csv"
    m1 = read_csv_as_tuples('../csv/minutes1.csv')
    m2 = read_csv_as_tuples('../csv/minutes2.csv')

    # return as single tuple containing both dictionaires: DRY (Don't Repeat Yourself)
    return m1, m2

# call the fuction and store in global variable minutes1 and minutes2
minutes1, minutes2 = read_minutes()

# print the output
print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)


# Task 13: Create minutes_set

def create_minutes_set():

    # create 2 sets from minutes1 and minutes2
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])

    # combine the members of both sets into single set
    combined_result_set = set1 | set2

    return combined_result_set

# call create_minutes_set() and store in minutes_set
minutes_set = create_minutes_set()

print(f"total_entries_unique: {len(minutes_set)}")

# Task 14: Convert to datetime
 
def create_minutes_list():

    # Create a list from the minutes_set. This is just type conversion
    minutes_set_list = list(minutes_set)

    # Use the map() function with lambda to convert each tuple
    # x[0] is name, x[1] is date(str)
    converted_map = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set_list)
    
    # return the resulting list
    return list(converted_map)

# Call the function and Store the return value in the minutes_list global
minutes_list = create_minutes_list()

print("Minutes list with data&time:", minutes_list)

# Task 15: Write Out Sorted List

def write_sorted_list():

    # Sort minutes_list in ascending order of datetime
    minutes_list.sort(key=lambda x: x[1])

    # Call map again to convert the list
    # create a new tuple,  The first element of the tuple is the name (unchanged)
    # The second element of the tuple is the datetime converted back to a string, using datetime.strftime(date, "%B %d, %Y")
    converted_map = map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list)
    converted_list = list(converted_map)
   
    # Open a file called ./minutes.csv,Use a csv.writer to write out the resulting sorted data
    with open('./minutes.csv', mode='w', newline='') as f:
        writer = csv.writer(f)

        # The first row is the the value of fields the from minutes1 dict
        writer.writerow(minutes1['fields'])

        # The subsequent rows is the elements from minutes_list
        writer.writerows(converted_list)

    return converted_list

# call the function
sorted_minutes= write_sorted_list()

# print the result
print("First row written:", sorted_minutes[0] if sorted_minutes else "Empty")





    # The function should return the converted list.















































