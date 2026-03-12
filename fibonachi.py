num=int(input("Enter the number of terms of the fibonacci series you want to print : "))
a=0
b=1
print("The fibonacci series is :")
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c
    