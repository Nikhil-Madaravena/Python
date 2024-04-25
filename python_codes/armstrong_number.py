num=int(input("enter the numbr:"))
num1=num
sum=0
while num>0:
    rem=num%10
    sum+=rem**3
    num=num//10
if num1==sum:
    print(f"{num1} is a armstrong number")
else:
    print(f"{num1} is  not a armstrong number")

