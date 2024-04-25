Names = input("Enter student's name : ")
roll_no = int(input("Enter student's rno : "))
m_marks = int(input("Enter marks of Maths subject : "))
phy_marks = int(input("Enter marks of Physics subject : "))
chem_marks = int(input("Enter marks of Chemistry subject: "))
def my_fun(Names, roll_no, m_marks, phy_marks, chem_marks):
    total = m_marks + phy_marks + chem_marks
    avg = total/3
    if m_marks <= 0 or phy_marks <= 0 or chem_marks <=0 :
        print("Invalid marks, Error")
    else:
        if avg >= 70:
            print("Student got District marks")
        elif 60 <= avg > 70:
            print("Student got First Class marks")
        elif 50 <= avg > 60:
            print("Student got Second Class marks")
        else:
            print("Student is Fail")
my_fun(Names, roll_no, m_marks, phy_marks, chem_marks)