import matplotlib.pyplot as plt
import numpy as np
import random
import time

#hypothesis function
def h(theta0, theta1, xi):
    return theta0+theta1*xi

#cost function
def J_der(theta0, theta1,xi,yi, isThetaOne):
    if not isThetaOne: return (h(theta0, theta1, xi) - yi)
    else: return (h(theta0, theta1, xi) - yi) * xi

def J(theta0, theta1, xi, yi, isThetaOne):
    sum = h(theta0, theta1, xi) - yi
    return sum*sum



#sum of cost function
def Sum(theta0, theta1, x, y, m, isThetaOne, function):
    total = 0
    for i in range(0, m):
        total = total + function(theta0, theta1, x[i], y[i], isThetaOne)
    return total / m

def gradientDescent(x,y, alpha):
    #weight 0
    theta0 = random.uniform(0,2)
    #weight 1
    theta1 = random.uniform(0,3)
    temp0 = theta0
    temp1 = theta1
    sameVal = False
    graph(theta0, theta1, 'g')

    while Sum(theta0, theta1, x, y, x.size, 0, J)/2 > .0001 and not sameVal:
        temp0 = theta0 - (alpha * Sum(theta0, theta1, x, y, x.size, 0, J_der))
        temp1 = theta1 - (alpha * Sum(theta0, theta1, x, y, x.size, 1, J_der))
        if round(temp0, 10) == round(theta0, 10) and round(temp1, 10) == round(theta1, 10): sameVal = True
        theta0 = temp0
        theta1 = temp1
    graph(theta0, theta1, 'b')
        
def graph(theta0, theta1, char):
    for i in range (0, 15):
        plt.plot(i,theta0+theta1*i,'{}o'.format(char))


def ploting(x, y):
    plt.plot(x, y, 'ro')
    plt.axis([0,np.amax(x)+5, 0,np.amax(y)+5])
    plt.show()

def main():
    '''
    Learning rate
    '''
    alpha = .01
    data = np.random.rand(2,10)
    data = data*10
    x, y = np.vsplit(data, [1])
    gradientDescent(x[0],y[0], alpha)
    ploting(x[0],y[0])
    
    
    

main()
 
    