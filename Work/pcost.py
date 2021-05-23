# pcost.py
#
# Exercise 1.32
import csv

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        cost = 0.0
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
            except ValueError:
                print("This line missing something, couldn't parse:", row)
            cost += shares * price
    return cost

cost = portfolio_cost('Data/missing.csv')
print('Total cost', cost)