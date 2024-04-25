'''num = int(input("Enter a three digit number: "))
n = num
new = 0 
if num >= 100 and num <= 999: 
    i = 1
    while i <= 3:
        t = num % 10 
        new = (new * 10)+t
        num = num // 10 
        i += 1 
else:
    print("The entered number is not a three digit number")
print("The reversed value of", n, "is:", new)'''


