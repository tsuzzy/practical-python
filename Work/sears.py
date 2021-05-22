import sys

bill_thick = 0.11 * 0.001
sears_height =442

num_bills = 1
day = 1
money_i_have = float(sys.argv[1])

while num_bills * bill_thick < sears_height:
    print(day, num_bills, num_bills*bill_thick)
    day += 1
    num_bills = num_bills * 2

print('Number of days:', day)
print('Number of bills:', num_bills)
print('Final height:', num_bills * bill_thick)

if num_bills <= money_i_have:
    print("Do it!")
else:
    print("Go to find enough money pls")