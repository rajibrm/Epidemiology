#agent.py
import random;
import matplotlib.pyplot as plt

class Agent:
    id = 0
    xmin = 0;
    xmax = 0;
    ymin = 0
    ymax = 0
    tmax = 0;
    xcor = [0]
    ycor = [0]
    
    def __init__(self,id,xmin,xmax,ymin,ymax,tmax):
        self.id = id
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.tmax = tmax
        self.xcor[0] = random.randint(0,self.xmax)
        self.ycor[0] = random.randint(1,self.ymax)
        print("An agent with id " + str(id) + " created")
    
    def findTrace_Random(self, tickGap):
        for i in range(1,self.tmax):
            if i%tickGap == 0:
                print("ticks completed " + str(i))
            #get previous coordinate
            currx = self.xcor[i-1]
            curry = self.ycor[i-1]
        
            #compute current coordinate
            randx = random.random()
            if randx > 0.5:
                currx = currx + 1
            else: 
                currx = currx - 1
            
            randy = random.random()
            if randy > 0.5:
                curry = curry + 1
            else:
                curry = curry -1;
        
            if currx > self.xmax:
                currx = currx % self.xmax
        
            if currx < self.xmin:
                currx = currx + self.xmax
        
            if curry > self.ymax:
                curry = curry % self.ymax
            
            if curry < self.ymin:
                curry = curry + self.ymax
            
            #add current coordinate to locations
            self.xcor.append(currx)
            self.ycor.append(curry)
            
        print("Trace created for agent " + str(id)+" for " + str(self.tmax) + " ticks duration")
    
    def storeTrace(self,filename):
        print("trace storing")    
    
    def readTrace(self,fileName):
        print("trace loading")
    
    def plotTrace(self):
        plt.plot(self.xcor,self.ycor,"b.")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()
        print "plotting done ... "
    