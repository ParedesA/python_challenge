import os
import csv

#to show the path to the resources document
poll_csv=os.path.join('PyPoll','Resources','election_data.csv')

#to create a reader for the resources csv file
with open (poll_csv) as pollfile:
    reader=csv.reader(pollfile)
    poll_header = next(reader) #to skip the hearder

    #to create a list with the reader data
    votes = list(reader)
    
    #to count the total of votes all together
    grandtotalvotes=len(votes)
    #these are the variable that will hold each vote by candidate
    charlesvotes=0
    dianavotes=0
    raymonvotes=0
    
    #loop to calculate how many votes each candidate received
    for row in votes:
        if (row[2]) == str('Charles Casper Stockham'):
            charlesvotes=charlesvotes+1
        elif (row[2]) == str('Diana DeGette'):
            dianavotes=dianavotes+1
        elif (row[2]) == str('Raymon Anthony Doane'):
            raymonvotes=raymonvotes+1

#functions to calculate the percentage of votes received and change format of output
charlespercent=(charlesvotes/grandtotalvotes)*100
charlespercent="{:.3f}".format(charlespercent)
dianapercent=(dianavotes/grandtotalvotes)*100
dianapercent="{:.3f}".format(dianapercent)
raymonpercent=(raymonvotes/grandtotalvotes)*100
raymonpercent="{:.3f}".format(raymonpercent)

#to print results to terminal
print("Election Results\n\n--------------------\n")
print(f"Total Votes: { grandtotalvotes}\n\n--------------------\n")
print(f"Charles Casper Stockham: { charlespercent}% ({charlesvotes})\n")
print(f"Diana DeGette: { dianapercent}% ({dianavotes})\n")
print(f"Raymon Anthony Doane: { raymonpercent}% ({raymonvotes})\n\n--------------------\n")

if charlesvotes > dianavotes and charlesvotes > raymonvotes:
    print('Winer: Charles Casper Stockham\n\n--------------------')
elif dianavotes > charlesvotes and dianavotes > raymonvotes:
    print('Winner: Diana DeGette\n\n--------------------')
else:
    print('Winner: Raymon Anthony Doane\n\n--------------------')

#to print results to output file
with open(os.path.join("PyPoll","Analysis","ElectionResults.txt"),"w") as output:
    output.write("Election Results\n\n--------------------\n")
    output.write(f"Total Votes: { grandtotalvotes}\n\n--------------------\n")
    output.write(f"Charles Casper Stockham: { charlespercent}% ({charlesvotes})\n")
    output.write(f"Diana DeGette: { dianapercent}% ({dianavotes})\n")
    output.write(f"Raymon Anthony Doane: { raymonpercent}% ({raymonvotes})\n\n--------------------\n")

    if charlesvotes > dianavotes and charlesvotes > raymonvotes:
        output.write('Winer: Charles Casper Stockham\n\n--------------------')
    elif dianavotes > charlesvotes and dianavotes > raymonvotes:
        output.write('Winner: Diana DeGette\n\n--------------------')
    else:
        output.write('Winner: Raymon Anthony Doane\n\n--------------------')