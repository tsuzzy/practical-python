# report.py
#
# Exercise 2.16
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for rowno, row in enumerate(rows, start=1):
            holding = dict(zip(header, row))
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
                print("Function read_prices() EXCEPTION: empty line, can't add to dict!")
    return prices


def gain_loss(portfolio, prices):
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
            change = prices[d['name']] - float(d['price'])
            record = (d['name'], int(d['shares']), prices[d['name']], change)
            report.append(record)
    
    headers = ('Name', 'Shares', 'Price', 'Change')
    header_str = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}'
    print(header_str)

    separator = '---------- ---------- ---------- ----------'
    print(separator)

    for name, shares, price, chg in report: # Formatted table
        dollar = '$'+str(round(price,2)) # converting price from floating-point to string
        print(f'{name:>10s} {shares:>10d} {dollar:>10s} {chg:>10.2f}')


portfolio = read_portfolio('Data/portfoliodate.csv') # change file, output as the same
prices = read_prices('Data/prices.csv')

make_report(portfolio, prices)