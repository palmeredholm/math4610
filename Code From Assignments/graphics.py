from matplotlib import pyplot as plt
import numpy as np
import regex
from sympy import sympify
from sympy.abc import x


def graphics(expression, xlow=-10, xhigh=10, ylow=-10, yhigh=10):
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
        poly = []
        # Insert appropriate math operators
        for term in regex.findall(r'[+-]?\d*\w+\^?\d*', expression[i]):
            term = regex.sub(r'(\d*)([A-Za-z]\w*)(.*)', r'\1*\2\3', term)
            term = term.replace('^', '**')
            poly.append(term)
        poly = ''.join(poly)
        # Parse the polynomial so it's a sympy object
        poly = sympify(poly)
        # Calculate range values
        yvals = [poly.subs(x, y) for y in xvals]
        # Plot the function
        plt.plot(xvals, yvals, label=f'y={expression[i]}')
    plt.legend(loc='best')
    plt.show()
