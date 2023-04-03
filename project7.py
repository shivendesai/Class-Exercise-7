#Written by Shiven Desai
def main():
    # create a list to store the sales for each day of the week
    sales = []
    
    # loop to get the sales for each day of the week from the user
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        sales_for_day = float(input(f"Enter sales for {day}: "))
        sales.append(sales_for_day)
    
    # calculate the total sales for the week
    total_sales = sum(sales)
    
    # print the total sales to the console and to a text file
    with open('total_sales.txt', 'w') as f:
        f.write(f"Total sales for the week: {total_sales:.2f}\n")
        print(f"Total sales for the week: {total_sales:.2f}")
    
if __name__ == '__main__':
    main()
