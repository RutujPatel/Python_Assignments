string_input = input("Enter a string: ")

character_frequency = {}


for char in string_input:
    character_frequency[char] = character_frequency.get(char, 0) + 1


print("Character Frequency:")
for char, count in character_frequency.items():
    print(f"'{char}' occurs {count} time(s)")
