# 7: Write a Python program to find the sum of all even numbers between 1 to n.
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum = sum + i
    print("sum of even number=", sum)
        