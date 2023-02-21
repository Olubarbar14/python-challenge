#Import modules
import csv
import os

#read the csv file budget_data.csv
csv_path = "../Resources/budget_data.csv"

 
#set variables
months = []
profit_loss_changes = []

count_of_months = 0
total_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0


# Open and read csv
with open(csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
    
     # This prints -->> Header: Date, Profit/Losses
    print(f"Header: {csv_header}")
   
             
    #use for loop to iterate the CSV file and increment
    for row in csv_reader:

        # Count of months
        count_of_months += 1

        # get the net profits over the entire period
        current_month_profit_loss = int(row[1])
        total_profit_loss += current_month_profit_loss

        if (count_of_months == 1):
            # this will make the previous month's profit loss to become the current month's profit loss
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Calculate the change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Add each month to the months array
            months.append(row[0])

            # Add the profit losses to the profit loss change array
            profit_loss_changes.append(profit_loss_change)

            # This changes the previous month to become the current month and the loop through again
            previous_month_profit_loss = current_month_profit_loss

    #Calculate the sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_of_months - 1), 2)

    # Get the highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Get the date and amount of the greatest increase and decrease in profits
    greatest_increase = months[highest_month_index]
    greatest_decrease = months[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_of_months}")
print(f"Total:  ${total_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {greatest_increase} (${highest_change})")
print(f"Greatest Decrease in Losses:  {greatest_decrease} (${lowest_change})")


# -->>  Export a text file with the results
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_of_months}\n")
    outfile.write(f"Total:  ${total_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {greatest_increase} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {greatest_decrease} (${lowest_change})\n")
