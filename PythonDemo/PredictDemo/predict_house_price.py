# 1. Import packages:   Required Packages
import matplotlib.pyplot as plt
import numpy
import pandas
from sklearn import datasets, linear_model

# 2. define the function:  Function to get data
def get_data(file_name):
    data = pandas.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    for single_square_feet, single_price_value in zip(data['square_feet'], data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append(float(single_price_value))
    return X_parameter, Y_parameter


# 3. Constructor data.
# input_data.csv  :
# no,square_feet,price,
# 1,150,6450,
# 2,200,7450,
# 3,250,8450,
# 4,300,9450,
# 5,350,11450,
# 6,400,15450,
# 7,600,18450,


# 4. create function.
# Function for Fitting our data to Linear model
def linear_model_main(X_parameters, Y_parameters, predict_value):

    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions



# 5. Function to show the resutls of linear fit model
def show_linear_line(X_parameters, Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters, Y_parameters, color='blue')
    plt.plot(X_parameters, regr.predict(
        X_parameters), color='red', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()


def main():
    print("hello world")
    X, Y = get_data('input_data.csv')

    predictvalue = 650
    result = linear_model_main(X, Y, predictvalue)
    print("Intercept value ", result['intercept'])
    print("coefficient     ", result['coefficient'])
    print("Predicted value:", result['predicted_value'])

    show_linear_line(X,Y)


if __name__ == '__main__':
    main()
