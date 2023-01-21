# import os module 
import os

#Import csv files
import csv

#original join path did not work
csvpath = "/Users/athiaqureshi/Desktop/git/python-challenge/PyBank/Resources/budget_data.csv"

# lists to store data
total_months = 0
month_of_change = []
net_change_list = []
total_net = 0

# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row 
    csv_header = next(csvreader)
    first_row = next(csvreader)
    # Calculate the total months, calculate the net amount of profits losses over the entire period 
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in csvreader:
         total_months += 1
         total_net += int(row[1])
         net_change = int(row[1]) - prev_net
         prev_net = int(row[1])
         net_change_list += [net_change]
         month_of_change += [row[0]]
print(total_months)
print(total_net)
print(net_change)

#Calculate tha average of changes
avg_value = sum(net_change_list)/len(net_change_list)
print(avg_value)


maxChange= max(net_change_list)
print(maxChange)

print(month_of_change)

# Index where greatest increase in profits occurs
net_change_list += [net_change]
max_value = max(net_change_list)
index = net_change_list.index(max_value)
print(index)

# Print the month of change with the Greatest increase in profits:
print(f'Greatest Increase in Profits: {month_of_change[index]} ({max_value})')

# Greatest decrease in profits 
minChange = min(net_change_list)
print(minChange)

# Index where greatest decrease occurs
net_change_list += [net_change]
min_value = min(net_change_list)
index = net_change_list.index(min_value)
print(index)

#print the month of change with the greatest decrease in profits
print(f'Greatest Decrease in Profits: {month_of_change[index]} ({min_value})')

# Create a path and write txt file 
print(f"Financial Analysis\n-------------------------------\nTotal Months: {total_months}\nTotal: ${sum(net_change_list)}\nAverage Change: ${net_change}\nGreatest Increse in Profits: {month_of_change[index]} (${max_value})\nGreatest Decrease in Profits: {month_of_change[index]} (${min_value})")


outputfile = "/Users/athiaqureshi/Desktop/git/python-challenge/PyBank/analysis/analysis.txt"
with open(outputfile,"w", newline ="") as txt_file:
    txt_file.write(f"Financial Analysis\n-------------------------------\nTotal Months: {total_months}\nTotal: ${sum(net_change_list)}\nAverage Change: ${net_change}\nGreatest Increse in Profits: {month_of_change[index]} (${max_value})\nGreatest Decrease in Profits: {month_of_change[index]} (${min_value})")