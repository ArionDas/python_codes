# write a python script to check whether entered string is a palindrome or not without using in built function

def check_palin(str, low, high):
    while(low<=high):
        if(str[low] != str[high]):
            return False
        low += 1
        high -= 1
    return True

S = input()
if check_palin(S,0,len(S)-1):
    print("Palindrome")
else:
    print("Not Palindrome")
