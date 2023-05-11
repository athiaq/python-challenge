# import os module
import os
# import csv
import csv

#original join path did not work
csvpath = os.path.join('Resources', 'election_data.csv')

#/Users/athiaqureshi/Desktop/git/python-challenge/PyPoll/Resources/election_data.csv"

#Defining variables and lists
candidates_name = []

# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    first_row = next(csvreader)
    for row in csvreader:
        candidates_name.append(row[2])

candidate_options = []
candidate_votes = {}
for candidate in candidates_name:
    if candidate_votes.get(candidate):
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate]=1
#Calculating total votes
total_votes = len(candidates_name)
print(f'Total Votes: {total_votes}')

# List of candidates that received votes, the percentage of votes each candidate won and the number of votes each candidate won
for candidate, votes in candidate_votes.items():
    print(f'{candidate}: {round(votes/total_votes *100, 3)}% ({votes})')
    
# The winner of the election based on popular vote
winner = max(set(candidates_name), key= candidates_name.count)
print(f'Winner: {winner}')

# Create path and write text file
outputfile = "/Users/athiaqureshi/Desktop/git/python-challenge/PyPoll/analysis/analysis.txt"

with open(outputfile,"w",newline="\n") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("------------\n")
    for candidate, votes in candidate_votes.items():
        txt_file.write(f'{candidate}: {round(votes/total_votes *100, 3)}% ({votes})')
    txt_file.write("------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("------------\n")