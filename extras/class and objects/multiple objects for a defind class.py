''' write a python program to create multiple objects for a defind class
by using parameterized constructor:-'''
class me:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print(f"name={self.name}")
        print(f"age={self.age}")
        print(f"address={self.address}")
#object creation :-
me1=me("lallu",5,'house')
print("detais of me1:-")
me1.display()
me2=me("lalith",19,'earth')
print("detais of me2:-")
me2.display()
me3=me(input("Enter me3 details : "),input(),input())
print("detais of me3:-")
me3.display()
