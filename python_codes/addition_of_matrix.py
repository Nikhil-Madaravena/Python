def matrix(r,c):
    o=[]
    for i in range(r):
        row=[]
        for j in range(c):
            row.append(int(input(f"element[{i}][{j}]=")))
        o.append(row)
    return o
r=int(input("no of rows="))
c=int(input("no of colomns="))
a=matrix(r,c)
print(" first is matrix  is {a}")
b=matrix(r,c)
print(" second is matrix  is {b}")
def sum(a,b):
    #c1=[[0,0],[0,0]]
    c1=[]
    for i in range(r):
        for j in range(c):
            c1[i][j]=a[i][j]+b[i][j]
    return c1
print(f"the sum of a {a} and b{b} is :{sum(a,b)}")


