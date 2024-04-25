a=input("Enter a number : ")
b=input("Enter another number : ")
c=input("operator(+,-,*,/) : ")
a=int(a)
b=int(b)
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)
else:
    print("Invalid operator")