import matplotlib.pyplot as plt
import random
fobj=plt.figure(figsize=(10,10),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
fobj.suptitle('My-Plots')
yn1=[random.randrange(1,25,5) for i in range(5)]
xn=[n for n in range(5)]
print(xn)
yn1.sort()
print(yn1)
yn2=[2*n for n in yn1]
print(yn2)
spobj.plot(xn,yn1,'ro:',drawstyle='steps-mid',label='Single')
spobj.plot(xn,yn2,'bo:',drawstyle='steps-mid',label='Double')
spobj.set_xticks(xn)
spobj.set_xlabel('Parts')
spobj.set_title('Modified sample plot')
spobj.legend(loc='best')
'''print('xn=',xn)
print('yn=',yn)'''
plt.show()
