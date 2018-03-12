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

def printToFile(totMonth, totRevenue, avgRevChange, grtIncrease, grtDecrease):
    with open("Financial Analysis HW.txt", "w") as text_file:
        print("Financial Analysis", file=text_file)
        print("------------------------------", file=text_file)
        print("Total months: %d" % (totMonth), file=text_file)
        print("Total Revenue: $%d" % (totRevenue), file=text_file)
        print("Average Revenue Change: $%.2f" % (avgRevChange), file=text_file)
        print("The greatest increase in revenue: $%d" % (grtIncrease), file=text_file)
        print("The greatest decrease in revenue: $%d" % (grtDecrease), file=text_file)
        print("\n", file=text_file)
    
        

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
totMonth = 0
totRevenue = 0
revArr = []
revChange = 0
totRevChange = 0
avgRevChange = 0
grtIncrease = 0
grtDecrease = 0
grtIncDateIndex = 0
grtDecDateIndex = 0



with open(csvpath1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        trunkMonth = row[0].split("-")
        # print("trunkMonth: " + str(trunkMonth[0]))
        if (isMonth(trunkMonth[0])):
            totMonth = totMonth + 1
            # print("Revenue change: " + str(row[1]))
            totRevenue = int(totRevenue) + int(row[1])
            revArr.append(row[1])
    # print("revArr: " + str(revArr))

    for i in range(len(revArr) - 1):
        revChange = (int(revArr[i + 1]) - int(revArr[i]))
        totRevChange = totRevChange + revChange
        if (revChange > grtIncrease):
            grtIncrease = revChange
            grtIncDateIndex = (i + 1)
        if (revChange < grtDecrease):
            grtDecrease = revChange
            grtDecDateIndex = (i + 1)
    

avgRevChange = (totRevChange/totMonth)

printToFile(totMonth, totRevenue, avgRevChange, grtIncrease, grtDecrease)
            
# print to terminal
print("\nFinancial Analysis")
print("------------------------------")
print("Total months: " + str(totMonth))
print("Total Revenue: $" + str(totRevenue))
print("Average Revenue Change: $%.2f" % (avgRevChange))
print("The greatest increase in revenue: %s" % str(grtIncrease))
print("The greatest decrease in revenue: " + str(grtDecrease))
print("\n")



    