string_to_reverse = "python"

if len(string_to_reverse) % 4 == 0:
    result = string_to_reverse[::-1]
else:
    result = string_to_reverse

print("Reversed string (if length is a multiple of 4):", result)
