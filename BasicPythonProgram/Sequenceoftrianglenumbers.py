'''
Created on Jul 24, 2017

@author: Dhiraj varma
'''
f=open("names.txt")
string = f.readlines()
print string
f.close()

x=str(string).split(",")
print x
list1 =[]
sumword=0
def addword(x):
    
    for letter in x:
        if letter == "A": sumword += 1
        elif letter == "B": sumword += 2
        elif letter == "C": sumword += 3
        elif letter == "D": sumword += 4
        elif letter == "E": sumword += 5
        elif letter == "F": sumword += 6
        elif letter == "G": sumword += 7
        elif letter == "H": sumword += 8
        elif letter == "I": sumword += 9
        elif letter == "J": sumword+= 10
        elif letter == "K": sumword += 11
        elif letter == "L": sumword += 12
        elif letter == "M": sumword += 13
        elif letter == "N": sumword += 14
        elif letter == "O": sumword += 15
        elif letter == "P": sumword += 16
        elif letter == "Q": sumword += 17
        elif letter == "R": sumword += 18
        elif letter == "S": sumword += 19
        elif letter == "T": sumword += 20
        elif letter == "U": sumword += 21
        elif letter == "V": sumword += 22
        elif letter == "W": sumword += 23
        elif letter == "X": sumword += 24
        elif letter == "Y": sumword += 25
        elif letter == "Z": sumword += 26
        else: sumword += 0
    
