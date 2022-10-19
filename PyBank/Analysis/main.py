#Modules needed
import csv
import os

#read the csv file budget_data.csv
csv_path = "../Resources/budget_data.csv"

#use for loop to iterate the CSV file and increment 
#set variables
Total_PL = 0  #the net total amount  FYI PL is Profit/Losses
PL_change = 0  #the Profit/Losses over the entire period
previous_PL = 0  #the previous profit/losses
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999]
average_change = 0
total_months = 0
time_of_change = []
PL_change_list = []

#Read the CSV file 
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None) #excludes the header

    
    for row in csvreader:
        Total_PL = Total_PL + int(row[1]) # calculates the total amount of profits/losses

        #the average change over the entire period
        PL_change = int(row[1]) - previous_PL
        previous_PL = int(row[1])
        PL_change_list = PL_change_list + [PL_change]
        time_of_change = time_of_change + [row[0]]

        #get the greatest increase in profits and date 
        if (PL_change > greatest_increase[1]):
            greatest_increase[1] = PL_change
            greatest_increase[0] = row[0]
        
        #get the greatest degrease in profits and date
        if (PL_change < greatest_decrease[1]):
            greatest_decrease[1] = PL_change
            greatest_decrease[0] = row[0]

        total_months += 1 #counts the number of rows
    
    #calculate the average Profit/Losses
    average_change = sum(PL_change_list)/len(PL_change_list)  

    #output  
    print(f"Total Months : {total_months}" )    
    print(f"Total : {Total_PL}" )
    print(f"Average Change : {average_change}" )
    print(f"Greastest Increase in Profits : {greatest_increase[0]}, (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits : {greatest_decrease[0]}, (${greatest_decrease[1]})")
