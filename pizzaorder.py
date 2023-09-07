print("Welcome to PizzaSlut deliveries!")

size = input("What size pizza do you want? S, M, or L")

add_pepperoni = input("Do you want pepperoni? Y or N")

extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0

if size == "S":
    bill += 1500
elif size == "M":
    bill += 2000
else:
    bill += 2500

    if add_pepperoni == "Y":
        if size == "S":
            bill += 200
        else:
            bill += 300

    if extra_cheese == "Y":
       bill += 100

print(f"Your final bill is: Ksh{bill}.") 
