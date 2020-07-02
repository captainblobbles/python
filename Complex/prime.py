p= int(input("Please enter an integer: "))

if (p<2):
    print(p, "is NOT a prime number")
elif (p==2):
    print(p, "is a prime number")

else:
    isPrime = "true"

for i in range(2,p):
    if (p%i)==0:
        isPrime = "false"
        div=i
        break

if (isPrime == "true"):
    print(p, "is a prime number.")
else:
    print(p, "is NOT a prime number and is divisible by ", div)