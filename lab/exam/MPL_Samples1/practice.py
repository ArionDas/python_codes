import matplotlib.pyplot as plt
import random

fobj = plt.figure(figsize=(8,8),facecolor='red')
spobj = fobj.add_subplot(1,1,1)
stud_name = 'Ram Tom Raj Ravi Roy Anil'.split()
x_val = [n for n in range(len(stud_name))]

stud_scores = [90,30,60,50,25,80]
spobj.bar(x_val, stud_scores)

plt.title("student performance")
plt.show()

