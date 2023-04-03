#Written by Shiven Desai
# This program demonstrates several string testing methods.
def main():
    # Get a string from the user.
    user_string = input('Enter a string: ')
    print('This is what I found about that string:')
    # Test the string.
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.isdigit():
        print('The string contains only digits.')
    if user_string.isalpha():
        print('The string contains only alphabetic characters.')
    if user_string.isspace():
        print('The string contains only whitespace characters.')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase.')

# The get_login_name function accepts a first name, last name, and ID number as arguments.
# It returns a system login name.
def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name.
    # If the name is less than 3 characters, the slice will return the entire first name.
    set1 = first[0:3]

# Call the main function if this file is executed.
if __name__ == '__main__':
    main()
