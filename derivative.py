import math

def f(x):
    return x*x*x - x*x
#def f(x):
#    return math.sin(x)

def derivative_front(x):
    dx = 0.01
    return (f(x+dx) - f(x))/dx
def derivative_back(x):
    dx = 0.01
    return (f(x) - f(x-dx))/dx
def cut_error(x):
    dx = 0.01
    return(f(x+dx) - f(x-dx))/2*dx + dx*dx

def relative_error(dx,x):
    result = (dx * derivative_front(x))/dx
    if result > 0:
       result = result * 1.0
    elif result < 0:
        result = - result 
    
    print("relative error " + str(result))

"""
def t_error(x):
    tol = 0.001
    dx = 1
    for i in range(1,10):
        dx = dx/2
        der_to = derivative(x)
        der_temp = der_to
        if der_to - der_temp
"""       
    


print(derivative_front(3))
print(derivative_back(3))
print(cut_error(3))
relative_error(0.01, derivative(3))
