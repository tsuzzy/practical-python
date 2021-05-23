# pcost.py
#
# Exercise 1.27
f = open('Data/portfolio.csv', 'rt')
header = next(f).split(',')

cost = 0.0
for line in f:
    row = line.split(',')
    shares = int(row[1])
    price = float(row[2])
    cost += shares * price

print('Total cost', cost)

f.close()