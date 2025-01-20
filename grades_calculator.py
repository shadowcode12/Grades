name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
grade = ""

if marks >= 90:
    grade = "A+"

elif marks >= 80:
    grade = "A"

elif marks >= 70:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 40:
    garde = "D"

else:
    grade = "F"
    print("You are Failed, Better luck next time")

print(f"Hello! My name is {name}, and my marks is {marks} and my grade is {grade}")
