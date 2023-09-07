# if condition1 & condition2 & condition3:
#     do this
# else:
#     do this 

## Logical Operators
# A and B
# C 0r D
# not E

print("Welcome to the Cinema!")
age = int(input("What is your age?"))
if age < 12:
    bill = 500
    print("Child tickets are Ksh500.")
elif age <= 18:
    bill = 700
    print("Youth tickets are Ksh700.")
elif age >= 45 and age <= 55:
    print("Everything is going to be ok.Enjoy the show!")
else:
    bill = 1200
    print("Adult tickets are Ksh1200.")

wants_photo = input("Do you want a photo taken? Y or N.")
if wants_photo == "Y":
   # Add Ksh300 to their bill 
   bill += 300

print(f"Your final bill is {bill}")