"""
Create a function called process_data that:

1. Takes a string input representing potential data
2. Tries to convert it to an integer, then calculates 100 divided 
   by that integer
3. /Returns the result
4. Handles at least 3 possible exceptions: 
  -ValueError if the input cannot be converted to an integer 
   (print "Input must be a number!")
  -ZeroDivisionError if the input is 0 (print "Cannot divide by zero!")
  -Any other exception with a generic handler 
   (print "An unexpected error occurred!")
"""
def process_data(input_string):
    try:
        # Try to convert the input string to an integer
        converted_input = int(input_string)
        
        # Calculate 100 divided by the input value
        result = 100 / converted_input 
        
        # Return the result
        return result

    except ValueError:
        # Handle the case where input cannot be converted to an integer
        print("Input must be a number!")
    except ZeroDivisionError:
        # Handle the case where input is zero
        print("Cannot divide by zero!")
    except:
        # Handle any other unexpected exceptions
        print("An unexpected error occurred!")
    return None


process_data("a")
process_data(0)
