#Nested if / else
#if condition:
#   if another condition:
#       do this
#   else:
#       do this:
#else:
#    do this

print("Welcome to the Cinema!")
age = int(input("What is your age?"))
if age < 12:
    bill = 500
    print("Child tickets are Ksh500.")
elif age <= 18:
    bill = 700
    print("Youth tickets are Ksh700.")
else:
    bill = 1200
    print("Adult tickets are Ksh1200.")

wants_photo = input("Do you want a photo taken? Y or N.")
if wants_photo == "Y":
   # Add Ksh300 to their bill 
   bill += 300

print(f"Your final bill is {bill}")
