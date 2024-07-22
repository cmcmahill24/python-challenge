import os
import csv

#Set Path for CSV File
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#Set Variables 
total_months = 0
Total_Profit_Loss = 0
change = []
changes = []
previous_profit_loss = None 
average_change = None

#Open CSV File
with open(budget_csv, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip the header row
    next(csv_reader)

#Find Total Number of Months in Dataset
    for row in csv_reader:
        total_months += 1
        Profit_Loss = int(row[1])  
        Total_Profit_Loss += Profit_Loss

#Net Total Amount of Profit/Losses Over Entire Period
        if previous_profit_loss is not None:
            change = Profit_Loss - previous_profit_loss
            changes.append(change)
        
        previous_profit_loss = Profit_Loss

        # Average of changes in Profit/Losses over entire period
        if len(changes) > 0:
            average_change = sum(changes) / len(changes)
            average_change_rounded = round(average_change, 2)

            #Greatest Increse/Decrease of Profits
            Greatest_Increase = max(changes)
            Greatest_Decrease = min(changes)

    Greatest_Increase = max(changes)
    Greatest_Decrease = min(changes)
    Greatest_Increase_Index = changes.index(Greatest_Increase)
    Greatest_Decrease_Index = changes.index(Greatest_Decrease)

#Print Dates of Greatest Increase/Decrease of Profits
    Dates = []
    csv_file.seek(0)
    next(csv_file)
    next(csv_file)

    for row in csv_reader:
        Dates.append(row[0])

Greatest_Increase_Date = Dates[Greatest_Increase_Index]
Greatest_Decrease_Date = Dates[Greatest_Decrease_Index]

#Print Results to Terminal
print(f"Financial Analysis")
print(f"-------------------------")
print(f"Total Months: {total_months}")
print(f"Net Profit/Losses: {Total_Profit_Loss}")
print(f"Average Change: ${average_change_rounded}")
print(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})")

#Print Results to Text File
analysis_path = os.path.join("..", "Analysis")
f = open(f"{analysis_path}/PyBank_Code.txt" , "w")
print(f"Financial Analysis", file= f)
print(f"----------------------------------", file = f)
print(f"Total Months: {total_months}", file= f)
print(f"Net Profit/Losses: {Total_Profit_Loss}", file= f)
print(f"Average Change: ${average_change_rounded}", file=f)
print(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})", file= f)
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})", file = f)

