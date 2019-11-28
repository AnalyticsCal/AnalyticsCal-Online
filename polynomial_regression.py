import matrix_operation as mo

class PolynomialRegression:
  def __init__(self, order):
    self.order = order  

  def fit(self, independent, dependent):
      if len(independent) != len(dependent):
          raise ValueError(
            'Number of samples of dependent and independent variables must be same')
          
      data = [[0 for x in range(2)] for y in range(len(independent))]
      for index in range(len(independent)):
          data[index][0] = independent[index]
          data[index][1] = dependent[index]
          
      return self._fit(data)
  
  def _fit(self, data):
      # A.X = b
      A = self._getCoefficientMatrix(data)
      b = self._getResultVector(data)
      A_Inverse = mo.getMatrixInverse(A, tol=1)
      X = mo.multiply(A_Inverse, b)
      return mo.transposeMatrix(X)[0]

  def _getCoefficientMatrix(self, data):
      dependentVariableSum = {}
      power = 0
      
      while power <= self.order * 2:
          sum = 0
          for (x, y) in data:
              sum = sum + pow(x, power)
          dependentVariableSum[power] = sum
          power = power + 1            
      
      dim = self.order + 1
      coefficientMatrix = [[0 for x in range(dim)] for y in range(dim)]
      for i in range(dim):
          for j in range(dim):
              coefficientMatrix[i][j] = dependentVariableSum[i+j]
      return coefficientMatrix
  
  def _getResultVector(self, data):
      dim = self.order + 1
      resultVector = [[0 for x in range(1)] for y in range(dim)]
      
      for j in range(dim):
          sum = 0
          for (x, y) in data:
              sum = sum + (pow(x, j) * y)
          resultVector[j][0] = sum
      return resultVector