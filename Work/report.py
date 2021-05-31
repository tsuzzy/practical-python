# report.py
#
# Exercise 3.12
from fileparse import parse_csv

def make_report(portfolio, prices):
    '''
    Make reports
    '''
    report = []
    
    # Convert tuple to dictionary
    price = {}
    for r in prices:
        name, cur_price = r
        price[name] = cur_price
    prices = price

    for d in portfolio:
        if d['name'] in prices:
            change = prices[d['name']] - d['price']
            record = (d['name'], d['shares'], prices[d['name']], change)
            report.append(record)
    
    headers = ('Name', 'Shares', 'Price', 'Change')
    header_str = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}'
    print(header_str)

    separator = '---------- ---------- ---------- ----------'
    print(separator)

    return report


def print_report(report):
    '''
    Output the report
    '''
    for name, shares, price, chg in report: # Formatted table
        dollar = '$'+str(round(price,2)) # converting price from floating-point to string
        print(f'{name:>10s} {shares:>10d} {dollar:>10s} {chg:>10.2f}')


def portfolio_report():
    '''
    Merge the functions into the top-level function
    '''
    portfolio = parse_csv('Data/portfolio.csv',types=[str,int,float])
    prices = parse_csv('Data/prices.csv',types=[str,float],has_headers=False)
    print_report(make_report(portfolio, prices))


# Adding back retired read_portfolio() and read_prices()
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
                pass
    return prices