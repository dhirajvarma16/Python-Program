
'''
Created on Jul 24, 2017

@author: Dhiraj varma
'''
m=10
for i in range(1,10):
    m= m*i
print m
sum1=0    
while(m > 0):
    z=m%10
    sum1 +=z
    m=m//10
print sum1
