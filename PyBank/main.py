#import os module to create file paths across operating systems
import os

#import module to read csv files
import csv

#create path to the csv file
csvpath = os.path.join('Resources','budget_data.csv')

#open the csv file based on path
with open(csvpath) as csvfile:

    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #read the header row first
    csv_header = next(csvreader)
    
    #convert csv to list and create an array to store profits as integers
    #citation: https://stackoverflow.com/questions/24662571/python-import-csv-to-list
    convert_to_list = list(csvreader)
    
    profit_list = []
    
    for row in convert_to_list:
        profit = int(row[1])
        profit_list.append(profit)
    
    #get total number of rows / months in the csv file
    month_count = len(convert_to_list)
    
    #get net total amount of profit/losses 
    total = sum(profit_list)

    #create an array to store profit changes between months
    profit_changes = []

    for i in range(1,len(profit_list)):
        change = profit_list[i] - profit_list[i-1]
        profit_changes.append(change)

    #get average of the changes in profit/losses
    average_profit_change = round(sum(profit_changes)/len(profit_changes),2)

    #get greatest increaes in profits (date and amount)
    #citation: https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
    max_profit_change = max(profit_changes)
    index_of_max = profit_changes.index(max_profit_change)
    month_of_max = convert_to_list[index_of_max+1][0]

    #get greatest decrease in losses (date and amount)
    #citation: https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
    min_profit_change = min(profit_changes)
    index_of_min = profit_changes.index(min_profit_change)
    month_of_min = convert_to_list[index_of_min+1][0]

#print out results to the terminal
print("Financial Analysis \n------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average Change: ${average_profit_change}")
print(f"Greatest Increase in Profits: {month_of_max} (${max_profit_change})")
print(f"Greatest Decrease in Profits: {month_of_min} (${min_profit_change})")

#create a new text file under analysis folder to store results
txtpath = os.path.join('Analysis','result.txt')

#store the respective values to the text file using write function
txtfile = open(txtpath,'w')
txtfile.write("Financial Analysis \n")
txtfile.write("---------------------------- \n")
txtfile.write(f"Total Months: {month_count} \n")
txtfile.write(f"Total: ${total} \n")
txtfile.write(f"Average Change: ${average_profit_change} \n")
txtfile.write(f"Greatest Increase in Profits: {month_of_max} (${max_profit_change}) \n")
txtfile.write(f"Greatest Decrease in Profits: {month_of_min} (${min_profit_change}) \n")
txtfile.close()