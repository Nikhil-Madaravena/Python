a=input("Enter first number : ")
b=input("Enter second number : ")
c=input("Enter third number : ")
if a==b and b==c:
    print("All are equal")
elif a>=b and a>=c:
    print("Greatest is "+str(a))
elif b>=a and b>=c:
    print("Greatest is "+str(b))
elif c>=a and c>=b:
    print("Greatest is "+str(c))
