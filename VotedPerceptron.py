import numpy as np
import math


class VotedPerceptron:
    def __init__(self, eta, epochs):
        self.eta = eta
        self.epochs = epochs


    def training(self, X, Y):
        self.k = 0
        self.c = [0]
        self.W = [np.zeros(len(X[0]))]
        self.w = np.zeros(len(X[0])) #vector of predictions
        i=0
        while True:
            nErr = 0
            for x, y in zip(X, Y):
                if y*(1 if np.dot(x, self.w) >= 0 else -1) >= 0:
                    self.c[self.k] += 1
                else:
                    self.W.append([(h + y*r) for h, r in zip(self.w, x)])
                    self.w = self.W[self.k + 1]
                    self.c.append(1)
                    self.k += 1
                    nErr += 1
            i += 1
            if nErr == 0 or i > self.epochs:
                break
        if i > self.epochs:
            print "ERROR, look at hyperplane"
        #print "valore di k", self.k
        return self.w, i-1, len(self.W)

    def net_input(self, xi):
        s = [(1 if np.dot(xi, self.W[i]) >= 0 else -1)*self.c[i] for i in np.arange(0, self.k+1, 1)]
        return sum(s)


    def guess(self, x):
        return 1 if self.net_input(x) >= 0 else -1
