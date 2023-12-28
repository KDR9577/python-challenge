#Import modules
import os
import csv

#Add csv file
file = os.path.join("PyBank", "Resources.csv")

#Read csv
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

#Calculate total number of months
months = csvreader["Date"]

#Total amount of profit/losses over the period

#Changes in profit/losses over the period, and average of those changes

#Greatest increase in profits (date and amount) over the period

#Greatest decrease in profits (date and amount) over the period