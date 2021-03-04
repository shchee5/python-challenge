#import os module to create file paths across operating systems
import os

#import module to read csv files
import csv

#create path to the csv file
csvpath = os.path.join('Resources','election_data.csv')

#open the csv file based on path
with open(csvpath) as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row first
    csv_header = next(csvreader)

    #create a dictionary for candidates and count of votes
    vote_counter = {}
    
    #for loop to go through all rows in file
    #if the candidate name exists in dictionary, add 1; if not, create an entry
    for row in csvreader:
        name = row[2]
        if name in vote_counter:
            vote_counter[name] += 1
        else:
            vote_counter[name] = 1
        
#calculate total votes and which candidate has the highest vote count
Total_Votes = sum(vote_counter.values())
Maximum_Votes = max(vote_counter.values())

print("Election Results \n---------------------")
print(f"Total Votes: {Total_Votes} \n---------------------")

#print dictionary entries - candidate name, percent of total vote counts, total vote counts
for key,value in vote_counter.items():
    percent_of_total = (value/Total_Votes)*100
    rounded_percent = round(percent_of_total,4)
    print(key,":", rounded_percent,"% (",value,")")

print("---------------------")

#print winner by checking which candidate has the highest vote count
for key,value in vote_counter.items():
    if value == Maximum_Votes:
        print("Winner: ",key)

print("---------------------")

#create a new text file under analysis folder to store results
txtpath = os.path.join('Analysis','result.txt')

#list(vote_counter.items())[0][1]

#store the respective values to the text file using write function
txtfile = open(txtpath,'w')
txtfile.write("Election Results \n---------------------\n")
txtfile.write(f"Total Votes: {Total_Votes} \n---------------------\n")

txtfile.write("\n---------------------\n")
txtfile.write("Winner: \n---------------------")

txtfile.close()