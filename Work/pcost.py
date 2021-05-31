# pcost.py
#
# Exercise 3.14

# Strange instruction, 
# we just discard report.read_portfolio() in 3.12
# and use fileparse.parse_csv() instead.

# Therefore, to generalize the models, 
# in this exercise, I use fileparse.parse_csv()

import sys
from fileparse import parse_csv

def portfolio_cost(filename):
    records = parse_csv(filename, types=[str,int,float])
    cost = 0.0
    for record in records:
        try:
            cost += record['shares'] * record['price']
        except ValueError as e:
            print(f'Error occurs: {e}')
    return cost

# reading filename from command line
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost:>.2f}')