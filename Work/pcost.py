# pcost.py
#
# Exercise 3.15

# Strange instruction, 
# we just discard report.read_portfolio() in 3.12
# and use fileparse.parse_csv() instead.

# Therefore, to generalize the models, 
# in this exercise, I use fileparse.parse_csv()

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

def main(argv):
    try:
        portfolio_file = argv[1]
    except:
        portfolio_file = 'Data/portfolio.csv'
        print(f'You didnt provide filename, using {portfolio_file} as default file.')
    
    cost = portfolio_cost(portfolio_file)
    print(f'Total cost: {cost:>.2f}')

if __name__ == '__main__':
    import sys
    main(sys.argv)