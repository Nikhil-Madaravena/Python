#  59 reverse of num
num=int(input("enter the numbr:"))
num1=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10 + rem
    num=num//10
print(f"the reverse of {num1} is {rev}")
