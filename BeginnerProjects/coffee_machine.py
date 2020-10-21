class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.new_material = []  # only way i could figure out to have get_integer function to be used to fill

    def print_state(self):
        print(f'''\nThe coffee machine has:
    {self.water} of water
    {self.milk} of milk
    {self.beans} of coffee beans
    {self.cups} of disposable cups
    ${self.money} of money\n''')

    def adjust_resources(self, water_needed, milk_needed, beans_needed, new_money):
        self.water -= water_needed
        self.milk -= milk_needed
        self.beans -= beans_needed
        self.cups -= 1
        self.money += new_money

    def how_buy(self, water_needed, milk_needed, beans_needed, new_money):
        possible = True
        if water_needed > self.water:
            print("Sorry, not enough water!")
            possible = False
        if milk_needed > self.milk:
            print("Sorry, not enough milk!")
            possible = False
        if beans_needed > self.beans:
            print("Sorry, not enough beans!")
            possible = False
        if 1 > self.cups:
            print("Sorry, not enough cups!")
            possible = False
        if possible:
            print("I have enough resources, making you a coffee!")
            self.adjust_resources(water_needed, milk_needed, beans_needed, new_money)

    def buy(self):
        while True:
            coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n").casefold()
            if coffee_type in ["1", "espresso"]:
                self.how_buy(250, 0, 16, 4)  # espresso takes 250 ml water, 0 ml milk, 16 grams coffee beans, and costs 4 dollars
                break
            elif coffee_type in ["2", "latte"]:
                self.how_buy(350, 75, 20, 7)  # latte takes 350 ml water, 75 ml milk, 20 grams coffee beans, and costs 7 dollars
                break
            elif coffee_type in ["3", "cappuccino"]:
                self.how_buy(200, 100, 12, 6)  # cappuccino takes 200 ml water, 100 ml milk, 12 grams coffee beans, and costs 6 dollars
                break
            elif coffee_type == "back":
                break
            else:
                print("Sorry, I did not understand that.:\n")
                continue
        print()

    def get_integer(self, new_material):
        while True:
            try:
                new_material = int(input(f"Write how many {new_material} you want to add:\n"))
                self.new_material.append(new_material)
            except ValueError:
                print("Sorry, I did not understand that.\n")
                continue
            else:
                break

    def fill(self):
        self.new_material.clear()  # this list needs to be cleared everytime fill is ran
        self.get_integer("ml of water")
        self.water += self.new_material[0]
        self.get_integer("ml of milk")
        self.milk += self.new_material[1]
        self.get_integer("grams of coffee beans")
        self.beans += self.new_material[2]
        self.get_integer("disposable cups")
        self.cups += self.new_material[3]
        print()

    def take(self):
        print(f"I gave you ${self.money}\n")
        self.money = 0

    def run_machine(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n").casefold()
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.print_state()
            elif action == "exit":
                break
            else:
                print("Sorry, I did not understand that.\n")
                continue


my_machine = CoffeeMachine(400, 540, 120, 9, 550)
# my_machine starts with 400 ml of water, 540 ml of milk,
# 120 grams of coffee beans, 9 disposable cups, and $550

my_machine.run_machine()

# my main first project. followed JetBrains Academymg
