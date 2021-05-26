# report.py
#
# Exercise 2.6
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
                print("Successfully added to dict.")
            except:
                print("Empty line, can't add to dict!")
    return prices