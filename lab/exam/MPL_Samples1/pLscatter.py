import matplotlib.pyplot as plt
import random
fobj=plt.figure(figsize=(6,6),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
yn=[random.randint(1,100) for i in range(10)]
xn=[n for n in range(0,20,2)]
yn.sort()
spobj.scatter(xn,yn)
#spobj.scatter(xn,yn,color='r',marker='*')
#spobj.scatter(xn,yn,color='r',marker='$test$',)
#spobj.scatter(xn,yn,color='r',marker='$test$',s=300)

print('xn=',xn)
print('yn=',yn)
plt.show()
