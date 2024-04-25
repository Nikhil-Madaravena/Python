c=input("enter the colour code:-")
def colour(c):
    if c=='b':
        col="blue"
    elif c=='p':
        col="pink"
    elif c=='r':
        col="red"
    elif c=='g':
        col="green"
    elif c=='o':
        col="orange"
    else:
        col="no colour"
    return(col)
print("colour is",colour(c))
