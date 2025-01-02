import random
def create_account(accounts):
    username = input("Enter a username: ")
    for account in accounts:
        if account["username"] == username:
            print("Username already exists. Please choose a different username.")
            return

    password = input("Enter a password: ")
    accounts.append({"username": username, "password": password, "balance": 0})
    print("Account created successfully!")

def deposit(accounts):
    username = input("Enter username: ")
    password = input("Enter password: ")

    for account in accounts:
        if account["username"] == username and account["password"] == password:
            amount = float(input("Enter deposit amount: "))
            account["balance"] += amount
            print(f"Deposited ${amount}. New balance: ${account['balance']}")
            return

    print("Invalid username or password.")

def withdraw(accounts):
    username = input("Enter username: ")
    password = input("Enter password: ")

    for account in accounts:
        if account["username"] == username and account["password"] == password:
            amount = float(input("Enter withdrawal amount: "))
            if amount > account["balance"]:
                print("Insufficient funds. Withdrawal canceled.")
            else:
                account["balance"] -= amount
                print(f"Withdrew ${amount}. New balance: ${account['balance']}")
            return

    print("Invalid username or password.")

def check_balance(accounts):
    username = input("Enter username: ")
    password = input("Enter password: ")

    for account in accounts:
        if account["username"] == username and account["password"] == password:
            print(f"Account balance: ${account['balance']}")
            return

    print("Invalid username or password.")

def reset_password(accounts):
    username = input("Enter username: ")
    for account in accounts:
        if account["username"] == username:
            verification_code = random.randint(1000, 9999)
            print(f"Verification code sent to your registered contact: {verification_code}")
            
            entered_code = int(input("Enter the verification code: "))
            if entered_code == verification_code:
                new_password = input("Enter your new password: ")
                account["password"] = new_password
                print("Password reset successfully!")
            else:
                print("Invalid verification code. Password reset canceled.")
            return
    
    print("Username not found.")

def main():
    accounts = []

    while True:
        print("\nBank Account System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Reset Password") 
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            create_account(accounts)

        elif choice == '2':
            deposit(accounts)

        elif choice == '3':
            withdraw(accounts)

        elif choice == '4':
            check_balance(accounts)

        elif choice == '5': 
            reset_password(accounts)

        elif choice == '6':
            print("Exiting the Bank Account System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()
