user_string = input("Please enter a string.")
reversed = ""

# It is looping from String length back to -1.
for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]
if user_string == reversed:
    print("The entered is a palindrome.")
else: print("The entered is not a palindrome.")