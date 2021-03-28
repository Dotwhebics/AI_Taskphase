# Logistic Regression

## Definition
Regression is the process of finding relationship between independent and dependent variable iteratively using the data available. Regression can be linear, logistic or polynomial based on the situation and requirement.

Logistic Regression is a form of Regression that is used to catagorise any input value of independent variable into one of the possible binary outputs. Logistic Regression produces only two outputs, 0 or 1 used to denote negative and positive outcome respectively based on our aim.

## Logistic Regression vs Linear Regression

Linear regression is used to find the linear relationship between
the dependent and independent variable. It has a straight line graph
and yields either continuous increasing (slope positive) or continuous 
decreasing (slope negative) values with the change in input values. It is put to use when 
there is a possibility of linearity in the relationship between two factors. It is done using
a method called least squares method.

Logistic Regression is used for catagorisation where any input is catagorised
into two fixed outputs that are the opposite of each other. It has an S shaped or sigmoid
graph confined between the y-values 0 and 1 for any x-value input. It is put to use in 
decisive applications. It is done using a method called maximum liklihood method.

## The Procedure Explained

The final requirement in logistic regression is to determine a sigmoid function that can 
produce output values between 0 and 1. There is a threshold at 0.5 . All values above are
classified as 1 and all values below the threshold value are classified as 0.
To begin with, we linearise the situation first so we can establish a linear relationship 
between the x and y values and then transfrom it to the sigmoid graph.

As an example let's say we aim to predict the extreme possibilities of an event.
The graph of probability vs any independent variable will be a sigmoid graph.

P(E) = 1 / (1 + e^(-z))  - (1)

z is the value of y determined in the linearly fixed relationship.
Let's find out what is z first.
Solving eq(1) we get 

z = ln( P(E) / (1 - P(E)) )

The value within parenthesis of ln , i.e , P(E)/(1-P(E)) is known as the odds of an event.

So, for the linear part of the calculation we use the values of the independent variable 
itself for the x-values and calculate the corresponding odds and take natural log which shall
serve as the y-values.

We find a linear relationship, 

y_pred = mx + c  , m is the slope and c is the y-intercept of the line

We assume intial m and c values and perform gradient descend iteratively converging the 
linear regression line to better fit the data. 

m(new) = m(old) - (learning rate)/(total points) * ∑( (y_pred - y) * x )

c(new) = c(old) - (learning rate)/(total points) * ∑(y_pred - y) 

Now, we may proceed with the transformation to get probability as y-values and the x-values
remain the independent variable values.

This builds up a model for our prediction.

## Applications of Logistic Regression

1) Sports data can be used to build models to predict probability of a particular event.
2) Medical models can be used to predict if the patient suffers from a particular disease.
3) Weather forcast data built models can predict weather conditions, e.g., will it rain?
4) Probability of passing or failing based on the amount of syllabus covered and classes 
attended in an effective manner.

## Sources

> StatQuest with Josh Starmer - YouTube channel

> edureka - YouTube channel

> towards data science website

> https://en.wikipedia.org/wiki/Logistic_regression

> https://gist.github.com/michhar/2dfd2de0d4f8727f873422c5d959fff5 (Titanic dataset)