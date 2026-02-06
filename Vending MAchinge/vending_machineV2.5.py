itmA = 1.20
itmB = 0.60
itmC = 0.75

coins = [200, 100, 50, 20, 10, 5]

print("Welcome to the vending machine.")
while True:
    item = input("What do you wish to purchase? Item A, B or C ").upper()

    if item == "A":
        cost = itmA
        name = "Item A"
        break
    elif item == "B":
        cost = itmB
        name = "Item B"
        break
    elif item == "C":
        cost = itmC
        name = "Item C"
        break
    else:
        print("NOOO VAYYYY try again")
        continue

money = float(input("How much money did you put into the machine? "))

cost = cost * 100
money = money * 100

if money < cost:
    print(f"You don't have enough money to purchase {name}. You need ${(cost - money)/100:.2f} more.")
    money += float(input("How much more money do you wish to add to the machine? ")) * 100

change = money - cost

if money == cost:
    print(f"You have paid exactly for {name}. Thank you!")
else:
    print(f"You have received ${change/100:.2f} change.")
    print("Change dispensed in:")

    for coin in coins:
        count = change // coin
        if count > 0:
            print(f"{int(count)} x ${coin/100:.2f}")
            change -= count * coin
