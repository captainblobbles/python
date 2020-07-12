user_str = input("Please enter a string.")
charToFind = input("Please enter a character.")

charCount = 0
for item in range(0, len(user_str)-1, 1):
    if charToFind == user_str[item]:
        charCount += 1

print(charCount)