import cv2
import math
import os

if __name__ == '__main__':
    # Variable Declaration
    model = cv2.CascadeClassifier("cascade.xml")
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    # Handle positive samples
    os.chdir("datasets")
    for i in open("positiveSamples/positiveTestDataInfo.txt").read().split('\n')[:-1]:
        if len(model.detectMultiScale(cv2.imread("positiveSamples/" + i, 0))) == 0:
            FN += 1
        else:
            TP += 1

    print("Positive Samples handled")

    # Handle negative samples
    os.chdir("..")
    myList = open("datasets/negativeSamples/negativeTestDataInfo.txt").read().split('\n')[:-1]
    for i in range(len(myList)):
        if len(model.detectMultiScale(cv2.imread(myList[i], 0))) == 0:
            TN += 1
        else:
            FP += 1
        print("(Handling Negative samples) " + str(math.floor((i / len(myList)) * 100)) + "% complete")

    print("---- Classification Report ----")
    print("Accuracy = " + str(round((TN + TP) / (TN + FP + FN + TP), 4)))
    precision = TP / (TP + FP)
    print("Precision = " + str(round(precision, 4)))
    recall = TP / (TP + FN)
    print("Recall = " + str(round(recall, 4)))
    print("F1 Score = " + str(round(2 * ((precision * recall) / (precision + recall)), 4)))
