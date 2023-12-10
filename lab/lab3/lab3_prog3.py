# display first n fibonacci terms using while loop

n = int(input("Enter n "))

a = 0
b = 1
c = a + b

print(a,end=' ')
print(b,end=' ')

while n >= 3:
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    n -= 1
    
