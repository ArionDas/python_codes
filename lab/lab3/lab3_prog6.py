# check if all the characters is alphanumeric

def check_alphanum(str):
    for c in str:
        if ((c>='A' and c<='Z') or (c>='a' and c<='z') or (c>='0' and c<='9')):
            continue
        else:
            return False
        
    return True

s = input("Enter the string ")
if check_alphanum(s):
    print('True')
else:
    print('False')