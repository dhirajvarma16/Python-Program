'''
Created on Jul 18, 2017

@author: Dhiraj varma
'''
nums = range(2,50)
for i in range (2,8):
    numbs = filter(lambda x:x == i or x%i, nums)
    print numbs
    
    