import matplotlib.pyplot as plt
from polynomial_regression import PolynomialRegression

data = [[0 for x in range(2)] for y in range(4)]
data[0][0] = 1
data[0][1] = 13
data[1][0] = 2
data[1][1] = 26
data[2][0] = 3
data[2][1] = 42
data[3][0] = 4
data[3][1] = 68

def getPredictions(coefficients, independent):
    predictionList = []
    
    for sampleIndex in range(len(independent)):
        prediction = 0
        for index in range(len(coefficient)):
            prediction = prediction + coefficient[index] * pow(independent[sampleIndex], index)
        predictionList.append(prediction)
    return predictionList


independent = []
dependent = []
for (x, y) in data:
    independent.append(x)
    dependent.append(y)

p2 = PolynomialRegression(2)
coefficient = p2.fit(independent, dependent)
print(coefficient)
plt.scatter(independent, dependent)
predictionList = getPredictions(coefficient, independent)
plt.plot(independent, predictionList)