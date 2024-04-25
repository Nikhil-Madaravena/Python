# To print the sum of the series 1 + 12 + 123 + 1234....
n=input("Enter the number of terms : ")
n=int(n)
i=1
j=1
k=2
while i<=n:
    print(str(j),end=" ")
    if i<n:
        print("+",end=" ")
    j=int(j)
    if k<10:
        j=j*10+k
    elif k<100:
        j=j*100+k
    k=k+1
    i=i+1
