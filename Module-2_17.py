string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) >= 2 and len(string2) >= 2:  
    new_string = string2[:2] + string1[2:] + " " + string1[:2] + string2[2:]
else:
    print("Both strings must have at least 2 characters.")
    exit()

print("After swapping first two characters:")
print(new_string)
