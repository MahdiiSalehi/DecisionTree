#In the name of ALLAH!
#Mahdi Salehi

from settings import *
from my_array import Array
from random_forest_classifier import RFClassifier


rfc = RFClassifier()
predicted_labels = rfc.predict_all(test_rows, 10)
accuracy = rfc.accuracy(predicted_labels)
print(accuracy)
rfc.print()