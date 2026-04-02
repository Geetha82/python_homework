# Task 1: Hello
def hello():
    return "Hello!"
# Manual Test(debugging)
print(hello())


# Task 2: Greet with a Formatted String
def greet(name):
    return f"Hello, {name}!"
# Manual Test(debugging)
print(greet("Geetha"))


#Task 3: calculator
def calc(number1, number2, operation="multiply"):
    #Multiple Error Handling
    try:
        match operation:
            case "add":
                return number1 + number2                        
            case "subtract":
                return number1 - number2
            case "multiply":
                return number1 * number2
            case "divide":
                return number1 / number2        
            case "modulo":
                return number1 % number2
            case "int_divide":
                return number1 // number2
            case "power":
                return number1 ** number2       
            case _:
                return "Unknown operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    # More error handling
    except TypeError:
        return "You can't multiply those values!"

 # Manual Test(debugging)  
print(calc(10, 5)) # Should return: 50
print(calc(10, 5, "add")) # Should return: 15
print(calc(10, 5, "subtract")) # Should return: 5
print(calc(10, 5, "divide")) # Should return: 2.0
print(calc(10, 5, "modulo")) # Should return: 0
print(calc(10, 5, "int_divide")) # Should return: 2
print(calc(10, 5, "power")) # Should return: 100

# Manual Test for Zero Division Error
print(calc(10, 0, "divide")) # Should return: You can't divide by 0!
# Manual Test for Type Error
print(calc("apple", "orange", "multiply")) # Should return: You can't multiply those values!


# Task 4: Data Type Conversion
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

# Manual Test(debugging)
print(data_type_conversion("12.5", "float"))    # Should return 12.5
print(data_type_conversion("abc", "int")) 


# Task 5: Grading System, Using *args
def grade(*args):
    try:
        # calculating the average   
        # Using sum() and len() to calculate the average of the grades      
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
        # Error handling for ZeroDivisionError and TypeError    
    except (ZeroDivisionError, TypeError):
        return "Invalid input. Please provide numeric grades."

# Manual Test(debugging)
print(grade(95, 85, 90))  # return: A
print(grade(85, 75, 80))  # return: B
print(grade(75, 65, 70))  # return: C
print(grade(65, "abc", 60))  # return: "invalid input. Please provide numeric grades."
print(grade())  # return: "invalid input. Please provide numeric grades."  


# Task 6: Use a For Loop with a Range
def repeat(str,count):
    result = ""
    for i in range(count):
        result += str
    return result   

# Manual Test(debugging)
print(repeat("hello", 3))  #return: "hellohellohello    "               


# Task 7: Student Scores, Using **kwargs
def student_scores(student_position,**kwargs):
   if not kwargs:
        return "No student scores provided."
   if student_position == "best":
       return max(kwargs, key=kwargs.get)
   elif student_position == "mean":
       return sum(kwargs.values()) / len(kwargs)        
   
# Manual Test(debugging)
# for best score
print(student_scores("best", AAA=85, BBB=90, CCC=80))  # returns(for best) the name(BBB) of the student with the highest score
# for mean score
print(student_scores("mean", AAA=85, BBB=90, CCC=80))  # returns (for mean) the average score(85.0).

# Task 8: Titleize, with String and List Operations
def titleize(title_str):
    title_words = title_str.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    formatted_words = []

    for i, word in enumerate(title_words):
        # Rule 1 & 2: First and last words always capitalized
        if i == 0 or i == len(title_words) - 1:
            formatted_words.append(word.capitalize())
        # Rule 3: Capitalize unless it's a "little word"
        elif word.lower() in little_words:
            formatted_words.append(word.lower())
        else:
            formatted_words.append(word.capitalize())

    return " ".join(formatted_words)

        
# Manual Test(debugging)
print(titleize("a tale of two cities"))
print(titleize("the catcher in the rye"))

# Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    result = ""
    for letter in secret:
                # Check if the letter from the secret is in the guess string
        if letter in guess:
            result += letter
        else:
            # If the letter is not in the guess, adds an underscore to the result string
            result += "_"
    return result

# Manual Test(debugging)
print(hangman("apple", "ale"))  # returns:   "a__le"
print(hangman("apple", "xyz"))    # returns: "______"


# Task 10: Fibonacci Sequence, with a While Loop
def pig_latin(sentence):
    vowels= "aeiou"
    words = sentence.split()
    result = []
    for word in words:
        word = word.lower()
        vowels = "aeiou"
        # (1) If starts with a vowel (aeiou), "ay" is tacked onto the end
        if word[0] in vowels:
            result.append(word + "ay")      
        else:
        # (3)"qu": is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
            if word.startswith("qu"):
                cutoff = 2
            else:
                # (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them. 
                cutoff = 0
                cutoff = 0
                for i, char in enumerate(word):
                    if char in vowels:
                        cutoff = i
                        break
            
            # Move consonants to end and add "ay"
            new_word = word[cutoff:] + word[:cutoff] + "ay"
            result.append(new_word)
    return " ".join(result) 

# Manual Test(debugging)
print(pig_latin("apple"))        # appleay (Rule 1)
print(pig_latin("smile"))        # ilesmay (Rule 2)
print(pig_latin("quick check"))  # ickquay eckchay (Rule 3 & 2)

   

