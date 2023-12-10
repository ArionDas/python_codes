# waps to find the area and perimeter of a triangle when three sides are given. Enter the lengths using input() function.
a = int(input())
b = int(input())
c = int(input())

check = (a+b>c) and (b+c>a) and (a+c>b)

if(check == False):
    print("Triangle not possible")
else:
    s = (a+b+c)/2
    area_sq = s*(s-a)*(s-b)*(s-c)
    area = area_sq**(0.5)
    perm = (a+b+c)
    if(a==b and a==c):
        print("Equilateral")
    elif(a==b or b==c or a==c):
        print("Isosceles")
    else:
        print("Scalene")
    print("area = " + str(area))
    print("perimeter = " + str(perm))
