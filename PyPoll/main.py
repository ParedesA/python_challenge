import os
import csv

poll_csv=os.path.join('PyPoll','Resources','election_data.csv')

with open (poll_csv) as pollfile:
    reader=csv.reader(pollfile)
    poll_header = next(reader)

    votes = list(reader)
    
    grandtotalvotes=len(votes)
    charlesvotes=0
    dianavotes=0
    raymonvotes=0
    
    for row in votes:
        if (row[2]) == str('Charles Casper Stockham'):
            charlesvotes=charlesvotes+1
        elif (row[2]) == str('Diana DeGette'):
            dianavotes=dianavotes+1
        elif (row[2]) == str('Raymon Anthony Doane'):
            raymonvotes=raymonvotes+1
    
charlespercent=(charlesvotes/grandtotalvotes)*100
charlespercent="{:.3f}".format(charlespercent)
dianapercent=(dianavotes/grandtotalvotes)*100
dianapercent="{:.3f}".format(dianapercent)
raymonpercent=(raymonvotes/grandtotalvotes)*100
raymonpercent="{:.3f}".format(raymonpercent)

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