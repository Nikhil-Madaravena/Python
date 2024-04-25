def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(int(input("a=")))
        o.append(row)
    return o
m=int(input("m="))
n=int(input("n="))
a=matrix(m,n)
t=[]
for i in range(m):
    for j in range(n):
        t[i][j]=a[j][i]
print(t)
