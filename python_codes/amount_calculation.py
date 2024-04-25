#5
item_name=input("enter the name of item:")
item_amount=float(input("enter the amount of the item:"))
sgst=float(input("enter the rate of SGST:"))
cgst=float(input("enetr the rate of CGST:"))
gst=(sgst+cgst)*item_amount/100
total=item_amount+gst
print("the total payable amount of ",item_name,"is:",total) 
