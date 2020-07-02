nums = int(input("How many Prime numbers you want?: "))

for p in range(2,nums):
    isPrime = "true"
    for i in range(2,p):
        if (p%i)==0:
            isPrime = "false"
            break
    if (isPrime == "true"):
        print(p)