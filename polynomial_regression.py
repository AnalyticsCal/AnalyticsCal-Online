#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt 

class PolynomialRegression:
  def __init__(self, order):
    self.order = order
    
  def fit(self, data):
      A = self._getCoefficientMatrix(data)
      b = self._getResultsVector(data)
      A_Inverse = self._inverse(A)
      X = self._multiply(A_Inverse, b)
      return self._transpose(X)

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
      A = [[0 for x in range(dim)] for y in range(dim)]
      for i in range(dim):
          for j in range(dim):
              A[i][j] = dependentVariableSum[i+j]
      return A
  
  def _getResultsVector(self, data):
      dim = self.order + 1
      A = [[0 for x in range(1)] for y in range(dim)]
      
      for j in range(dim):
          sum = 0
          for (x, y) in data:
              sum = sum + (pow(x, j) * y)
          A[j][0] = sum
      return A
  
  def _inverse(self, matrix):
      x = np.array(matrix)
      y = np.linalg.inv(x)
      return y
  
  def _transpose(self, matrix):
      matrix_transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
      return matrix_transpose
  
  def _multiply(self, X, Y):
      return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]


data = [[0 for x in range(2)] for y in range(4)]
data[0][0] = 1
data[0][1] = 13
data[1][0] = 2
data[1][1] = 26
data[2][0] = 3
data[2][1] = 42
data[3][0] = 4
data[3][1] = 68

independent = []
dependent = []
for (x, y) in data:
    independent.append(x)
    dependent.append(y)

        
p1 = PolynomialRegression(2)
coefficient = p1.fit(data)
print(type(coefficient))
print(coefficient)
plt.scatter(independent, dependent)