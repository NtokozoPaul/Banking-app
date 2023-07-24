def get_balance():
    with open("Bank Data.txt", "r") as file:
        balance = float(file.read())
    return balance

def update_balance(new_balance):
    with open("Bank Data.txt", "w") as file:
        file.write(str(new_balance))


def make_deposit(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("You provided an invalid input.")
        return

    current_balance = get_balance()
    new_balance = current_balance + amount
    update_balance(new_balance)
    log_transaction("Deposit", amount)
    print("Deposit successful.")


def make_withdrawal(amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("You provided an invalid input.")
        return

    current_balance = get_balance()
    if current_balance < amount:
        print("Insufficient funds.")
        return

    new_balance = current_balance - amount
    update_balance(new_balance)
    log_transaction("Withdrawal", amount)
    print("Withdrawal successful.")

def log_transaction(transaction_type, amount):
    with open("Transaction Log.txt", "a") as file:
        file.write(f"{transaction_type}: {amount}\n")


def main():
    print("Welcome to the Banking Application!")

    while True:
        choice = input("Would you like to make a transaction? (Enter the corresponding number)\n1. Yes\n2. No\n")

        if choice == "2":
            break

        if choice == "1":
            transaction_type = input("Would you like to make a deposit or withdrawal? (Enter the corresponding number)\n1. Deposit\n2. Withdrawal\n")

            if transaction_type == "1":
                amount = input("How much would you like to deposit? ")
                make_deposit(amount)
            elif transaction_type == "2":
                amount = input("How much would you like to withdraw? ")
                make_withdrawal(amount)
            else:
                print("You provided an invalid input.")
                continue

        current_balance = get_balance()
        print(f"Current balance: {current_balance}")

    print("Thank you for using the Banking Application!")

if __name__ == "__main__":
    main()
