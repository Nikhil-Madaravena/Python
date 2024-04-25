def calculate_ticket_price(age):
    if age < 5:
        return 0
    elif 5 <= age <= 19:
        return 50
    elif 20 <= age <= 59:
        return 100
    else:
        return 10

def apply_discount(total_amount, payment_method):
    if payment_method == "cash":
        return total_amount * 0.97  # 3% discount for cash payment
    elif payment_method == "upi":
        return total_amount * 0.97  # 3% discount for UPI payment
    elif payment_method == "credit/debit card":
        return total_amount * 0.9   # 10% discount for credit/debit card
    elif payment_method == "net banking":
        return total_amount * 0.95  # 5% discount for net banking
    else:
        return total_amount

num_visitors = int(input("Enter the number of visitors: "))
visitor_names = []
total_bill = 0

print("\nNew Science Research Centre")
print("----------------------------")

for i in range(num_visitors):
    name = input(f"Enter the name of visitor {i + 1}: ")
    age = int(input(f"Enter age of visitor {i + 1}: "))
    ticket_price = calculate_ticket_price(age)
    total_bill += ticket_price
    visitor_names.append(name)

print("\nVisitor Names:")
for i, name in enumerate(visitor_names, start=1):
    print(f"Visitor {i}: {name}")

print("\nTotal Bill: Rs.", total_bill)

payment_method = input("Select payment method (cash/upi/credit/debit card/net banking): ").lower()
discounted_amount = apply_discount(total_bill, payment_method)

print("\nDiscounted Amount: Rs.", discounted_amount)

print("\nThank you for your visit!")
print("Please provide your feedback at newscience@feedback.com")
print("----------------------------")