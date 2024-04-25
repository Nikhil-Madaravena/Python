n = int(input("Enter a number: "))
temp = n

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def strong(n):
    temp = n
    sum_of_factorials = 0
    while n > 0:
        digit = n % 10
        sum_of_factorials += factorial(digit)
        n //= 10
    return sum_of_factorials

result = strong(n)

if result == temp:
    print(f"{temp} is a strong number.")
else:
    print(f"{temp} is not a strong number.")

