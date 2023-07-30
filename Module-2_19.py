given_string = input("Enter a string: ")

not_index = given_string.find('not')
poor_index = given_string.find('poor')

if not_index != -1 and poor_index != -1 and not_index < poor_index:

    result_string = given_string[:not_index] + 'good' + given_string[poor_index + 4:]
else:
    result_string = given_string


print("Resulting string:", result_string)
