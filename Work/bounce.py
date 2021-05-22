# bounce.py
#
# Exercise 1.5
height = 100

for hit in range(0,10):
    hit += 1
    height *= 0.6
    print(hit, round(height, 4))