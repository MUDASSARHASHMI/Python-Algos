__author__ = 'Mudassar'

from scipy import stats
import numpy as np
from matplotlib import pyplot as plt

# Size of the houses
x = np.array([112, 345, 190, 305, 372, 550, 302, 420, 570])
# Prizes of houses
y = np.array([1120, 1523, 2102, 2230, 2600, 3200, 3409, 3689, 4460])

slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.plot(x, y, 'ro', color='black')
plt.xlabel('Sizes of Houses')
plt.ylabel('Prices of Houses')

# After we calculated lets generate the regression line
plt.plot(x, x*slope+intercept, 'b')# 'b' here is just the blue color for line
plt.axis([0, 600, 0, 5000])
plt.plot()
plt.show()

# Lets make a prediction based on above
newValueX = 200
newValueY = newValueX*slope+intercept

print(newValueY)

# Result will show predicted price 1846.20911765.