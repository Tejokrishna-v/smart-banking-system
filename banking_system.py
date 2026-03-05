import json
from datetime import datetime


class BankAccount:
    bank_name = "Tejo krishna international bank"

    def __init__(self, account_number, name, balance=0, transactions=None):
        self.account_number = account_number
        self.name = name
        self.__balance = balance
        self.transactions = transactions if transactions else []

    def get_balance(self):
        return self.__balance

    def add_transaction(self, action, amount):
        self.transactions.append({
            "action": action,
            "amount": amount,
            "time": str(datetime.now())
        })

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.add_transaction("Deposit", amount)
            print(f" Deposited: {amount}")
        else:
            print(" Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.add_transaction("Withdraw", amount)
            print(f" Withdrawn: {amount}")
        else:
            print(" Insufficient or invalid amount")

    def show_transactions(self):
        print("\n---- Transaction History ----")
        if not self.transactions:
            print("No transactions yet")
        else:
            for t in self.transactions:
                print(f"{t['time']} | {t['action']} | {t['amount']}")

    def display(self):
        print("\n------ Account Details ------")
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Account No: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.__balance}")

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.__balance,
            "transactions": self.transactions,
            "type": "BankAccount"
        }


class SavingsAccount(BankAccount):
    def __init__(self, account_number, name, balance=0, interest_rate=0.05, transactions=None):
        super().__init__(account_number, name, balance, transactions)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f" Interest Added: {interest}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "SavingsAccount"
        data["interest_rate"] = self.interest_rate
        return data


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account):
        if account.account_number in self.accounts:
            print(" Account already exists")
        else:
            self.accounts[account.account_number] = account
            print(" Account Created Successfully")

    def delete_account(self, acc_no):
        if acc_no in self.accounts:
            del self.accounts[acc_no]
            print(" Account Deleted")
        else:
            print(" Account not found")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def save_data(self, filename="bank_data.json"):
        data = {acc_no: acc.to_dict() for acc_no, acc in self.accounts.items()}
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(" Data Saved Successfully")

    def load_data(self, filename="bank_data.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            for acc_no, details in data.items():

                if details["type"] == "SavingsAccount":
                    account = SavingsAccount(
                        details["account_number"],
                        details["name"],
                        details["balance"],
                        details.get("interest_rate", 0.05),
                        details.get("transactions", [])
                    )
                else:
                    account = BankAccount(
                        details["account_number"],
                        details["name"],
                        details["balance"],
                        details.get("transactions", [])
                    )

                self.accounts[acc_no] = account

            print(" Data Loaded Successfully")

        except FileNotFoundError:
            print("⚠ No previous data found")


def main():

    bank = BankSystem()
    bank.load_data()

    while True:

        print("\n===== SMART BANKING SYSTEM =====")
        print("1 Create Account")
        print("2 Deposit")
        print("3 Withdraw")
        print("4 Check Balance")
        print("5 Add Interest (Savings)")
        print("6 Transaction History")
        print("7 Delete Account")
        print("8 Save & Exit")

        choice = input("Enter choice: ")

        try:

            if choice == "1":
                acc_no = input("Account Number: ")
                name = input("Customer Name: ")
                acc_type = input("Account Type (normal/savings): ")

                if acc_type.lower() == "savings":
                    account = SavingsAccount(acc_no, name)
                else:
                    account = BankAccount(acc_no, name)

                bank.create_account(account)

            elif choice == "2":
                acc_no = input("Account Number: ")
                amount = float(input("Amount: "))
                account = bank.get_account(acc_no)

                if account:
                    account.deposit(amount)
                else:
                    print(" Account not found")

            elif choice == "3":
                acc_no = input("Account Number: ")
                amount = float(input("Amount: "))
                account = bank.get_account(acc_no)

                if account:
                    account.withdraw(amount)
                else:
                    print(" Account not found")

            elif choice == "4":
                acc_no = input("Account Number: ")
                account = bank.get_account(acc_no)

                if account:
                    account.display()
                else:
                    print(" Account not found")

            elif choice == "5":
                acc_no = input("Account Number: ")
                account = bank.get_account(acc_no)

                if isinstance(account, SavingsAccount):
                    account.calculate_interest()
                else:
                    print(" Not a savings account")

            elif choice == "6":
                acc_no = input("Account Number: ")
                account = bank.get_account(acc_no)

                if account:
                    account.show_transactions()
                else:
                    print(" Account not found")

            elif choice == "7":
                acc_no = input("Account Number: ")
                bank.delete_account(acc_no)

            elif choice == "8":
                bank.save_data()
                print(" Thank you for using Tejo krishna international bank ")
                break

            else:
                print(" Invalid choice")

        except Exception as e:
            print("⚠ Error:", e)


if __name__ == "__main__":

    main()
