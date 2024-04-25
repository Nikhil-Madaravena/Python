def sum_avg(n1,n2):
    if n2==0 or n2<0 or n1<0:
        print("invalidinput, try angain with positive value.")
    else:
        sum=0
        c=0
        avg=0
        for i in range(n1,n2+1):
            sum+=i
            c+=1
        if c > 0:
            avg = sum/c
        else:
            avg = 0
        return sum,avg
n1=int(input("enter the lower limit:-"))
n2=int(input("enter the upper limit:-"))      
a=sum_avg(n1,n2)
print("the sum =",a[0],"and avg=",a[1])

 
