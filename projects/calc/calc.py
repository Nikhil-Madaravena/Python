import calc_mod as ca
a=int(input("Enter 1st number : "))
ope=input("Enter operator(+,-,*,/,//,%,^) : ")
b=int(input("Enter 2nd number : "))
if ope=="+":
    ca.add(a,b)
elif ope=="-":
    ca.sub(a,b)
elif ope=="*":
    ca.product(a,b)
elif ope=="/":
    ca.div(a,b)
elif ope=="//":
    ca.f_div(a,b)
elif ope=="%":
    ca.m_div(a,b)
elif ope=="^":
    ca.powe(a,b)
else:
    print("Invalid Input")