def matrix(m,n):
    o=[]
    for i in range(m):
        row=[]
        for j in range(n):
            row.append(int(input("a"+str(i)+str(j)+"=")))
        o.append(row)
    return o
m=int(input("m="))
n=int(input("n="))

print(matrix(m,n))
