#nested if statement
# I can have an if statement inside and if statement
# elif, else will follow the closest if 
# correct indentation is the key!!!

color=input("pick a color: red, blue, or white: ")
number=int(input("Enter a positive integer: "))

if (color=="red"):
    if (number%2==0):
        print("You pick the color red and even number")
        print("You must like stray kids")
    else:
        print("You pick the color red and odd number")
        print("You must like EXO")
elif (color=="blue"):
    if (number%2==0):
        print("You pick the color blue and even number")
        print("You must like Seventeen")
    else:
        print("You pick the color blue and odd number")
        print("You must like BTS")
else:
    if (number%2==0):
        print("You pick the color white and even number")
        print("You must like NCT 127")
    else:
        print("You pick the color white and odd number")
        print("You must like ATEEZ")        