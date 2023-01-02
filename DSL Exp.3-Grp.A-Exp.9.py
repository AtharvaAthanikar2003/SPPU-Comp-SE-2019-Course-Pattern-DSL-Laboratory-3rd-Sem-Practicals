'''
Write a python program to compute following computation on matrix:
a) Addition of two matrices
b) Subtraction of two matrices
c) Multiplication of two matrices
d) Transpose of a matrix
'''


import numpy as np
print("For Matrix 1 :- ")
m=int(input("Enter the number of rows :- "))
n=int(input("Enter the number of columns :- "))
print("Enter the elements row-wise :- ")
matrix1=[];
for i in range(m):
    a=[]
    for j in range(n):
        v=int(input())
        a.append(v)
    matrix1.append(a)
print(matrix1)
print("For Matrix 2 :- ")
m1=int(input("Enter the number of rows :- "))
n1=int(input("Enter the number of columns :- "))
print("Enter the elements row-wise :- ")
matrix2=[];
for i in range(m1):
    a1=[]
    for j in range(n1):
         v=int(input())
         a1.append(v)
    matrix2.append(a1)
print(matrix2)
print("Addition of the two matrices is :- ",np.add(matrix1,matrix2))
print("Subtraction of the two matrices is :- ",np.subtract(matrix1,matrix2))
print("Multiplication of the two matrices  :- ",np.multiply(matrix1,matrix2))
print("Division of the two matrices is :- ",np.divide(matrix1,matrix2))
print("Transpose of Matrix 1 is :- ",np.transpose(matrix1))
print("Transpose of Matrix 2 is :- ",np.transpose(matrix2))
