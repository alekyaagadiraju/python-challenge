# Import modules
import os
import csv

# Set file path
csvpath = os.path.join("Resources", "election_data.csv" )

# Set variables
voter_count = 0


# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Calculate analysis
    for i in csvreader:
    # Total months
        voter_count = voter_count + 1