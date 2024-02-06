import matplotlib.pyplot as plot
import numpy as np

line = [0, 1]
recursionDepth = 6

def divide(line, level=0):
    plot.plot(line, [level, level], color="k", lw=20, solid_capstyle="butt")
    if level < recursionDepth:
        s = np.linspace(line[0], line[1], 4)
        divide(s[:2], level+1)
        divide(s[2:], level+1)

divide(line)
plot.gca().invert_yaxis()
plot.show()