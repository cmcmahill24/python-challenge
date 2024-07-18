import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

total_months = 0
Total_Profit_Loss = 0
change = []
changes = []
previous_profit_loss = None 
average_change = None

with open(budget_csv, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip the header row
    next(csv_reader)

    for row in csv_reader:
        total_months += 1
        Profit_Loss = int(row[1])  
        Total_Profit_Loss += Profit_Loss

        if previous_profit_loss is not None:
            change = Profit_Loss - previous_profit_loss
            changes.append(change)
        
        previous_profit_loss = Profit_Loss
         
        if len(changes) > 0:
            average_change = sum(changes) / len(changes)
            average_change_rounded = round(average_change, 2)

            

print(f"Total Months: {total_months}")
print(f"Net Profit/Losses: {Total_Profit_Loss}")
print(f"Average Change: ${average_change_rounded}")