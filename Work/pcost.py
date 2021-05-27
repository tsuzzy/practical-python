# pcost.py
#
# Exercise 2.16
import csv
import sys

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # skipping the headline
        headers = next(rows)
        cost = 0.0
        for rowno,row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                cost += shares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return cost

# reading filename from command line
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:>.2f}')