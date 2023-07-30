sentence = input("Enter a sentence: ")

words = sentence.strip().split()

word_frequency = {}

for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("Word Frequency:")
for word, count in word_frequency.items():
    print(f"'{word}' occurs {count} time(s)")
