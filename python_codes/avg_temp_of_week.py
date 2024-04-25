mon=float(input("enter the temperature of monday:"))
tue=float(input("enter the temperature of tusday:"))
wed=float(input("enter the temperature of wednesday:"))
thu=float(input("enter the temperature of thusday:"))
fri=float(input("enter the temperature of friday:"))
sat=float(input("enter the temperature of saturday:"))
sun=float(input("enter the temperature of sunday:"))

avg=(mon+tue+wed+thu+fri+sat+sun)/7
print("the average temperature experanced in this week is :")
print("0.2f" % avg)