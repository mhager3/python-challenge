import os
import csv

csvpath1 = os.path.relpath('Resources/budget_data_1.csv')
csvpath2 = os.path.join('Resources', 'budget_data_2.csv')

# method to verify if the record is an entry starting with date
def isMonth(month):
    for item in months:
        if (month == item):
            return True
    
    return False

# method to print to file
def printToFile(totMonth, totRevenue, avgRevChange, grtIncDate, grtDecDate, grtIncrease, grtDecrease):
    with open("Financial Analysis HW.txt", "w") as text_file:
        print("Financial Analysis", file=text_file)
        print("------------------------------", file=text_file)
        print("Total months: %d" % (totMonth), file=text_file)
        print("Total Revenue: $%d" % (totRevenue), file=text_file)
        print("Average Revenue Change: $%.2f" % (avgRevChange), file=text_file)
        print("The greatest increase in revenue: ", (grtIncDate), (grtIncrease), file=text_file)
        print("The greatest decrease in revenue: ", (grtDecDate), (grtDecrease), file=text_file)
        print("\n", file=text_file)
    
        
# set variables
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
totMonth = 0
totRevenue = 0
revChange = 0
totRevChange = 0
avgRevChange = 0
grtIncrease = 0
grtDecrease = 0
grtIncDate = ""
grtDecDate = ""
previous = 0
skipRowCheck = True


with open(csvpath1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        trunkMonth = row[0].split("-")
        # print("trunkMonth: " + str(trunkMonth[0]))
        if (isMonth(trunkMonth[0])):
            totMonth = totMonth + 1

            # print("Revenue change: " + str(row[1]))
            totRevenue = int(totRevenue) + int(row[1])

            # set previous for the first time to current, so = 0
            if skipRowCheck:
                previous = row[1]
                skipRowCheck = False
            
            # get current revenue
            current = row[1]

            #get change in revenue and calc total
            revChange = int(current) - int(previous)
            totRevChange = totRevChange + revChange

            # set greatest increase in revenue and date
            if (revChange > grtIncrease):
                grtIncrease = revChange
                grtIncDate = (row[0])

            # set greatest decrease in revenue and date
            if (revChange < grtDecrease):
                grtDecrease = revChange
                grtDecDate = (row[0])

            # advance the previous revenue for next iteration
            previous = current

# calculate average revenue change
avgRevChange = (totRevChange/totMonth)

# print to file
printToFile(totMonth, totRevenue, avgRevChange, grtIncDate, grtDecDate, grtIncrease, grtDecrease)
            
# print to terminal
print("\nFinancial Analysis")
print("------------------------------")
print("Total months: " + str(totMonth))
print("Total Revenue: $" + str(totRevenue))
print("Average Revenue Change: $%.2f" % (avgRevChange))
print("The greatest increase in revenue: ", (grtIncDate), (grtIncrease))
print("The greatest decrease in revenue: ", (grtDecDate), (grtDecrease))
print("\n")



    