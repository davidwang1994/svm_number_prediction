import os
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

print 100 * "#" + "\n"
print "Loading datasets..."
 
# Get sklearn digit datasets
digits = datasets.load_digits()
dataset_size = len(digits.target)
# Get path of the digit files
print "Loaded " + str(dataset_size) + " digit datasets from " + os.path.dirname(datasets.__file__)

'''
Keep looping until user inputs a valid number, which is defined as a value
greater than 0 and less than the overall lenght of the number of digits in the
file. Otherwise the variable will be set to the default values which for 
gamma_val=0.001, and C_val=100
'''
while True:
    try:
        gamma_val= raw_input("Enter gamma value (default=0.001): ")
        if gamma_val == "":
            gamma_val = 0.001
            break
        else:
            gamma_val = float(gamma_val)
    except ValueError:
        print "Please enter a valid floating number for gamma value."
    else:
        break

while True:
    try:
        C_val= raw_input("Enter C value (default=100): ")
        if C_val == "":
            C_val = 100
            break
        else:
            C_val = float(C_val)
    except ValueError:
        print "Please enter a valid floating number for C value."
    else:
        break

print "Created Support Vector Machine Classifier with following attributes:"
# Create the SVM classifier
# SVC is actually the C-Support Vector Classification model
clf = svm.SVC(gamma=gamma_val, C=C_val)
print clf

while True:
    try:
        train_size = raw_input("How many datasets out of " + str(dataset_size) + " do you want to use for trainning?: ")
    except ValueError:
        print "Value must be in the range of 0 - " + str(dataset_size)
    else:
        train_size = int(train_size)
        if train_size > 0 and train_size < dataset_size:
            break
        else:
            print "Value must be in the range of 0 - " + str(dataset_size)
    
X,y = digits.data[:train_size], digits.target[:train_size]

print "Trainning classifier with " + str(train_size) + " datasets."

clf.fit(X,y)

print "Beginning classification prediction on " + str(dataset_size -
        train_size) 


correct = []
incorrect = []

for index in range(train_size, dataset_size):
    print "predicting dataset #" + str(index)
    data = digits.data[index]
    prediction = clf.predict(data)
    if prediction == digits.target[index]:
        print "value: " + str(digits.target[index]) + " prediction: " + str(prediction)
        correct.append(data)
    else:
        print "############# Incorrect ########### value: " + str(digits.target[index]) + \
        "prediction: " + str(prediction)
        incorrect.append(data)
#    plt.imshow(digits.images[index], cmap=plt.cm.gray_r, interpolation='nearest')
#    plt.show()

print str(len(correct)) + " correct predictions"
print str(len(incorrect)) + " incorrect predictions"

print "\n" + 100 * "#"
