
account_data = {
    'name': 'Puneeth Madaravena',
    'acc_no': '1234567890',
    'pin': '2006',
    'balance': 100000000
}

# Function to read account holder details (name, acc_no, pin)
def read_account_details():
    name = input("Enter your name: ")
    acc_no = input("Enter your account number: ")
    pin = input("Enter your PIN: ")
    return name, acc_no, pin

# Function to verify account details
def verify_account(name, acc_no, pin):
    if name == account_data['name'] and acc_no == account_data['acc_no'] and pin == account_data['pin']:
        return True
    else:
        return False

# Function to display account details and menu
def display_menu():
    print("\n----------------------------------------------------------------------\n")
    print("Welcome, " + account_data['name'])
    print("Account Number: " + account_data['acc_no'])
    print("1. Display Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change PIN")
    print("5. Exit")

# Function to display account balance
def display_balance():
    print("Your balance is: $" + str(account_data['balance']))

# Function to deposit money
def deposit(amount):
    account_data['balance'] += amount
    print("Deposit successful. Your new balance is: $" + str(account_data['balance']))

# Function to withdraw money
def withdraw(amount):
    if amount <= account_data['balance']:
        account_data['balance'] -= amount
        print("Withdrawal successful. Your new balance is: $" + str(account_data['balance']))
    else:
        print("Insufficient funds")

# Function to change PIN
def change_pin(new_pin):
    account_data['pin'] = new_pin
    print("PIN changed successfully")

# Main ATM operation loop
while True:
    name, acc_no, pin = read_account_details()
    
    if verify_account(name, acc_no, pin):
        display_menu()
        choice = input("Enter your choice: ")
        print("\n----------------------------------------------------------------------\n")
        if choice == '1':
            display_balance()
            print("Thank you for using the ATM. Have a nice day!")
            print("\n----------------------------------------------------------------------\n")
            break
        elif choice == '2':
            amount = float(input("Enter the deposit amount: $"))
            deposit(amount)
            print("Thank you for using the ATM. Have a nice day!")
            print("\n----------------------------------------------------------------------\n")
            break
        elif choice == '3':
            amount = float(input("Enter the withdrawal amount: $"))
            withdraw(amount)
            print("Thank you for using the ATM. Have a nice day!")
            print("\n----------------------------------------------------------------------\n")
            break
        elif choice == '4':
            new_pin = input("Enter your new PIN: ")
            change_pin(new_pin)
            print("Thank you for using the ATM. Have a nice day!")
            print("\n----------------------------------------------------------------------\n")
            break
        elif choice == '5':
            print("Thank you for using the ATM. Have a nice day!")
            print("\n----------------------------------------------------------------------\n")
            break
        else:
            print("Invalid choice")
    else:
        print("Verification failed. Please try again.")
        print("\n----------------------------------------------------------------------\n")
