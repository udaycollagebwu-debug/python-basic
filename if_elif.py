# calculate the grade of a student based on the marks obtained
mark1 = int(input("Enter the marks obtained in the first subject :"))
mark2 = int(input("Enter the marks obtained in the second subject :"))
mark3 = int(input("Enter the marks obtained in the third subject :"))
average = float(mark1 + mark2 + mark3) / 3
if average >= 90:
    print("You got an A+ grade'GOOD JOB'")
elif average >= 80:
    print("You got an A grade'GOOD JOB'")
elif average >= 70:
    print("You got a B grade'GOOD JOB'")
elif average >= 60:
    print("You got a C grade'GOOD JOB'")
elif average >= 50:
    print("You got a D grade'GOOD JOB'")
else:
    print("You got an F grade'BETTER LUCK NEXT TIME'")
print("Your average marks are :", average)
