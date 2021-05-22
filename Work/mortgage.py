# mortgage.py
#
# Exercise 1.7

principal = 500000
rate_year = 0.05
payment_month = 2684.11
payment_year = payment_month * 12
payment_sum = 0;
count = 0;

while principal > 0:
    principal = principal * (1 + rate_year) - payment_year
    payment_sum += payment_year
    count += 1

print('Total paid', payment_sum)
print('Pay how many years', count)