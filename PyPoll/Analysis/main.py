#import dependencies
import csv
import os

#declare a variable and read the csv file
csv_path = "../Resources/election_data.csv"

#initialize a total vote counter
vote_total = 0

#create a dictionary for votes
number_votes = {}

#declare variables to keep track of the winner, the vote count and the percentage of vote
Winner = ""
vote_count = 0
vote_percentage = 0

#open the csv file  and read the file
with open(csv_path, encoding='utf-8') as election_dataset:
    csvreader = csv.reader(csv_path, delimiter=",")
    
    #count the rows in the csv file
    for row in csvreader:
        vote_total += 1
        #get the candidate's name
        candidates = row["Candidate"]
        #add a vote to candidate's count
        number_votes[candidates] =number_votes[candidates]+ 1

        #this should get the winner
    for candidate in number_votes:
        votes = number_votes.get(candidate)
        vote_percentage = float(votes) / float(vote_total) * 100

        #determine the winner
        if (votes > vote_count):
            vote_count = votes
            Winner = candidate

        #print each candidate's vote count and percentage and the election results
        print(f"Election Results")
        print(f"---------------------------\n")
        print(f"Total Votes: {vote_total}\n")
        print(f"-----------------------------\n")
        summary = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(summary, end="")
        print(f"-----------------------------------\n")
        print(f"Winner: {Winner}\n")
        print(f"----------------------------------\n")
               
# I have tried everything and even submitting late but can't get anything to work.
  




