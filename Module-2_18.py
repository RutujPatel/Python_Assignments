given_string = input("Enter a string: ")

if len(given_string) >= 3:
    if given_string.endswith('ing'):
        new_string = given_string + 'ly'
    else:
        new_string = given_string + 'ing'
else:
    new_string = given_string

print("Modified string:", new_string)
