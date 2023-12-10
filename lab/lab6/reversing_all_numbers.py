nums = [int(var) for var in input("Enter the numbers to be reversed").split()]

def reverse_numbers(nums):
    d=0
    for i in range(len(nums)):
        r=0
        j = nums[i]
        while(j>0):
            d = j%10
            r = r*10 + d
            j //= 10
        nums[i] = r

    return nums

rev_list = reverse_numbers(nums)
print(rev_list)
