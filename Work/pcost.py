# pcost.py
#
# Exercise 1.33
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # skipping the headline
        next(rows)
        cost = 0.0
        for row in rows:
            try:
                shares = int(row[1])
                price = float(row[2])
            except ValueError:
                print("This line missing something, couldn't be parsed:", row)
            cost += shares * price
    return cost

# reading filename from command line
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:>.2f}')