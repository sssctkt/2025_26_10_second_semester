"""
Task: I want to ask ppl's mark
80-100 (inclusive) A 
70-79  B 
60-69  C 
50-59  D 
Fail   E 
Assume the user will enter the correct input 
"""
mark=int(input("Enter your mark: "))
if(mark>=80 and mark<=100):
    print("Congratulations!")
    print("You got an A!")
if(mark>=70 and mark<=79):
    print("Good Job!")
    print("You got a B!")
if(mark>=60 and mark<=69):
    print("You got a C")
    print("That's okay")
if(mark>=50 and mark<=59):
    print("Nice try")
    print("You got a D")
else:
    print("E")
    
    