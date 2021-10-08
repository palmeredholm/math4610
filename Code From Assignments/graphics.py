from matplotlib import pyplot as plt
import numpy as np


def graphics(expression, xlow=-10.0, xhigh=10.0, ylow=-10.0,
             yhigh=10.0):
    # Set size of graph
    plt.xlim([xlow, xhigh])
    plt.ylim([ylow, yhigh])
    # Create values for x-axis
    xvals = np.linspace(xlow, xhigh, 10000)
    # Hard code labels for axes
    plt.xlabel('x')
    plt.ylabel('y')
    # Loop through all strings in array
    for i in range(len(expression)):
        # Create anonymous function for ith function in expression
        func = lambda x: eval(expression[i])
        # Compute range values of function
        yvals = [func(y) for y in xvals]
        # Plot the function
        plt.plot(xvals, yvals, label=f'y={expression[i]}')
    plt.legend(loc='best')
    plt.show()
