# mortgage.py

principal = 500000
rate = 0.05/12
payment = 2684.11
payment_sum = 0;
months = 0;

# Extra payment variables
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if (months>=extra_payment_start_month) and (months<=extra_payment_end_month):
        principal = principal * (1 + rate) - payment - extra_payment
        payment_sum += payment + extra_payment
    else:
        principal = principal * (1 + rate) - payment
        payment_sum += payment
    months += 1
    if principal > 0:
        print(f'{months}  {round(payment_sum,2)}  {round(principal,2)}')
    else:
        payment_sum = payment_sum + principal
        print(f'{months}  {round(payment_sum,2)}  0')


print(f'Total paid {round(payment_sum,2)}')
print(f'Pay how many months {months}')