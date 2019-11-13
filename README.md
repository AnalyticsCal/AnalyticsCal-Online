
# Usage of the PolynomialRegression API

```
data = [[0 for x in range(2)] for y in range(4)]
data[0][0] = 1
data[0][1] = 13
data[1][0] = 2
data[1][1] = 26
data[2][0] = 3
data[2][1] = 42
data[3][0] = 4
data[3][1] = 68

regression = PolynomialRegression(2)
coefficient = regression.fit(data)
print(coefficient)
#[[8.249999999999318, 1.849999999999909, 3.250000000000057]]
```

### The returned coefficients are listed in increasing order of the degree terms, i.e. (B0, B1, B2, B3, ....)
