# Polynomial regression

> Sometimes the data does not look like a straight line. It looks like there are curves in there. Then you probably need a polynomial regression.

Note: 
- **We have only 1 variable (x).**
- It's very sensitive to outliers
- In the context of ML, the return coefficients might come in this order: $(x^1, x^2, x^3, x^4, x^5 ...)$


![](20230205_polynomial_regression.png)


Vocabulary:
Example algebra: $y = 3x^5 + 8x^2 + 1$
- degree of a polynomial: the highest power. . Degree is 5 here.
- coefficient: the *weights* of each degree parameter. Here is $(x^5, x^4, x^3, x^2, x^1)$ ->`(3, 0, 0, 8, 1)`. **Some libraries return this in different order. Some from low to high, vice versa.
- leading term: the term with highest power. here is $3x^5$
- leading coefficient. $3$ in our example
- intercept, constant term: $1$ in this example.

## (Multiple) linear regression v.s. polynomial regression

Polynomial regression mathematical form:
$y = w_1*x + w_2*x^2 + ... + w_n*x^n + constant$ 

Multiple linear regression form:
$y = w_1*x_1 + w_2*x_2 + ... + w_n * x_n + constant$ 

> Polynomial regression is a linear model that used for describe non-straight line relationships. It does by raising the power/degree of a feature.

