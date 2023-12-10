# find sum of digits of a number using while loop

n = int(input("Enter n "))
sum = 0
while n > 0:
    sum += n%10
    n //= 10
    
print(sum)