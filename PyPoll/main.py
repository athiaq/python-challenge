import os
import csv

csvpath = "/Users/athiaqureshi/Desktop/git/python-challenge/PyPoll/Resources/election_data.csv"

#Defining variables and lists
total_votes = []
candidates_votes = []
percentage_won = []
total_won = 0
winner = ""
total = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)
    first_row = next(csvreader)

    # calculate the total number of votes
    for row in csvreader:
        total = total + 1
        votes_per_candidate =[]
        percentage = []
        candidates_votes = []
print(total)

# Complete list of candidates who received votes
'''candidates_votes = []
print(candidates_votes)'''


'''for candidate_name in candidate_votes:
    # Get the vote count and percentage
    votes = candidates_votes.get(candidate_name)
    vote_percentage = float(votes)/ float(total_votes)* 100'''
'''# Percentage of votes each candidate won 
percentage_won_charles = str(len(candidates_votes))
print(percentage_won_charles)

#total number of votes each candidate won
percentage = (candidates_votes) / (total) *100
print(percentage)'''