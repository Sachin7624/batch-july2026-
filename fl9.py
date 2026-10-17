# 9: Write a Python program to print a multiplication table of any number.
n = int(input("Enter a number: "))
for i in range(1, 11):
    if i <= 10:
       print(n, "x", i, "=", n * i)
    