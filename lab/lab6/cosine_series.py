import math as m

n = int(input("Enter the number of terms: "))
x = int(input("Enter the degrees: "))
x = x*(3.14)/180
sum_ = 1.0
dummy = 1

def fact(num):
    if(num<=1):
        return 1
    return fact(num-1)*num

def find_cosine_series_sum(x,n,sum_,dummy):
    for i in range(n-1):
        if(dummy&1):
            sum_ += ((-1)*((pow(x,dummy*2))/fact(dummy*2)))
        else:
            sum_ += ((pow(x,dummy*2))/fact(dummy*2))

        dummy += 1

    return sum_


ans = find_cosine_series_sum(x,n,sum_,dummy)
print("The required sum is {0}".format(ans))
        
