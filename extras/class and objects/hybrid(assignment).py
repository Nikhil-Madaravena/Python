class person:
    def __init__(plp,name,age):
        plp.name=name
        plp.age=age
    def d1(plp):
        print("name :-",plp.name)
        print("age:-",plp.age)
class employe(person):
    def __init__(plp,name,age,id):
        person.__init__(plp,name,age)
        plp.id=id
    def d2(plp):
        print("empoly id :-",plp.id)
class customer(person):
    def __init__(plp,name,age,amount):
        person.__init__(plp,name,age)
        plp.amount=amount
    def d2_1(plp):
        print("the bill amount of customer:-",plp.amount)
class faculty(employe):
    def __init__(plp,name,age,id,designation):
        employe.__init__(plp,name,age,id)
        plp.designation=designation
    def d3(plp):
        print("the designation of faculty:-",plp.designation)
class devloper(employe):
    def __init__(plp,name,age,id,pl):
        employe.__init__(plp,name,age,id)
        plp.pl=pl
    def d4(plp):
        print("the programing language used by the developer:-",plp.pl)
print("______________________________________________________________________________________________________________")
print("details of person:-")
print("-----------------------------")
p=person("Nikhil",17)
p.d1()
print("_______________________________________________________________________________________________________________")
print("")
print("________________________________________________________________________________________________________________")
print("details of employs:-")
print("-----------------------------")
e=employe("Nikhil",17,240106)
e.d1()
e.d2()
print("________________________________________________________________________________________________________________")
print("")
print("________________________________________________________________________________________________________________")
print("details of faculty:-")
print("-----------------------------")
f=faculty("Akshay",19,240804,"ass.prof")
f.d1()
f.d3()
print("________________________________________________________________________________________________________________")
print("")
print("________________________________________________________________________________________________________________")
print("details of developer:-")
print("-----------------------------")
d=devloper("Nikhil",17,240106,"python")
d.d1()
d.d4()
print("________________________________________________________________________________________________________________")
print("")
print("________________________________________________________________________________________________________________")
print("details of customer:-")
print("-----------------------------")
c=customer("Nikhil",17,5000)
c.d1()
c.d2_1()
print("________________________________________________________________________________________________________________")
