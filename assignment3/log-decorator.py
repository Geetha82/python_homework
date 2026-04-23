

import logging
from functools import wraps

# Task 1: Writing and Testing a Decorator

# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

#Task1 -step 2

# Declare decorator(logger_decorator) to log function name (func.__name__)
def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # formatt positional parameters 
        pos_parameters = list(args) if args else "none"

        # formatt keyword parameters
        key_parameters = kwargs if kwargs else "none"

        # call the function for return value
        result = func(*args, **kwargs)

        # To write a log record:
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_parameters}")
        logger.log(logging.INFO, f"keyword parameters: {key_parameters}")
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper

#Task1 -step 3
# Declare a function that takes no parameters and returns nothing
@logger_decorator
def hello():
    print("Hello, World")

#Task1 -step 4
# Declare a function that takes a variable number of positional arguments and returns True
@logger_decorator
def check_position(*args):
    return True


#Task1 -step 5
# Declare a function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator
@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

#Task1 -step 6
#  mainline code
if __name__ == "__main__":
    hello()
    check_position(1, "Apple", 3)
    return_decorator(user="admin", level='high')

    print("Please check ./decorator.log for the results.")
