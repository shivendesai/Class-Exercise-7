#Written by Shiven Desai
# The get_login_name function accepts a first name,
# last name, and ID number as arguments. It returns
# a system login name.
def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name.
    # If the name is less than 3 characters, the
    # slice will return the entire first name.
    set1 = first[0:3]

    # Get the first three letters of the last name.
    # If the name is less than 3 characters, the
    # slice will return the entire last name.
    set2 = last[0:3]

    # Get the last three characters of the student ID.
    # If the ID number is less than 3 characters, the
    # slice will return the entire ID number.
    set3 = idnumber[-3:]

    # Put the sets of characters together.
    login_name = set1 + set2 + set3

    # Return the login name.
    return login_name


# The valid_password function accepts a password as
# an argument and returns either true or false to
# indicate whether the password is valid. A valid
# password must be at least 7 characters in length,
# have at least one uppercase letter, one lowercase
# letter, and one digit.
def valid_password(password):
    # Set the Boolean variables to false.
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Begin the validation. Start by testing the
    # password's length.
    if len(password) >= 7:
        correct_length = True

    # Test each character and set the
    # appropriate flag when a required
    # character is found.
    for ch in password:
        if ch.isupper():
            has_uppercase = True
        if ch.islower():
            has_lowercase = True
        if ch.isdigit():
            has_digit = True

    # Determine whether all of the requirements
    # are met. If they are, set is_valid to true.
    # Otherwise, set is_valid to false.
    if correct_length and has_uppercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    # Return the is_valid variable.
    return is_valid


# This program gets a password from the user and
# validates it.
def main():
    # Get user information
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    id_number = input('Enter your student ID number: ')

    # Generate login name
    login_name = get_login_name(first_name, last_name, id_number)

    # Get a password from the user.
    password = input('Enter your password: ')

    # Validate the password.
    while not valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')

    print("Welcome, {}! Your login name is {}.".format(first_name, login_name))

# Call the main function.
if __name__ == '__main__':
    main()
