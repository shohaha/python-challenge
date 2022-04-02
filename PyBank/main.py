import csv
import os

# Locate CSV file
file = "./Resources/budget_data.csv"

# Create placeholder lists for the data
months = []
net_total = []
 
with open (file, newline = "") as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ',')
 
    csv_header = next(csvfile)

# Put the data into lists
    for row in readcsv:
        months.append(row[0])
        net_total.append(int(row[1]))

# Count the number of months
month_count = len(months)

# Set variables for loops
x = 1
y = 0

# Average change place holder
average_change = (net_total[1]-net_total[0])

# Place holder list for changes
changes = []

# For loop to calculate month to month change and move values into list
for month in range(month_count-1):
        average_change = (net_total[x] - net_total[y])
        changes.append(int(average_change))
        x+=1
        y+=1

# Calculate the average monthly change and round average
av_mon_chng = round(sum(changes)/(month_count -1),2)

# Find the min and max change 
min_change = min(changes)
max_change = max(changes)

# Return the index to find the positions in the list
chng_i_min = changes.index(min_change)
chng_i_max = changes.index(max_change)

# Find the months for the min and max changes
min_chng_month = months[chng_i_min + 1]
max_chng_month = months[chng_i_max + 1]

# Print the values in console 
print("Financial Analysis")
print("----------------------------")
print(f"Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Monthly Change: {av_mon_chng}")
print(f"Greatest Increase in Profits: {max_chng_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})")

# Output to text file
fin_analysis = open("Financial_Analysis.txt","w")
 
fin_analysis.write("Financial Analysis\n")
fin_analysis.write("----------------------------\n")
fin_analysis.write(f"Months: {len(months)}\n")
fin_analysis.write(f"Total: ${sum(net_total)}\n")
fin_analysis.write(f"Average Monthly Change: {av_mon_chng}\n")
fin_analysis.write(f"Greatest Increase in Profits: {max_chng_month} (${max_change})\n")
fin_analysis.write(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})\n")
 
  
fin_analysis.close() 