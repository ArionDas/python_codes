import matplotlib.pyplot as plt
import random
fobj=plt.figure(figsize=(10,10),facecolor='#00FF00')
fobj.suptitle('My-Plots')
spobj=fobj.add_subplot(1,1,1)
yn=[random.randrange(0,100,10) for i in range(4)]
xn=[n for n in range(4)]
xtick=[0,2,4]
ytick=[0,25,50,75,100]
spobj.set_yticks(ytick)
yn.sort()
spobj.plot(xn,yn,'ro:',drawstyle='steps-mid')
spobj.set_xticks(xtick)
spobj.set_xticklabels(['Phase 1', 'Phase 2', 'Phase 3'],rotation=90, fontsize='large')
spobj.set_xlabel('Time in Seconds')
spobj.set_ylabel('Amplitude')
spobj.set_title('A sample plot')
print('xn=',xn)
print('yn=',yn)
plt.show()
