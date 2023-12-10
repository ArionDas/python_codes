
import matplotlib.pyplot as plt
import random
fobj=plt.figure(figsize=(6,6),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
yn=[random.randrange(1,100,10) for i in range(10)]
xn=[i for i in range(0,10)]
yn.sort()
spobj.plot(xn,yn)
print('xn=',xn)
print('yn=',yn)
plt.show()
