numbers = [10, 5, 20, 30, 15]

if not numbers:
    largest_num = smallest_num = None
    sum_of_all = 0
else:
    largest_num = smallest_num = numbers[0]
    sum_of_all = 0

   
    for num in numbers:
        sum_of_all += num

        if num > largest_num:
            largest_num = num

        if num < smallest_num:
            smallest_num = num

print("Largest number:", largest_num)
print("Smallest number:", smallest_num)
print("Sum of all numbers:", sum_of_all)
