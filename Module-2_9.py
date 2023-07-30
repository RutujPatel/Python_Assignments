# Get input for three integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Check if any two values are equal
if num1 == num2 or num1 == num3 or num2 == num3:
    sumnum = 0
else:
    sumnum = num1 + num2 + num3

print("Sum of the three integers:", sumnum)
