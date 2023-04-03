#Written by Shiven Desai
def main():
    # Strings to tokenize
    str1 = 'one two three four'
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'

    # Display the tokens in each string.
    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')

def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for item in tokens:
        print(f'Token: {item}')

# Execute the main function.
if __name__ == '__main__':
    main()
