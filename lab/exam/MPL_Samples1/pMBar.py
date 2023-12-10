import matplotlib.pyplot as plt
import random
fobj=plt.figure(figsize=(6,4),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
stud_name='Ram Tom Raj Ravi Roy Anil'.split()
x_val=[n for n in range(len(stud_name))]

stud_scores=[90,30,60,50,25,80]
spobj.bar(x_val, stud_scores)
#spobj.bar(x_val, stud_scores, width=0.3)
#spobj.bar(x_val, stud_scores, color='r',width=0.3)
#spobj.barh(x_val, stud_scores, height=0.3)
spobj.set_xticks(x_val)
spobj.set_xticklabels(stud_name)
plt.title("Student's Performance")
plt.show()
