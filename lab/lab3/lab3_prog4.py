n = int(input("Enter the multiplicand "))
limit = int(input("Enter the limit "))

i = 1
while i <= limit:
    print(str(n) + 'X' + str(i) + ' = ' +  str(i*n))
    i += 1