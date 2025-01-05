
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def get_balance(self):
        return self.balance

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")

def main():
    accounts = {}

    while True:
        print("\nWelcome to the Bank")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display Account Details")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder's name: ")
            if account_number in accounts:
                print("Account number already exists. Please try again.")
            else:
                accounts[account_number] = BankAccount(account_number, account_holder)
                print("Account created successfully.")
        
        elif choice == '2':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found. Please try again.")
        
        elif choice == '3':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found. Please try again.")
        
        elif choice == '4':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                balance = accounts[account_number].get_balance()
                print(f"Current balance: ${balance:.2f}")
            else:
                print("Account not found. Please try again.")
        
        elif choice == '5':
            account_number = input("Enter account number: ")
            if account_number in accounts:
                accounts[account_number].display_details()
            else:
                print("Account not found. Please try again.")
        
        elif choice == '6':
            print("Thank you for using the bank. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()