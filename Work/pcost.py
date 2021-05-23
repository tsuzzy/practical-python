# pcost.py
#
# Exercise 1.31
def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        header = next(f).split(',')
        cost = 0.0
        for line in f:
            try:
                row = line.split(',')
                shares = int(row[1])
                price = float(row[2])
            except ValueError:
                print("This line missing something, couldn't parse:", line)
            cost += shares * price
    return cost

cost = portfolio_cost('Data/missing.csv')
print('Total cost', cost)