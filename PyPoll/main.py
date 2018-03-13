import os
import csv


csvpath1 = os.path.relpath('Resources/election_data_1.csv')
csvpath2 = os.path.join('Resources', 'election_data_2.csv')

def printToFile(totVotes, voteCtr):
    highvote = 0
    winner = ""
    with open("Voter Results HW.txt", "w") as text_file:
        print("\nElection Results", file=text_file)
        print("------------------------------", file=text_file)
        print("Total Votes: ", totVotes, file=text_file)
        print("------------------------------", file=text_file)
        #print(voteCtr)
        for keys in voteCtr:
            percentage = ((voteCtr[keys]/totVotes)*100)
            
            #print("%s: %.1f " % (keys, percentage), voteCtr[keys])
            print(f'{keys}: {percentage:.1f}% ({voteCtr[keys]})', file=text_file)
            if voteCtr[keys] > highvote:
                highvote = voteCtr[keys]
                winner = keys
        print("------------------------------", file=text_file)
        print(f'Winner: {winner}', file=text_file)
        print("------------------------------", file=text_file)

# variables
totVotes = 0
candidates = []
voteCtr = {}
highvote = 0
winner = ""

with open(csvpath1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        totVotes = totVotes + 1

        if row[2] not in voteCtr.keys():
            voteCtr[row[2]] = 1
        else:
            voteCtr[row[2]] = voteCtr[row[2]] + 1


print("\nElection Results")
print("------------------------------")
print("Total Votes: ", totVotes )
print("------------------------------")
#print(voteCtr)
for keys in voteCtr:
    percentage = ((voteCtr[keys]/totVotes)*100)
    
    #print("%s: %.1f " % (keys, percentage), voteCtr[keys])
    print(f'{keys}: {percentage:.1f}% ({voteCtr[keys]})')
    if voteCtr[keys] > highvote:
        highvote = voteCtr[keys]
        winner = keys
print("------------------------------")
print(f'Winner: {winner}')
print("------------------------------")

printToFile(totVotes, voteCtr)