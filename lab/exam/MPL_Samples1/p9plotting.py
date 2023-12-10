
import matplotlib.pyplot as plt
import random
fobj=plt.figure(figsize=(6,4),facecolor='#00FF00')
spobj=fobj.add_subplot(111,facecolor='1')
an=[random.randint(1,100) for i in range(10)]
spobj.plot(an)
print(an)
plt.show()
