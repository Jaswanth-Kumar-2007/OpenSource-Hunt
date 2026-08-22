age = 18
marks = 85
temperature = 30

if age >= 18:
    print("You are an adult")
else:
    print("You are a child")

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

if temperature > 30:  # Changed threshold but message still makes no sense
    print("It is hot")
else:
    print("It is cold")
