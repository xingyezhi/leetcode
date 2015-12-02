__author__ = 'lenovo'
# coding=utf-8

a=[]
b=[0]
map={}
for i in range(3):
    b[0]=i
    a.append(b)
b[0]=99
b=[100]
print a
print b
map[0]=a
a=[]
print map