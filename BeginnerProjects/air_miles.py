import math

print("Air Miles Calculator!\n")

print("How much money did you spend this month? ")
money = input()
if money[0] == "$":
    money = int(money[1:])
else:
    money = int(money)

print('''
Who is is your level?
Bronze
Silver
Gold
Platinum
      ''')
provider = input()
if provider.casefold() == "bronze":
    miles_per_dollar = 0.5
elif provider.casefold() == "silver":
    miles_per_dollar = 1
elif provider.casefold() == "gold":
    miles_per_dollar = 1.5
elif provider.casefold() == "platinum":
    miles_per_dollar = 2
print("You get", miles_per_dollar, "miles per dollar")

miles_per_month = money * miles_per_dollar

print(''' 
Where do you want to go?
Paris
London
China
New Zealand''')
location = input()
if location.casefold() == "paris":
    miles_goal = 2 * 3700
elif location.casefold() == "london":
    miles_goal = 2 * 3400
elif location.casefold() == "china":
    miles_goal = 2 * 6900
elif location.casefold() == "new zealand":
    miles_goal = 2 * 9000

months_needed = math.ceil(miles_goal / miles_per_month)
print("You need", months_needed, "months to travel", miles_goal, "miles to", location.title(), "and back for free.")

# one of the first projects i did.
