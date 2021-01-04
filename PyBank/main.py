# Import modules
import os
import csv

# Set file path
csvpath = os.path.join("Resources", "budget_data.csv" )

# Set variables
month_count = 0
Total_Profit_Loss = 0
Difference = 0
DiffMax = 0
DiffMin = 0
initial_profit = 0

# Create lists for Profit total and Average Profit change
Total_Profit = []
Difference_Total = []


# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Calculate analysis
    for i in csvreader:
    # Total months
        month_count = month_count + 1

    # Set monthly change variables
        month = i[0]
        Total = i[1]
        New_profit = int(Total)
        Diff = New_profit - initial_profit
        Monthly_Change = New_profit - initial_profit

    # Total Profit List Change
        Total_Profit.append(int(Total))
        
    # Greatest increase in profits over period
        if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month

    # Greatest decrease in losses over period
        if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month

    # Set New Profit to get changes
        initial_profit = New_profit

# Sum of Total Profit/Loss
Sum_Profit = sum(Total_Profit)


# Print Financial Analysis
print("Financial Analysis")
print("------------------------------------")
print(f'Total Months : {month_count}')
print(f'Total: $ {Sum_Profit}')
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {DiffMax})')
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {DiffMin})')


