# Import modules
import os
import csv

# Set file path
csvpath = os.path.join("..", "Resources","budget_data.csv" )

# Set variables
month_count = 0
Total = 0
Difference = 0
Max_Difference = 0
Min_Difference = 0

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
