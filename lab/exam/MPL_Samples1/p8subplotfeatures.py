
import matplotlib.pyplot as plt
fobj=plt.figure(figsize=(8,8),facecolor='#00FF00')
print(type(fobj))
spobj1=fobj.add_subplot(221,facecolor='#0000FF')
print(type(spobj1))
spobj1=fobj.add_subplot(222,facecolor='0.5')
spobj1=fobj.add_subplot(223)
plt.show()
