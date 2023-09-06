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
    print("Please pay Ksh500.")
elif age <= 18:
    print("Please pay Ksh700.")
else:
    print("Please pay Ksh1200.")