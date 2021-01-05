# Import modules
import os
import csv

# Set file path
csvpath = os.path.join("Resources", "budget_data.csv" )

# Set variables
month_count = 0
Total_Profit_Loss = 0
Difference = 0
Diff_Max = 0
Diff_Min = 0
initial_profit = 0
Change = 0 

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
        Difference_Total.append((Diff))
        
    # Total Profit List Change
        Total_Profit.append(int(Total))

        
    # Greatest increase in profits over period
        if Diff_Max < Diff:
            Diff_Max = Diff
            DiffMaxDate = month     

    # Greatest decrease in losses over period
        if Diff_Min > Diff:
            Diff_Min = Diff
            DiffMinDate = month


    # Set New Profit to get changes
        initial_profit = New_profit

# Sum of Total Profit/Loss
Sum_Profit = sum(Total_Profit)

#Average of Monthly Changes
Avg_Profit_Change = (sum(Difference_Total) - Difference_Total[0])/ (len(Difference_Total)-1)

# Print Financial Analysis
print("Financial Analysis")
print("------------------------------------")
print(f'Total Months : {month_count}')
print(f'Total: $ {Sum_Profit}')
print(f'Average Change: {Avg_Profit_Change}')
print(f'Greatest Increase in Profits: {DiffMaxDate} : ($ {Diff_Max})')
print(f'Greatest Decrease in Profits: {DiffMinDate} : ($ {Diff_Min})')

with open('financial_analysis.txt', 'w') as text:
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(month_count) + "\n")
    text.write("    Total Profits: " + "$" + str(Sum_Profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(Avg_Profit_Change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(DiffMaxDate) + " ($" + str(Diff_Max) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(DiffMinDate) + " ($" + str(Diff_Min) + ")\n")
    


