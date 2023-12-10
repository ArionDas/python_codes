# find squares of first n natural numbers using while loop

n = int(input("Enter n "))
i = 1
while i <= n:
    print(str(i) + " " + str(i*i))
    i += 1