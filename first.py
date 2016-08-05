import random
import matplotlib.pyplot as plt

#from findTrace import findTrace_Random
from agent import Agent

#import matplotlib.pyplot as plt

xmin = 0;
xmax = 1000;
ymin = 0;
ymax = 1000;

tmax = 10;
tickGap = 100;

a1 = Agent(1,xmin,xmax,ymin,ymax,tmax);
a1.findTrace_Random(tickGap)
a1.plotTrace()
#xcor = [500]
#ycor = [500]

#xcor, ycor = findTrace_Random(xmin,xmax,ymin,ymax,tmax,tickGap,xcor,ycor)

#plt.plot(xcor,ycor,"b.")
#plt.xlabel("X")
#plt.ylabel("Y")
#plt.show()
#print "mobility completed"

