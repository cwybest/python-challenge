import os
import csv
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath)as csvfile:
    name = []
    csvreader = csv.reader(csvfile, delimiter =",")
    header = next(csvreader)
    data = [str(row[2]) for row in csvreader]
    for i in range(len(data)-1):
       if data[i] != data[i+1]and data[i] not in name:
           name.append(data[i])
    votes=[data.count(name[j])for j in range(len(name))]
    total = sum(votes)
    percentage = ["{:.2%}".format(votes[x]/total) for x in range(len(votes))]
    winner = name[votes.index(max(votes))]
newlist = list(zip(name,votes,percentage))
def outcome():
    text = (f'Election Results\n _________________\nTotal Votes:{total}\n____________________\n{newlist}\n Winner: {winner}')
    return text
with open(os.path.join('Analysis',"analysis"), "w+") as f:
    f.write(outcome())
print(outcome())