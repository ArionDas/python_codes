# check whether all the characters present are vowels

s = input("Enter a string ")
for c in s:
    if c not in "AEIOUaeiou":
        print("False")
        break
else:
    print("All are vowels")
