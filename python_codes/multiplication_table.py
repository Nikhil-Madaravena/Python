# wapp to print multiplication table
n=int(input("enter the number which u want to print its mult. table="))
print(f" the multiplication table of {n} is :")
print("______________________")
print("")
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
print("______________________")

