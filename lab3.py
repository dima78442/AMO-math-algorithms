
# coding: utf-8

# In[26]:


from math import *


# In[27]:


matrix2 = [ [ 6, 3, 11, 17, 155 ],
         [ 0, 16, 5, 10, 161 ],
         [ 11, 5, 25, 8, 147 ],
         [ 5, 5, 11, 15, 151 ] ] 
matrix = [ [ 32, 3, 11, 17, 259 ],
          [ 0, 16, 5, 10, 161 ],
          [ 11, 5, 25, 8, 147 ],
          [ 5, 5, 11, 22, 193 ] ]
N = 4
esp = 1e-06;

print(matrix2)


# In[28]:


def directIterationMethod():
    A = [[0 for x in range(0,N)]for x in range(0,N)]
    X = [0 for x in range(0,N)]
    Xk = [0 for x in range(0,N)]
    B = [0 for x in range(0,N)]
    q = 0
    
    
    for i in range(N):
        X[i] = matrix[i][N] / matrix[i][i]
        B[i] = X[i]
        Xk[i] = 0
    for i in range(N):
        for j in range(N):
            if (i != j):
                A[i][j] = -matrix[i][j] / matrix[i][i]
            else:
                A[i][j] = 0



    for i in range(N):
        sum = 0;
        for j in range(N):
            sum += abs(A[i][j])
        if(sum > q):
            q = sum
    
    for i in range(N):
        sum = 0
        for j in range(N):
            if(i != j):
                sum += A[i][j] * X[j]
        Xk[i] = B[i] + sum;


    while(True):
        for i in range(N):
            sum = 0;
            for j in range(N):
                if(i != j):
                    sum += A[i][j] * X[j]
            Xk[i] = B[i] + sum;


        norm = 0;
        
        for i in range(N):
            sum = 0;
            for j in range(N):
                sum += abs(Xk[j] - X[j])
            if (sum > norm):
                norm = sum

        if (norm <= abs(esp*(1 - q) / q)):
            break
        for i in range(N):
            X[i] = Xk[i];

    print("DIRECT ITERATION")
    print("x0")
    print(X[0])
    print("x1")
    print(X[1])
    print("x2")
    print(X[2])
    print("x3")
    print(X[3])


# In[29]:


def GaussianEliminationMethod():
    for i in range(N):
        
        x_zero = matrix2[i][i];
        x_one = matrix2[(N - 3 + i) % N][i]
        x_two = matrix2[(N - 2 + i) % N][i]
        x_three = matrix2[(N - 1 + i) % N][i]
        
        for j in range(N - 4 + i,N + 1,1):
            matrix2[i][j] = matrix2[i][j] / x_zero;
            matrix2[(N - 3 + i) % N][j] -= matrix2[i][j] * x_one;
            matrix2[(N - 2 + i) % N][j] -= matrix2[i][j] * x_two;
            matrix2[(N - 1 + i) % N][j] -= matrix2[i][j] * x_three;

    print("Gaussian Elimination")
    print("x0")
    print(matrix2[0][N])
    print("x1")
    print(matrix2[1][N])
    print("x2")
    print(matrix2[2][N])
    print("x3")
    print(matrix2[3][N])


# In[30]:


def main():
    directIterationMethod()
    GaussianEliminationMethod()
main()

