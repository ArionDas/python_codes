# count occurrences of specific character in the given string using for loop

s = input("Enter the string ")
ch = (input("Enter the character to be searched "))
cnt = 0
for c in s:
    if c == ch:
        cnt += 1
        
print(ch + " occurs " + str(cnt) + " in " + s)