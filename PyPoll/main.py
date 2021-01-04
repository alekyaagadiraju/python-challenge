# Import modules
import os
import csv

# Set file path
csvpath = os.path.join("Resources", "election_data.csv" )

# Set variables
voter_count = 0

# List of voters
candidate_list = []
voter_countlist = []
candidate_percent = []

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Calculate analysis
    for i in csvreader:
    # Total months
        voter_count = voter_count + 1

    # list of candidates
        candidate = i[2]
        if not candidate in candidate_list:
            candidate_list.append(candidate)
            #add first vote for this candidate
            voter_countlist.append(1)
            #else add another vote for this candidate
        else:
            indexofCandidate =  candidate_list.index(candidate)
            VoteTally = voter_countlist[indexofCandidate]
            #increase vote tally for this candidate by 1
            voter_countlist[indexofCandidate] = VoteTally+1
            
    #compute percentage
            
    for candidate in candidate_list:
            votes = voter_countlist[candidate_list.index(candidate)]
            percent_of_votes = (votes/voter_count)*100
            candidate_percent.append(percent_of_votes)


print(f'{candidate_percent}')
# Print Election Results
print("Election Results")
print("------------------------------------")
print(f'Total Votes : {voter_count}')
print("------------------------------------")
print(f'{candidate_list[0]} : {candidate_percent[0]}% ({voter_countlist[0]})') 
print(f'{candidate_list[1]} : {candidate_percent[1]}% ({voter_countlist[1]})') 
print(f'{candidate_list[2]} : {candidate_percent[2]}% ({voter_countlist[2]})') 
print(f'{candidate_list[3]} : {candidate_percent[3]}% ({voter_countlist[3]})') 
print("------------------------------------")