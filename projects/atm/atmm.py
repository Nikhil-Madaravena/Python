import atmm_module as userdata

# Function to withdraw money
def withdraw(user):
    amount = int(input("Enter the amount to be withdrawn: "))
    current_balance = user.get_balance()

    if current_balance < 1000:
        print("Insufficient funds. Your balance is below the minimum required.")
        return

    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        return withdraw(user)

    if amount > current_balance:
        print("Insufficient funds. Cannot withdraw more than the available balance.")
        return withdraw(user)

    if current_balance - amount < 1000:
        print("You cannot withdraw all the amount.")
        print("According to bank rules, you have to maintain a minimum balance of 1000.")
        print("Please try again.")
        return withdraw(user)

    new_balance = current_balance - amount
    user.update_balance(-amount)
    print(f"You have successfully withdrawn {amount} from your account.")
    print(f"Your present bank balance is {new_balance}")

# Function to deposit money
def deposit(user):
    amount = int(input("Enter amount to be deposited to your account: "))
    if amount > 0:
        user.update_balance(amount)
        new_balance = user.get_balance()
        print(f"Your present bank balance is {new_balance}")
    else:
        print("Invalid amount. Please enter a positive value.")
        return deposit(user)

# Function to display user details
def display(user):
    user_details = user.get_user_details()
    print("|------------------------|")
    print("|   Your details are:    |")
    print("|------------------------|")
    for key, value in user_details.items():
        print(f"{key.capitalize()}: {value}")
    print("|------------------------|")

# Function to change PIN
def pin_change(user):
    old_pin = input("Enter your old PIN: ")
    if old_pin == user.get_pin():
        new_pin = input("Enter your new PIN: ")
        if len(new_pin) == 6:
            user.change_pin(new_pin)
            print("PIN change successful.")
        else:
            print("Please enter a 6-digit numeric PIN.")
    else:
        print("Incorrect old PIN. Please try again.")

# Main ATM interface
print("Welcome to Automated Teller Machine Services ")
print("____________________________________________")

user_data = userdata.UserData()
user_data.input_user_data()  # Takes user inputs

attempts = 0
while attempts < 5:
    account_number = int(input("Enter your account number: "))
    if user_data.get_account_number() == account_number:
        pin_attempts = 0
        while pin_attempts < 3:
            entered_pin = input("Enter your PIN: ")
            if user_data.get_pin() == entered_pin:
                choice = int(input("Choose the required options:\n1. Know your details\n2. Withdraw cash\n3. Deposit\n4. Change your PIN\nEnter your choice: "))
                if choice == 1:
                    display(user_data)
                elif choice == 2:
                    withdraw(user_data)
                elif choice == 3:
                    deposit(user_data)
                elif choice == 4:
                    pin_change(user_data)
                else:
                    print("Invalid choice. Please select a valid option.")
                break
            else:
                pin_attempts += 1
                if pin_attempts < 3:
                    print("Incorrect PIN. Please try again.")
                else:
                    print("Exceeded maximum attempts for PIN.")
                    break
        else:
            print("Exceeded maximum attempts. Please go to your bank and get your details.")
            break
    else:
        print('Invalid account number. Please try with the correct one.')
        attempts += 1
else:
    print("You have used 5 attempts. Please go to your bank and get your details.")