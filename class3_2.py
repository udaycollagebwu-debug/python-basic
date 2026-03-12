# Write a Python program that asks the user to enter CGPA and then prints the placement chances. 
#If CGPA is greater than or equal to 8 print High placement chances. If CGPA is between 6 and 8 
#print Average placement chances. If CGPA is less than 6 print Low placement chances.

cgpa = float(input("Enter your CGPA :"))
if cgpa >= 8:
    print("High placement chances")
elif cgpa >= 6 and cgpa < 8:
    print("Average placement chances")
else:
    print("Low placement chances")
