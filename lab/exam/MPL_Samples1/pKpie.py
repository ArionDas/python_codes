
import matplotlib.pyplot as plt

fobj=plt.figure(figsize=(6,6),facecolor='0.5')
spobj=fobj.add_subplot(1,1,1)
fruits='Apple Orange Grapes Mango Pineapple'.split()
sales=[30,40,25,10,35]
colrs='r y c g b'.split()
spobj.pie(sales)
#spobj.pie(sales,colors=colrs)
#plt.legend(fruits,loc='upper left')
#spobj.pie(sales,colors=colrs,labels=fruits)
#spobj.pie(sales,colors=colrs,labels=fruits,startangle=90)
#expl=[0.2,0,0,0,0]
#spobj.pie(sales,explode=expl,colors=colrs,shadow=True,startangle=90,labels=fruits)

plt.show()
