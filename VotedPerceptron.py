import numpy as np
import math


class VotedPerceptron:
    def __init__(self, eta, epochs, X):
        self.eta = eta
        self.epochs = epochs
        self.W = [np.zeros(len(X[0]))]
        self.c = 0
        self.w = np.zeroes(len(X[0])) #vector of predictions
        self.X = X

    def training(self, X, Y):
        k = 0
        i = 0
        while True:
            nErr = 0
            for x,y in zip(X,Y):
                if y*(1 if np.dot(x,self.w) else -1)>=0:
                    self.c +=1
                else:
                    self.W.append([(w+y*r) for w,r in zip(self.w,x)])
                    self.w = self.W[self.k +1]
                    self.k+=1
                    nErr += 1
            i+=1
            if nErr == 0 or i>self.epochs:
                break
        if i > self.epochs:
            print "ERROR, look at hyperplane"
        return self.w, i-1, len(self.W)

    def net_input(self, x):
        for i in range(0,self.k+1,1):
            if np.dot(x,self.W[i])>=0:
                s = 1
            else:
                s = 1


    def guess(self, x):
        if self.net_input(x)>=0:
            return 1
        else:
            return -1