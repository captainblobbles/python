user_str = input("Please enter a string.")
wordToFind = input("Please enter a word to find.")

wordCount = 0
wordUntilSpace = ""

for item in range(0, len(user_str)-1, 1):
    wordUntilSpace += user_str[item]
    if user_str[item+1] == " ":
        if wordToFind == wordUntilSpace:
            wordCount += 1
            wordUntilSpace = ""

print(wordCount)