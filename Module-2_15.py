string_input = input("Enter a string: ")
substring_input = input("Enter the substring to count: ")

count = 0
start_index = 0

while True:
    index = string_input.find(substring_input, start_index)
    if index == -1:
        break
    count += 1
    start_index = index + 1

print(f"The substring '{substring_input}' occurs {count} time(s) in the string.")
