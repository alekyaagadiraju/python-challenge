# Import modules
import os
import csv

# Set file path
csvpath = os.path.join("Resources", "budget_data.csv" )

# Set variables
month_count = 0
Total_Profit_Loss = 0
Difference = 0
Max_Difference = 0
Min_Difference = 0
initial_profit = 0

# Create list for Total Profit
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

    # Total Profits/Losses
        Total = i[1]
        Total_Profit.append(int(Total))

    #Set monthly change variables
        month = i[0]
        New_profit = int(i[1])
        Difference = New_profit - initial_profit
        Monthly_Change = New_profit - initial_profit
        
    # Monthly Profit/Loss Change
        Difference_Total.append(int(Monthly_Change)

    # Greatest increase in profits over period
        if Max_Difference < Difference:
             Max_Difference = Difference
             DiffMaxDate = month

    # Greatest decrease in losses over period
        if Min_Difference > Difference:
             Min_Difference = Difference
             DiffMinDate = month

    # Set New Profit to get changes
        initial_profit = New_profit

# Sum of Total Profit/Loss
Sum_Profit = sum(Total_Profit)

#Average of Monthly Changes
Avg_Profit_Change = ((sum(Difference_Total))/month_count)

# Print Financial Analysis
print("Financial Analysis")
print("------------------------------------")
print(f'Total Months : {month_count}')
print(f'Total: $ {Sum_Profit}')
print(f'Average Change: {Avg_Profit_Change}')
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {Max_Difference})')
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {Min_Difference})')

