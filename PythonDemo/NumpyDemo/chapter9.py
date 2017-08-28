
import numpy as np    
import matplotlib.pyplot as plt    

"""
polynomical with poly1d function of numpy
"""
func  = np.poly1d( np.array([1,2,3,4,5,6,7]).astype(float) )
func1 = func.deriv(m=1)
func2 = func.deriv(m=2)

print(func)

x = np.linspace( -10, 10, 200 )

y = func(x)
y1= func1(x)
y2= func2(x)

fit = plt.figure()

print( func(2) )

plt.subplot(311)
plt.plot(x,y, 'ro', x, y1, 'b-', x, y2, 'g+')

plt.xlabel('x')
plt.ylabel('y(x)')

plt.show()
