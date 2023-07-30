given_string = input("Enter a string: ")

if len(given_string) < 2:
    new_string = ""
else:
    new_string = given_string[:2] + given_string[-2:]

print("Resulting string:", new_string)
