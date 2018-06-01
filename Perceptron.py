import numpy as np
import math

class Perceptron:
    def __init__(self, eta, epochs):
        eta = 0.25
        epochs = 100
    def training(self, X, Y):
        self.w = np.zeros(len(X[0])) #initializing a vector representing the weights
        k = 0
        i = 0




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
    
