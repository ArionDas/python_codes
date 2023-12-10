# enter the following details of one student :- Name, Roll, Marks for Physics exam. Write a python script to prepare the result sheet based on the given criteria

# Range of marks       Grade Point       Remarks
# --------------       -----------       -------
#      >= 90               10           "OUTSTANDING"
#   90 > Marks >= 80       9            "VERY GOOD"
#   80 > Marks >= 70       8            "GOOD"
#   70 > Marks >= 60       7            "AVERAGE"
#   60 > Marks >= 50       6            "PASS"
#   50 > Marks             0            "FAIL"

# Result Sheet
# ------------
# Name :
# Roll No :
# Marks :
# Grade Point :
# Remarks : 

name = input("Enter student's name ")
roll = int(input("Enter student's roll "))
math_marks = int(input("Enter student's marks "))

if math_marks >= 90:
    grade_point = 10
    remark = "Outstanding"
elif 90 > math_marks >= 80:
    grade_point = 9
    remark = "Very Good"
elif 80 > math_marks >= 70:
    grade_point = 8
    remark = "Good"
elif 70 > math_marks >= 60:
    grade_point = 7
    remark = "Average"
elif 60 > math_marks >= 50:
    grade_point = 6
    remark = "Pass"
else:
    grade_point = 5
    remark = "Fail"

# Display result sheet
print("\nResult Sheet")
print("-------------")
print("Name:" + name)
print("Roll Number:" + str(roll))
print("Mathematics Marks:" + str(math_marks))
print("Grade Point:" + str(grade_point))
print("Remark:" + remark)
print(" tu kya problem set krega re ??!!")


