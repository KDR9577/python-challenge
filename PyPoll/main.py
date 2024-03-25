# Import modules
import os
import csv

# Add csv file
csvpath = os.path.join("main.py", "Resources.csv")

# Read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

# The total number of votes cast
# def voter_data(poll_data):
#     ballot = str(poll_data[0])
#     county = str(poll_data[1])
#     candidate = str(poll_data[2])

#     total_votes = ballot.sum
#     print(total_votes)
# A complete list of candidates who received votes
    
# The percentage of votes each candidate won
    
# The total number of votes each candidate won
    
# The winner of the election based on popular vote
    
