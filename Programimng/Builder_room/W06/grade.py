marks = int(input("Enter your Marks: "))
if marks > 90 and marks <=100:
    grade = "A"
elif marks > 80:
    grade = "B"
elif marks > 70:
    grade = "C"
elif marks > 60:
    grade = "D"
elif marks > 50:
    grade = "E"
else: 
    grade = "F"

print("Your Grade is:",grade)