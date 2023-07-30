strings_list = ["hello", "python", "wow", "level", "good"]

count = 0

for string in strings_list:

    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print("Number of strings where first and last character are the same:", count)