import numpy as np

def cholesky(a):
 a = np.array(a, float)
 L = np.zeros_like(a)
 n,_ = np.shape(a)
 for j in range(n):
   for i in range(j,n):
     if i == j:
       L[i,j] = np.sqrt(a[i,j]-np.sum(L[i,:j]**2))
     else:
       L[i,j] = (a[i,j] - np.sum(L[i,:j]*L[j,:j])) / L[j,i]
 return L

def solveLU(L, U, b):
 L = np.array(L, float)
 U = np.array(U, float)
 b = np.array(b, float)
 n,_=np.shape(L)
 y = np.zeros(n)
 x = np.zeros(n)
   for i in range(n):
     y[i] = (b[i]-np.sum(L[i,:i] * y[:i]))/L[i, i]
   for i in range(n-1,-1,-1):
     x[i] = (y[i]-np.sum(U[i,i+1:n] * x[i+1:n]))/U[i,i]
 return x

a = [[8.00, 3.22, 0.8, 0.00, 4.10],
 [3.22, 7.76, 2.33, 1.91, -1.03],
 [0.8, 2.33, 5.25, 1.00, 3.02],
 [0.00, 1.91, 1.00, 7.50, 1.03],
 [4.10, -1.03, 3.02, 1.03, 6.44]]
b = [9.45, -12.20, 7.78, -8.1, 10.0]
l = cholesky(a)
x = solveLU(l,np.transpose(l),b)
print(x)
print(np.linalg.solve(a,b))