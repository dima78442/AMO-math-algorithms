
# coding: utf-8

# In[180]:


from math import *


# In[181]:


a = -1
b = 16
eps = 1e-4


# In[182]:


def integral(x : float):
    return x*sin(2*x)


# In[183]:


def primitive_F(x : float):
    return (-1/2)*x*cos(2*x) + sin(2*x)/4


# In[184]:


def integral_compution(n, a, b):
    
    sum_even = 0.0
    sum_odd = 0.0
    
    n = 2 * ceil(n / 2)
    step = (b - a) / n;
    
    for i in range(1,n,1):
        if i % 2 == 0:
            sum_odd += integral(a + i*step)
        else:
            sum_even += integral(a + i*step)
            
    return step / 3 * (integral(a) + integral(b) + 4 * sum_even + 2 * sum_odd)


# In[185]:


def main():
    Io = primitive_F(b) - primitive_F(a)

    print("interval with points a ={0:1} b ={1:1}".format(a,b))
    print("Newton Leibniz: I = F(b) - F(a) = {0:3}".format(Io))
    print("\n           Simpson Method       \n")
    print("---------------------------------------------------------------------------------\n")
    print("|  epsilon   |           h         |       Integral     |       ABS(module)     |\n")
    print("---------------------------------------------------------------------------------\n")
    
    max_deriv4 = 114.47008286166447
    
    n = 2 * ceil(0.5*(b - a) / (pow((180 * eps / (b - a) / max_deriv4), 0.25)))
    h = (b - a) / n
    abs_err = abs(Io - integral_compution(n, a, b))
    print("| {0:10} | {1:1} | {2:1} | {3:1}|".format(eps, h, integral_compution(n, a, b), abs_err))
    print("---------------------------------------------------------------------------------\n\n")
    
    print("           Runge Method        \n")
    print("---------------------------------------------------------------------\n")
    print("|          delta       |          h         |           ABS         |\n")
    print("---------------------------------------------------------------------\n")
    n = ceil((b - a) / sqrt(sqrt(abs_err)))
    h = (b - a) / n;

    In = integral_compution(n, a, b)
    I2n = integral_compution(2 * n, a, b)
    r = abs(In - I2n) / 15

    while (r > abs_err):
        n *= 2
        In = I2n
        I2n = integral_compution(2 * n, a, b)
        r = abs(In - I2n) / 15
        
    print("| {0:12} | {1:1} | {2:1} |".format(abs_err, h, abs(Io - I2n)))
    print("---------------------------------------------------------------------\n\n")
main()

