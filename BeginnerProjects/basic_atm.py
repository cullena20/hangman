class Atm:

    def __init__(self, balance, number, pin):
        self.pin = pin
        self.number = number
        self.balance = balance
        self.change_money = []  # list needed to get integer for money deposited / withdraw (is there a better way?)
        self.check_pin = []  # eh list needed to check card number and pin

    def get_int(self, action):  # function to ask for an integer value and loop if a string is given instead
        self.change_money.clear()  # need to clear this list to make it work again (is there a better way?)
        while True:
            try:
                if action == "withdraw":
                    money = float(input(f"How much do you want to {action}?\n"))
                    if money > self.balance:
                        print("You can't withdraw that much!")
                        continue
                    else:
                        self.change_money.append(money)
                elif action == "deposit":
                    money = float(input(f"How much do you want to {action}?\n"))
                    self.change_money.append(money)
                elif action in ["card number", "pin"]:
                    money = int(input(f"What is your {action}?\n"))
                    self.check_pin.append(money)
            except ValueError:
                print("Sorry, I did not understand that.")
                continue
            else:
                break
                # feels like a mess

    def display(self):
        print("Current Balance: $", self.balance)

    def deposit(self):
        self.get_int("deposit")
        self.balance += self.change_money[0]
        print("Deposited: $", self.change_money[0])
        print("Current Balance: $", self.balance)

    def withdraw(self):
        self.get_int("withdraw")
        self.balance -= self.change_money[0]
        print("Withdrawn: $", self.change_money[0])
        print("Current Balance: $", self.balance)

    def run_raw(self):  # building inside out. runs main part of atm
        print('''Select your desired action:
        Display
        Deposit
        Withdraw''')
        while True:
            action = input().casefold()
            if action == "display":
                self.display()
                break
            elif action == "deposit":
                self.deposit()
                break
            elif action == "withdraw":
                self.withdraw()
                break
            else:
                print("Sorry, I didn't understand that.")
                continue

    def loop(self):  # allows program to loop if yes is answered
        while True:
            print("Would you like to do anything else?")
            answer = input()
            if answer.casefold() == "yes":
                self.run_raw()
            elif answer.casefold() == "no":
                print("Have a good day! :)")
                break
            else:
                print("Sorry, I did not understand that.")
                continue

    def run_machine(self):  # main function putting it all together and checking the number and pin
        self.get_int("card number")
        self.get_int("pin")
        if self.check_pin[0] == self.number and self.check_pin[1] == self.pin:
            self.run_raw()
            self.loop()
        else:
            print("Wrong pin!")


patrick_atm = Atm(1000, 1234, 5678)  # balance is 1000, card number is 1234, pin is 5678

patrick_atm.run_machine()

# one of the first projects I did but updated after finishing coffee machine
