
pos_int = int(input("Please enter a positive integer."))
int_init = pos_int

summed = 0
while pos_int > 0:
    summed += pos_int

    pos_int -= 1

print(int_init)
print(summed)