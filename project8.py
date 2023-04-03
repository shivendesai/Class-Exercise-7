#Written by Shiven Desai
def main():
    # create a list to store rainfall for each month
    rainfall = []
    
    # ask user to enter rainfall for each month
    for i in range(12):
        month_rainfall = float(input(f"Enter rainfall for month {i+1}: "))
        rainfall.append(month_rainfall)
        
    # calculate total rainfall for the year
    total_rainfall = sum(rainfall)
    
    # calculate average monthly rainfall
    avg_rainfall = total_rainfall / 12
    
    # find month with highest and lowest rainfall
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_month = rainfall.index(max_rainfall) + 1
    min_month = rainfall.index(min_rainfall) + 1
    
    # output results to console
    print(f"Total rainfall for the year: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {avg_rainfall:.2f}")
    print(f"Month with highest rainfall: {max_month} ({max_rainfall:.2f} inches)")
    print(f"Month with lowest rainfall: {min_month} ({min_rainfall:.2f} inches)")
    
    # output results to text file
    with open("rainfall_results.txt", "w") as file:
        file.write(f"Total rainfall for the year: {total_rainfall:.2f}\n")
        file.write(f"Average monthly rainfall: {avg_rainfall:.2f}\n")
        file.write(f"Month with highest rainfall: {max_month} ({max_rainfall:.2f} inches)\n")
        file.write(f"Month with lowest rainfall: {min_month} ({min_rainfall:.2f} inches)\n")

# call the main function
main()
