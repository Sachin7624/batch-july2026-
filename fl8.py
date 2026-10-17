#8: Write a Python program to find the sum of all odd numbers between
n = 10
sum = 0
for i in range(n + 1):
    if i % 2 != 0:
        sum = sum + i
    print("sum of odd number=", sum)
    