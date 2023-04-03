#Written by Shiven Desai
# This program counts the number of times 
# the letter T (uppercase or lowercase) 
# appears in a string.

def main():
    # Create a variable to use to hold the count.
    # The variable must start with 0.
    count = 0
    # Get a string from the user.
    my_string = input('Enter a sentence: ')
    # Count the Ts.
    for ch in my_string:  # Fixed variable name and added colon
        if ch == 'T' or ch == 't':  # Fixed comparison operator and added second condition
            count += 1  # Increment count variable
    # Print the result.
    print (f'The letter T appears {count} times.')  # Fixed string formatting syntax
# Call the main function.
if __name__ == '__main__':
    main()
