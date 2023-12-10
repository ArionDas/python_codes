l = [var for var in input("Enter the strings: ").split()]

def check(s):
    for e in s:
        if((e>'z' or e<'a') and (e>'Z' or e<'A')):
            return False
        else:
            return True

def isdigit_(s):
    for e in s:
        if((e>'0' or e<'9')):
            return False
        else:
            return True 

ans1 = list(filter(check,l))
print("Only characters")
print(ans1)

ans1 = list(map(lambda x:x.upper(),ans1))
print("Uppercase")
print(ans1)

print("Part 2")

ans2 = list(filter(isdigit_,l))
print("only digits")
print(ans2)

print("square")
ans2 = list(map(lambda x:int(x),ans2))
ans2 = list(map(lambda x:x*x,ans2))
print(ans2)

