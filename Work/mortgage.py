# mortgage.py
#
# Exercise 1.7

principal = 500000
rate = 0.05/12
payment_sum = 0;
months = 0;

while principal > 0:
    if months < 12:
        payment_month = 3684.11
    else:
        payment_month = 2684.11
    principal = principal * (1 + rate) - payment_month
    payment_sum += payment_month
    months += 1

print('Total paid', payment_sum)
print('Pay how many months', months)