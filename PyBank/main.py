import os
import csv

csvpath1 = os.path.relpath('Resources/budget_data_1.csv')
csvpath2 = os.path.join('Resources', 'budget_data_2.csv')

# 
def isMonth(month):
    for item in months:
        if (month == item):
            return True
    
    return False
    
        

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
totMonth = 0
totRevenue = 0

with open(csvpath1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        trunkMonth = row[0].split("-")
        # print("trunkMonth: " + str(trunkMonth[0]))
        if (isMonth(trunkMonth[0])):
            totMonth = totMonth + 1
            # print("Revenue change: " + str(row[1]))
            totRevenue = int(totRevenue) + int(row[1])
        # print(totMonth)
        # print(totRevenue)
        

print("\nThere are a total of " + str(totMonth) + " months included in the data set.")
print("The total amount of revenue gained over the period is: " + str(totRevenue) + "\n")



    