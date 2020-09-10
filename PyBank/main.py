import os
import csv
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath)as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    header = next(csvreader)
    revenue = []
    months = []
    for row in csvreader:
        revenue.append(float(row[1]))
        months.append(str(row[0]))
    counter = len(revenue)
    net_total = sum(revenue)
    avg_changes = (revenue[-1]-revenue[0])/counter
    monthly_change = [revenue[i]-revenue[i-1]for i in range(counter)]
    value_of_increase = max(monthly_change)
    month_of_increase =months[monthly_change.index(value_of_increase)]
    value_of_decrease = min(monthly_change)
    month_of_decrease =months[monthly_change.index(value_of_decrease)]
with open(os.path.join('Analysis',"analysis"), "w+") as f:
    def results():
        text = f'Financial Analysis\nTotal Months: {counter}\nTotal: {net_total}\nAverage Change: {avg_changes}\nGreatest Increase in Profit: {month_of_increase}, {value_of_increase}\nGreatest Decrease in Profits:{month_of_decrease}, {value_of_decrease}'
        return text
    f.write(results())
print(results())
