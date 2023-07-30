original_string = "Hello, world!"
string_to_insert = "Python"

middle_index = len(original_string) // 2

if len(original_string) % 2 == 0:
    new_string = original_string[:middle_index] + string_to_insert + original_string[middle_index:]
else:
    new_string = original_string[:middle_index + 1] + string_to_insert + original_string[middle_index + 1:]

print("Resulting string:", new_string)
