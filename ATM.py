class Account:
    def __init__(self,account_number, holder_name, balance):
        self.__account_number=account_number
        self.__holder_name=holder_name
        self.__balance=balance
        
    def deposit_money(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount}successfully deposited")
        else:
            print("amount will be positive value")
            
    def withdraw_money(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print(" No balance")
            
    def check_balance(self):
        return self.__balance
    
    def show_details(self):
        print("\n----- Account Details -----")
        print(f"Account Number: {self.__account_number}")
        print(f"Holder Name: {self.__holder_name}")
        print(f"Balance: ₹{self.__balance}")
        print("----------------------------")
        
class ATM(Account):
    def __init__(self, account_number, holder_name, balance,pin):
        super().__init__(account_number, holder_name, balance)
        self.__pin = pin
        
    def validate_pin(self,entered_pin):
        return entered_pin == self.__pin
        
    def show_details(self):
        print("\n----- Account Details -----")
        super().show_details()
        
atm_user = ATM("123456789", "Arathy", 5000, 1234)

entered_pin = int(input("Enter your ATM PIN: "))
# if atm_user.validate_pin(entered_pin):
#     atm_user.show_details()
#     atm_user.deposit_money(1000)
#     atm_user.withdraw_money(2000)
#     print("Balance: " ,atm_user.check_balance())
# else:
#     print("Incorrect PIN!")
if atm_user.validate_pin(entered_pin):
    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Show Account Details")
        print("5. Exit")
        choice = int(input('Enter your choice: '))
        
        if choice == 1:
            print(f"Current Balance : {atm_user.check_balance()}")
        elif choice == 2:
            amount = float(input('Enter deposit amount :'))
            atm_user.deposit_money(amount)
        elif choice == 3:
            amount = float(input('Enter withdraw amount :'))
            atm_user.withdraw_money(amount)
        elif choice == 4:
            atm_user.show_details()
        elif choice == 5:
            print("Thank you for using atm")
            break
        else:
            print("Invalid option")
else:
    print("INCORRECT PIN")