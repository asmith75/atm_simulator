def read_initial_balance(filename="Projcet_read.txt"):
    try:
        with open(filename, 'r') as file:
            balance = float(file.read().strip())
            return balance
    except FileNotFoundError:
        print(f"{filename} not found. Using default balance of $5000.")
        return 5000.0
    except ValueError:
        print(f"Invalid balance in {filename}. Using default balance of $5000")
        return 5000.0
    
def write_final_balance(balance, filename="Smith_project.txt"):
    with open(filename, 'w') as file:
        file.write(f"Final balance: {balance:.2f}")

def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    if amount <= 0:
        print("Deposit must be positive number.")
    else:
        balance += amount
        print(f"Deposit successful. New balance ${balance:.2f}")
    return balance

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= 0:
        print("Withdrawal amount must be a positive number.")
    elif amount > balance:
        print("Insufficient balance, withdrawal failed.")
    else:
        balance -= amount
        print(f"Withdrawal successful. New balance: ${balance:.2f}")
        if balance < 100:
            print("Your balance is now below $100.")
    return balance

def balance_inquiry(balance):
    print(f"WARNING: Your current balance is: ${balance:.2f}")

def atm_menu():
    balance = read_initial_balance()  # Corrected this line
    choice = 0
    while choice != 4:
        print("\nATM Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4):"))
        if choice == 1:
            balance = deposit(balance)
        elif choice == 2:
            balance = withdraw(balance)
        elif choice == 3:
            balance_inquiry(balance)
        elif choice == 4:
            write_final_balance(balance)
            print("Thank you for choosing our ATM")
        else:
            print("Invalid choice number, Please enter a number between 1-4.")

if __name__ == "__main__":
    atm_menu()
