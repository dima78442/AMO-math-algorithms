
# coding: utf-8

# In[102]:


from math import *


# In[103]:


def function(x):
    return exp(x) - 3*cos(2*x) + 2*x + 1


# In[104]:


def first_dirivative_func(x):
    return exp(x) + 6*sin(2*x)+2;


# In[105]:


def second_derivative_func(x):
    return exp(x)+12*cos(2*x)


# In[106]:


def frange(start, stop, step):
    x = start
    while x <= stop:
        yield x
        x += step


# In[107]:


def frange_strict(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


# In[108]:


def xrange(start, stop, step):
    x = start
    while x >= stop:
        yield x
        x *= step


# In[109]:


def roots_isolation(mezha1, mezha2, step, mas):
    
    i = -1;
    a = 0.0;
    
    for a in frange(mezha1,mezha2 + 0.1,step):
        if (function(a) * function(a + step) < 0):
            i = i + 1
            mas.append(a)
    return i


# In[110]:


def iteration (mas, step, nmbr_roots):
    
    
    n_it = [];
    
    for i in range(nmbr_roots + 1):
        print("{0:22} | {1:20} | {2:20}".format("EPS", "ROOT", "ACCURATELY " + str(i+1)))
        a = mas[i]
        b = a + step;
        
        if (abs(first_dirivative_func(a)) > abs(first_dirivative_func(b))):
            M = first_dirivative_func(a)
            m = first_dirivative_func(b)
        else:
            M = first_dirivative_func(b);
            m = first_dirivative_func(a);
        
        alfa = 1/M
        q = 1 - abs(m/M)
        
        for eps in xrange(1e-2,1e-14,1e-3):
            x = (b+a)/2
            x1 = x
            n = 0
            n = n + 1;
            x = x1;
            x1 = x - alfa*function(x);
            while (abs(x1-x) > (1-q)/q*eps):
                n = n + 1;
                x = x1;
                x1 = x - alfa*function(x)
            if (i == 0):
                n_it.append(n)
            print("{0:22} | {1:20} | {2:20}".format(eps, x1, abs(fabs(x1)-fabs(x))*q/(1-q)))
        
    return n_it


# In[111]:


def tangent (mas, step, nmbr_roots ):
    
    n = 0
    n_tan = []
    
    for i in range(nmbr_roots + 1):
        print("{0:22} | {1:20} | {2:20}".format("EPS", "ROOT", "ACCURATELY " + str(i+1)))
        a = mas[i];
        b = a + step;
        
        m = abs(first_dirivative_func(a));
        for x1 in frange_strict(a,b,0.001):
            if (abs(first_dirivative_func(x1)) <= m):
                m = abs(first_dirivative_func(x1))
        if (function(a) * second_derivative_func(a) > 0):
            x1 = a
        else:
            x1 = b
        
        for eps in xrange(1e-2,1e-14,1e-3):
            x = x1
            n = 0
            while (abs(function(x))/m > eps):
                n+=1
                x -= function(x)/first_dirivative_func(x)
            if i == 0:
                n_tan.append(n)
            print("{0:22} | {1:20} | {2:20}".format(eps, x, abs(function(x))/m))
          
    return n_tan


# In[112]:


if __name__ == "__main__":
    mas = [];
    n_it,n_tan = [],[]
    i,k = 0,0;
    step = 0.5;
    p = 1e+1;
    
    k = roots_isolation (-10,10,step,mas);
    
    print("                iteration:     \n");
    n_it = meth_iteration(mas,step,k);
    print("---------------------------------------------------------------------\n\n");
    
    print("                tangent:     \n");
    n_tan = tangent(mas,step,k);
    print("---------------------------------------------------------------------\n\n");
    
    print(" EPS     ITERATION    TANGENT \n\n"  );
    for index in range(5):
        p = p/1000
        print("{0:22} | {1:20} | {2:20}".format(p,n_it[index],n_tan[index]))

