
import matplotlib.pyplot as plt
import random
fobj=plt.figure(figsize=(10,10),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
yn=[random.randrange(200,300,10) for i in range(10)]
xn=[n for n in range(10)]
yn.sort()
spobj.plot(xn,yn,color='green',linestyle='dotted',marker='o',mfc='r',mec='blue')
print('xn=',xn)
print('yn=',yn)
plt.show()
