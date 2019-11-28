from polynomial_regression import PolynomialRegression
import random
import numpy as np # numpy is used only for test data generation
import assignment_dataset as Dataset

def getPredictions(coefficients, independent):
    predictionList = []
    
    for sampleIndex in range(len(independent)):
        prediction = 0
        for index in range(len(coefficients)):
            prediction = prediction + coefficients[index] * pow(independent[sampleIndex], index)
        predictionList.append(prediction)
    return predictionList

def generateDataSet(coefficient=[], addError=False):
    independentList = np.arange(0, 50, 1.5)
    dependentList = []
    for value in independentList:
        dependent = 0
        for index in range(len(coefficient)):
            dependent = dependent + coefficient[index] * pow(value, index)
        if addError:
            dependent = dependent + random.randint(-100, 100)
        dependentList.append(dependent)
        
    return independentList, dependentList

def fitLineAndPlot(independentList, dependentList, plt, order=1):
    regression = PolynomialRegression(order)
    coefficient = regression.fit(independentList, dependentList)
    print('Coefficients for order %d' % order, coefficient)
    predictionList = getPredictions(coefficient, independentList)
    plt.plot(independentList, predictionList, label='Order-%d' % order, linewidth=3)
    plt.legend()
    
def drawScatterPlot(independentList, dependentList, plt):
    plt.scatter(independentList, dependentList, s=100)
    
def getAssignmentDataset():
    return Dataset.assignmentIndependentList, Dataset.assignmentDependentList
    