# Logistic regression

Logistic regression is used for classification problems with 2 possible outcomes.

> Logistic regression fits *Sigmoid* function to the data, squishing the linear equation to an output range of *0 ~ 1*. 

The output range can then use to determine the class. For example, *0 ~ 0.5* classifies as class A, *0.5~1* classifies as class B.

## Why we need sigmoid function?

Without sigmoid function, how do we classify by linear regression? We might set a threshold, 0 for example, any output value above 0, it's class A. Any below 0, it's class B.

The classification function is simple but it also has a drawback: impossible to tweak. 1, 2, 100, infinity all output class A, and vice versa. 

## Sigmoid function to make learning possible

We take the output of linear regression $y$ and feed it to the *sigmoid function*:
![](sigmoid.png)

As illustrated in the chart, there are many possible functions to map the output to *0 ~ 1*. 


## Use cases of logistic regression

[ibm](https://www.ibm.com/topics/logistic-regression#anchor-1926156509)

- Fraud detection
- Disease prediction
- Churn prediction
