# pcost.py
#
# Exercise 1.30
def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        header = next(f).split(',')
        cost = 0.0
        for line in f:
            row = line.split(',')
            shares = int(row[1])
            price = float(row[2])
            cost += shares * price
    return cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', cost)