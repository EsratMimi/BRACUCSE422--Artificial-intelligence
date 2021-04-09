import pylab
import numpy

x = numpy.linspace(-20,20,1000) # 100 linearly spaced numbers
v=pylab. sin(x)**2

y = numpy. log(1 / v) # computing the values

# compose plot
pylab.plot(x,y) # ln(1/pow(cos(x),2))
pylab.plot(x,y,'co') # same function with cyan dots
#pylab.plot(x,2*y,x,3*y) # 2*sin(x)/x and 3*sin(x)/x
pylab.show() # show the plot


# for cos
x = numpy.linspace(-20,20,1000) # 100 linearly spaced numbers
v=pylab. cos(x)**2

y = numpy. log(1 / v) # computing the values

# compose plot
pylab.plot(x,y) # ln(1/pow(cos(x),2))
pylab.plot(x,y,'co') # same function with cyan dots
#pylab.plot(x,2*y,x,3*y) # 2*sin(x)/x and 3*sin(x)/x
pylab.show() # show the plot


