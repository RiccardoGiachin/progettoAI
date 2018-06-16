import numpy as np
import math

class Perceptron:
    def __init__(self, eta, epochs):
        eta = 0.25
        epochs = 100
        self.w = np.zeros(len(X[0]))  # initializing a vector representing the weights
    def training(self, X, Y):
        k = 0
        i = 0
        vec = self.norm(X)
        while True:
            nErr = 0
            for x, y in zip(X, Y):
                if y*self.future(x)<0:
                    self.w[1:] = [fx + self.eta*(fy*y) for fx, fy in zip(self.w[1:], x)] #it allows to read inside a list.
                    self.w[0] += self.eta *y*math.pow(vec,2)
                    k += 1
                    nErr = nErr + 1
            i = i+1
            print "number of errors:", nErr
            if nErr == 0 or i > self.epochs:
                break
        if i > self.epochs:
            print "an error has occured"
            return self.w, i-1, k




    def norm(self, X):
        o = np.linalg.norm(X[0]);
        for i in range(1, len(X)):
            if np.linalg.norm(X[i])>o:
                o = np.linalg.norm(X[i])
        return o

    def input(self,x):
        return np.dot(x, self.w) #it makes the multiplication between an element of the input vector and the initial weight

    def future(self, x):
        return 1 if self.input(x)>= 0.0 else 0

