import os
import csv

bank_csv=os.path.join("PyBank","Resources","budget_data.csv")

#this will be used in the loop to calculate changes
previous_row = 0

with open (bank_csv) as csvfile:
    reader = csv.reader(csvfile)
    bank_header = next(reader)

    mylist = list(reader)
    lines = "Date"
    for row in mylist:
        if row==lines:
            mylist.remove(row)

    #to responde to total number of months in dataset
    total_month = len(mylist)

    #creating lists to hold values for calculations
    profit_losses = []
    all_changes = []

    for row in mylist:
        profit_losses.append(int(row[1]))
        all_changes.append(int(row[1]) - (int(previous_row)))
        previous_row = int(row[1])

    all_changes.pop(0)

    greatest_increase = max(all_changes)
    greatest_decrease = min(all_changes)
    profit_losses_total = sum(profit_losses)
    average_change = sum(all_changes)/(len(all_changes))
    average_change = "{:.2f}".format(average_change)

with open(os.path.join("PyBank","Analysis","FinancialAnalysis.txt"),"w") as output:
    output.write("\nFinancial Analysis\n\n--------------------\n")
    output.write(f"Total Months:{total_month}\n")
    output.write(f"Total: ${profit_losses_total}\n")
    output.write(f"Average Change: ${average_change}\n")
    output.write(f"Greatest Increase in Profits: (${greatest_increase})\n")
    output.write(f"Greatest Decrease in Profits: (${greatest_decrease})")

    #to print all the results:
    print("\nFinancial Analysis\n\n--------------------\n")
    print(f"Total Months:{total_month}\n")
    print(f"Total: ${profit_losses_total}\n")
    print(f"Average Change: ${average_change}\n")
    print(f"Greatest Increase in Profits: (${greatest_increase})\n")
    print(f"Greatest Decrease in Profits: (${greatest_decrease})")
    
