print("Enter 3 sides of the triangle : ")
a=input()
b=input()
c=input()
a=int(a)
b=int(b)
c=int(c)
if(a<b+c and b<a+c and c<a+b):
    if(a==b and b==c):
        print("The triangle is equilateral")
    elif(a==b or a==c or c==b):
        print("The triangle is isosceles")
    else:
        print("The triangle is scalene")
else:
    print("Enter valid sides")