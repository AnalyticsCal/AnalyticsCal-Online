# AnalyticsCal-Online

# Usage of the PolynomialRegression API

```
from polynomial_regression import PolynomialRegression

independent = [1, 2, 3, 4]
dependent = [13, 26, 42, 68]
    
regression = PolynomialRegression(2)
coefficient = regression.fit(independent, dependent)
print(coefficient)
#[8.25, 1.849999999999909, 3.25]
    
```
#### PolynomialRegression(n) <--- Here n indicates the degree of the curve being fit for regression.
#### coefficient = regression.fit(independent, dependent) <--- independent, dependent are two lists containing independent and dependent variable from the sample
#### The returned coefficients are listed in increasing order of the degree terms, i.e. (B0, B1, B2, B3, ....)
