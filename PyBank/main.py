import os
import csv
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath)as csvfile:
    csvreader = csv.reader(csvfile,delimiter =",")
    header = next(csvreader)
    revenue = [float(row[1]) for row in csvreader]
    months = [str(row[0]) for row in csvreader]
    counter = len(revenue)
    net_total = sum(revenue)
    avg_changes = (revenue[-1]-revenue[0])/counter
    monthly_change = [revenue[i]-revenue[i-1]for i in range(counter)]
    #greatest_increase =months[monthly_change.index(max(monthly_change))]
    for row in csvreader:
        print(row)
   