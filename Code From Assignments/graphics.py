from matplotlib import pyplot as plt
import numpy as np
import regex
from sympy import sympify
from sympy.abc import x


def graphics(expression, xlow=-10, xhigh=10, ylow=-10, yhigh=10):
    plt.xlim([xlow, xhigh])
    plt.ylim([ylow, yhigh])
    xvals = np.linspace(xlow, xhigh, 10000)
    plt.xlabel('x')
    plt.ylabel('y')
    for i in range(len(expression)):
        poly = []
        for term in regex.findall(r'[+-]?\d*\w+\^?\d*', expression[i]):
            term = regex.sub(r'(\d*)([A-Za-z]\w*)(.*)', r'\1*\2\3', term)
            term = term.replace('^', '**')
            poly.append(term)
        poly = ''.join(poly)
        poly = sympify(poly)
        yvals = [poly.subs(x, y) for y in xvals]
        plt.plot(xvals, yvals, label=f'y={expression[i]}')
    plt.legend(loc='best')
    plt.savefig('task2.png')
    plt.show()


graphics(['1x^2', '1x^3'])
