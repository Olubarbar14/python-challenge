# Import Modules
#I did not submit this homework because I could not get it to print the 
#exact information like the example homework no matter what I tried.

import os
import csv

#Read the csv file
csv_path = "../Resources/election_data.csv"
               
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)
    

#Declare Variables
    num_votes=0
    total_votes=0
    candidates=[]
    number_won = {}
    percent_won=0
    winner=""
    winner_votes=0
  
#The total number of votes cast
    for row in csv_reader:
        num_votes +=1
    
#get a list of candidates who received votes
#The total number of votes each candidate won
        if row[2] not in candidates:
            candidates.append(row[2])
            number_won[row[2]]=0
        number_won[row[2]]+=1
        

#The percentage of votes each candidate won
for name in number_won:
    votes = number_won[name]
    percentage = votes / num_votes
    percent = percentage * 100

#The winner of the election based on popular vote.
    if votes > winner_votes: 
        winner_votes = votes
        winner = name

#Print to terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {num_votes}")
print(f"-------------------------")
print(f"{name}: {percent:.3f}% ({votes})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

#write to outut file
results_file = os.path.join("Output", "Election_data.txt")
with open(results_file, "w") as outfile:

    outfile.write(f"Election Results\n")
    outfile.write(f"-------------------------\n")
    outfile.write(f"Total Votes: {num_votes}\n")
    outfile.write(f"-------------------------\n")
    outfile.write(f"{name}: {percent:.3f}% ({votes})\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write(f"-------------------------\n")

