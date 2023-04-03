#Written by Shiven Desai
def total():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sum = 0
    for value in numbers:
        sum += value  # total the numbers in the list
    average = sum / len(numbers)  # the lens functions returns the number of items in the list
    print('The total is:', sum, 'The average is:', average)

    # write the numbers list to a text file
    with open('numbers.txt', 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

total()
