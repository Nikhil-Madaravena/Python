import quiz_module as qm
c=0
for i in range(1,11):
    print(f"{i})question")
    print("1st option")
    print("2nd option")
    print("3rd option")
    print("4th option")
    result=int(input("enter the correct option number:"))
    if result== qm.q[i]:
        c+=1
if 0<=c<=5:
    print(f"your score is {c} marks, so less please take your test again")
elif 5<c<8:
    print(f"your score is {c} marks, thats a great score good luck for next test")
else:
    print(f"your score is {c} marks,thats a wonderfull score i hope u show this in the nest exam too")
    
