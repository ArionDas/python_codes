nums = [int(var) for var in input("Enter the numbers to be reversed: ").split()]

def reverse_numbers(j):
    r=0
    d=0
        
    while(j>0):
        d = j%10
        r = r*10 + d
        j //= 10
        

    return r

nums2 = list(map(reverse_numbers,nums))
print(nums2)
