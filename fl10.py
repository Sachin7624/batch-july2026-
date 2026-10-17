# 10: Write a Python program to count the number of digits in a number
num = int(input("Enter a number: "))
count = 0
for i in range(1, num + 1): 
    count = count + 1
    num = num // 10
    print("count=", count)
    
    