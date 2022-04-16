import csv 

with open ('./Resources/budget_data.csv') as csvfile: #Start csv file handling

    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader)

    # Prepare variables
    months=[] 
    prolosses=[] 

    # Set start conditions
    total=0
    a_change=0
    m_change=0
    m_count=0
    delta1=0
    delta2=0
    delta_line1=0
    delta_line2=0
    loop1=0
    loop2=0

    # Read in each row of data after the header and write data into assigned lists
    for row in csvreader:
        month=row[0] #Assign column 0 as month
        proloss=row[1] #Assign column 1 as proloss
        months.append(month) #Add next line to list months
        prolosses.append(proloss) #Add next line to list prolosses
    
    # Count the total of months in the "Date" column
    m_count = len(months) 
    
    # print(m_count)


# First loop 
for loop1 in range (m_count):
    total=total+int(prolosses[loop1]) #Calculate total amount
# print(total)

# Second loop 
for loop2 in range (m_count-1): 
    a_change=a_change+(float(prolosses[loop2+1])-float(prolosses[loop2]))  

# Calculate monthly change
    m_change=(float(prolosses[loop2+1])-float(prolosses[loop2])) 
    if m_change>delta1: 
        delta1=m_change
        delta_line1=loop2
    else:
        delta1=delta1

# print(delta1)
# print(months[delta_line1+1])

    if m_change<delta2: 
        delta2=m_change
        delta_line2=loop2
    else:
        delta2=delta2

# print(delta2)
# print(months[delta_line2+1])

# Generate output lines

analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {m_count}\n\
Total Amount: ${total}\n\
Average Change: ${round(a_change/(m_count-1),2)}\n\
Greatest Increase in Profits: {months[delta_line1+1]} (${int(delta1)})\n\
Greatest Decrease in Profits: {months[delta_line2+1]} (${int(delta2)})\n'

# Output results 

print(analysis) 

# Write into text file named Financial_Analysis.txt

file1=open("Financial_Analysis.txt","w")
file1.writelines(analysis)
file1.close()