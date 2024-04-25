a=input("enter a string:")
print(a)
li=a.split(" ")
for i in li:
    c=0
    for j in i:
        if c==0:    
        
            print(j.upper(),end="")
            c+=1
        else:
            print(j,end="")
    print(end=" ")
        
    
