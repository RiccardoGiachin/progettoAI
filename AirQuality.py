import Perceptron as pc
import VotedPerceptron as vp
import numpy as np
import pandas as p
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report



def test():
    y = []
    X = []
    Y = []
    print(" AIR QUALITY")
    ph = p.read_csv('datasets/AirQualityUCI.csv')
    ph.columns = ['date', 'time', 'CO(GT)', 'PT08', 'NMHC', 'C6H6', 'PT08.S2', 'NOx', 'PT08.S3', 'NO2', 'PT08.S4',
    			  'PT08.S5', 'T', 'RH', 'AH']
    y = ph[['PT08']]
    Y = [1 if fy.PT08 == 1313 else -1 for fy in y.itertuples()]
    X = (ph.iloc[:, 0:14])

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
    X_train = np.insert(np.array(X_train), 0, 1, axis=1)
    X_test = np.insert(np.array(X_test), 0, 1, axis=1)

    print(" ------------------- ")
    print(" STANDARD PERCEPTRON ")

    o_per = pc.Perceptron(0.25, 200)

    wei_standard, i_standard, k_standard = o_per.training(X_train, Y_train)

    # print "weight vector", wei_standard, "iteration done",  i_standard, k_standard
    wei_Y_per = [o_per.guess(z) for z in X_test]



    cm = confusion_matrix(Y_test, wei_Y_per)
    np.set_printoptions(precision=3)
    print("accuracy of a layer: %.2f%%" % (100 * accuracy_score(Y_test, wei_Y_per)))

    print

    print("confusion matrix, no normalization")
    print cm
    print
    print

    print ('normalized confusion matrix')
    print cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    print
    print

    print(classification_report(Y_test, wei_Y_per))

    print("lunghezza XTrain", len(X_train))
    print("VOTED PERCEPTRON")

    o_vper = vp.VotedPerceptron(0.25, 200)

    wei_voted, i_voted, length_array = o_vper.training(X_train, Y_train)

    wei_Y_vper = [o_vper.guess(z) for z in X_test]

    accu = 100 * accuracy_score(Y_test, wei_Y_vper)
    print("accuracy of a layer voted: %.2f%%" % (accu))

    cmv = confusion_matrix(Y_test, wei_Y_vper)
    np.set_printoptions(precision=3)

    print

    print("confusion matrix voted not normalized")
    print cmv
    print
    print

    print("normalized confusion matrix")
    print cmv.astype('float') / cmv.sum(axis=1)[:, np.newaxis]
    print
    print

    print(classification_report(Y_test, wei_Y_vper))