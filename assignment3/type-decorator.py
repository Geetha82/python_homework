# Task 2: A Decorator that Takes an Argument

# Task 2- step 2
import functools

# Task 2 - step 2
# Declare decorator(type_converter) that has one argument 
def type_converter(type_of_output):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # execute func for the return value
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator

# Task 2 - step 3
# return_int() function no arguments and returns the int 5
# Decorate with type-decorator by passing str as the parameter to type_decorator
@type_converter(str)
def return_int():
    return 5

# Task 2 - step 4
# return_string()function takes no arguments and returns the string - "not a number"
@type_converter(int)
def return_string():
    return ("not a number")

# Task 2 - step 5
# mainline of the program
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__) # This should print "str"
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!") # This is what should happen





