#Import modules
import os
import csv

#Add csv file
file = os.path.join("PyBank", "Resources.csv")
outfile = os.path.join("PyBank", "analysis", "financial_analysis.txt")

total_months = 0
profits_losses = 0
#Read csv
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    cat = next(csvreader)


    for row in csvreader:
        #Calculate total number of months
        total_months = total_months + 1
    
    

        #Total amount of profit/losses over the period
        profits_losses = profits_losses + int(row[1])


    #Changes in profit/losses over the period, and average of those changes


    #Greatest increase in profits (date and amount) over the period


    #Greatest decrease in profits (date and amount) over the period
        
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${profits_losses}\n"

)
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

with open(outfile, "w") as txtfile:
    print(output)
    txtfile.write(output)