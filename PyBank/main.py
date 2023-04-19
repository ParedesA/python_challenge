import os
import csv

#to show the path to the resources document
bank_csv=os.path.join("PyBank","Resources","budget_data.csv")

#this variable is needed for the loop to calculate changes
previous_row = 0

#to create a reader for the resources csv file
with open (bank_csv) as csvfile:
    reader = csv.reader(csvfile)
    bank_header = next(reader) #to skip header on resources file

    #I will remove the header all together so it will not cause issues on my calculations
    mylist = list(reader)
    lines = "Date"
    for row in mylist:
        if row==lines:
            mylist.remove(row)

    #to calculate to total number of months in dataset
    total_month = len(mylist)

    #creating lists to hold values for calculations
    profit_losses = []
    all_changes = []

    #this will populate values to my lists
    for row in mylist:
        profit_losses.append(int(row[1]))
        all_changes.append(int(row[1]) - (int(previous_row)))
        previous_row = int(row[1])

    #this will remove the first row so it will not cause issues on my total average changes calculation
    all_changes.pop(0)

    #functions to find the results and formating
    greatest_increase = max(all_changes)
    greatest_decrease = min(all_changes)
    profit_losses_total = sum(profit_losses)
    average_change = sum(all_changes)/(len(all_changes))
    average_change = "{:.2f}".format(average_change)

#this will populate the results to my output file
with open(os.path.join("PyBank","Analysis","FinancialAnalysis.txt"),"w") as output:
    output.write("\nFinancial Analysis\n\n--------------------\n")
    output.write(f"Total Months:{total_month}\n")
    output.write(f"Total: ${profit_losses_total}\n")
    output.write(f"Average Change: ${average_change}\n")
    output.write(f"Greatest Increase in Profits: (${greatest_increase})\n")
    output.write(f"Greatest Decrease in Profits: (${greatest_decrease})")

    #to print all the results in terminal
    print("\nFinancial Analysis\n\n--------------------\n")
    print(f"Total Months:{total_month}\n")
    print(f"Total: ${profit_losses_total}\n")
    print(f"Average Change: ${average_change}\n")
    print(f"Greatest Increase in Profits: (${greatest_increase})\n")
    print(f"Greatest Decrease in Profits: (${greatest_decrease})")
    
