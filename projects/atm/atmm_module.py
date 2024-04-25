class UserData:
    def __init__(self):
        self.data = {}

    def input_user_data(self):
        self.data['name'] = input("Enter your name: ")
        self.data['ac_no'] = int(input("Enter your account number: "))
        self.data['balance'] = float(input("Enter your initial balance: "))  
        self.data['pin'] = input("Enter your PIN (6 digits): ")
        self.data['mobile_no'] = input("Enter your mobile number: ")
        self.data['address'] = input("Enter your address: ")

    def get_account_number(self):
        return self.data.get('ac_no')

    def get_pin(self):
        return self.data.get('pin')

    def change_pin(self, new_pin):
        if len(new_pin) == 6:
            self.data['pin'] = new_pin
            return True
        else:
            return False

    def get_balance(self):
        return self.data.get('balance')

    def update_balance(self, amount):
        self.data['balance'] += amount

    def get_user_details(self):
        return {
            "name": self.data.get("name"),
            "ac_no": self.data.get('ac_no'),
            "balance": self.data.get('balance'),
            "mobile_no": self.data.get('mobile_no'),
            "address": self.data.get('address')
        }
