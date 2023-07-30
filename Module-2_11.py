n = int(input("Enter a positive integer n: "))

sumnum = 0

for i in range(1, n + 1):
    sumnum += i

print(f"The sum of the first {n} positive integers is: {sumnum}")
