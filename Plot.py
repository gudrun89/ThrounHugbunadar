import numpy as np
import matplotlib.pyplot as plt
import math

def plotFunction(x,y,xlab='',ylab='',title='', gridOn=False):
    plt.plot(x,y)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    if (gridOn):
        plt.grid()
    plt.show()
