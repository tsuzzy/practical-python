# report.py
#
# Exercise 2.9
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = { # dict
                header[0]: row[0],
                header[1]: int(row[1]),
                header[2]: float(row[2])
            }
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {} # init an empty dict
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                print("Empty line, can't add to dict!")
    return prices

def gain_loss():
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    total = 0.0
    for s in portfolio:
        if s['name'] in prices:
            current_price = prices[s['name']]
            buy_price = s['price']
            profit = (current_price - buy_price) * s['shares']
            if profit > 0:
                print(f'You gain {profit: 0.2f} in the stock', s['name'], ', you have been closer to retire! :D')
            else:
                print(f'You lost {profit: 0.2f} in the stock', s['name'])
            total += profit
    print(f'Your total gain/loss is {total: 0.2f}')

def make_report(portfolio, prices):
    report = []
    for d in portfolio:
        if d['name'] in prices:
            change = prices[d['name']] - d['price']
            record = (d['name'], d['shares'], prices[d['name']], change)
            report.append(record)
    return report