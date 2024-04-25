''' read a 3x3 matrix dynamicaly, find max and min elements and print the same
on to the screen'''
def matrix(r,c):
    o=[]
    for i in range(3):
        row=[]
        for j in range(3):
            row.append(int(input(f"element[{i}][{j}]=")))
        o.append(row)
    return o
a=matrix(3,3)
big=0
small=a[0][0]
for i in range(3):
    for j in range(3):
        if a[i][j]>big:
            big=a[i][j]

for i in range(3):
    for j in range(3):
        if a[i][j]<small:
            small=a[i][j]

print(f" the  maximum value in the matrix is {big}")
print(f" the  minumum value in the matrix is {small}")
