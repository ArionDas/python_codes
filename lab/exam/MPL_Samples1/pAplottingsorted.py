
import matplotlib.pyplot as plt
import random
fobj=plt.figure(figsize=(4,4),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
print(type(spobj))
an=[random.randint(1,100) for i in range(10)]
an.sort()
spobj.plot(an)
print(an)
plt.show()
