from itertools import count


class Account:
    accounts = {}
    counter = count(start=1)

    def __init__(self, fullname, balance, pin):
        self.fullname = fullname
        self.balance = balance
        self.pin = pin

        self.account_number = next(self.counter)

        self.accounts[self.account_number] = self

        # fullname and balance are passed to the object instance, so self. is not required to access them inside __init__
        print(
            f"Hi, {fullname}! Your account has been created with balance {balance}.")
        print(f"Your account number is {self.account_number}\n")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
        else:
            print("\nIncorrect PIN!")

    # __str__ is one of the dunder or magic methods
    # Dunder = Double underscores
    def __str__(self):
        # It is called when the print() or str() function is invoked
        return (f"Account number: {self.account_number}\n"
                f"Name: {self.fullname}\n"
                f"Balance: {self.balance}")

    def transfer(self, sender_pin, receiver_acc_num, amount):
        actual_sender_pin = self.pin
        sender_acc_num = self.account_number
        sender_balance = self.balance

        # Assignment: Put a validation to check own account
        if sender_acc_num == receiver_acc_num:
            print("\nYou can't transfer money to your own account!")
            return

        # The receiver is other than the sender
        if sender_pin != actual_sender_pin:
            print("\nPin doesn't match!")
            return

        # PIN matches
        receiver = self.accounts.get(receiver_acc_num)
        if not receiver:
            print(f"\nAccount number {receiver_acc_num} doesn't exist!")
            return

        # Receiver exists
        if sender_balance < amount:
            print("\nInsufficient balance!")
            return

        # Decrease the sender's balance and increase the receiver's balance
        self.balance -= amount
        receiver.balance += amount

        print("\nTransaction details:")
        print(f"From account number: {sender_acc_num}")
        print(f"To account number: {receiver_acc_num}")
        print(f"Transfer amount: {amount}")
        print(f"Your new balance: {self.balance}")


if __name__ == "__main__":
    print("Account Instantiations:")
    account1 = Account("Linus Torvalds", 1500, "6174")
    account2 = Account(pin="0153", balance=2500, fullname="Dennis Ritchie")

    # Accessing the properties (or attributes) outside of the class definition
    print(f"Account number of Guido: {account1.account_number}")
    print(f"Balance of Dennis: {account2.balance}")

    print("\nBefore money transfer:")
    print(account2)  # Call the __str__ dunder method

    # Call the transfer method on object account1
    account1.transfer(sender_pin="6174", receiver_acc_num=2, amount=1200)

    print("\nAfter money transfer -- Accounts database:")
    # Print the first account by printing the first object (call __str__)
    print(Account.accounts.get(next(iter(Account.accounts))))

    # Print remaining accounts
    for acc_num in dict(list(Account.accounts.items())[1:]):
        print()  # For linebreak
        print(Account.accounts.get(acc_num))  # Print the object (call __str__)
