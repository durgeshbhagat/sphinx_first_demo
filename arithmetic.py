#!usr/bin/python -tt

''' This file provides function for the basic arithmetic operation of two integers '''

####------------- Import Module -------
import os
import sys
import optparse



def add(a, b):
    ''' return the addition of integer a and b '''
    return a+b 
    #pass
def sub(a,b):
    ''' return the substarction of two integer a and b'''
    return a-b
    #pass
    
    
def mult(a,b):
    ''' return the multiplication of two integer a and b '''
    return a*b    
    #pass

def divide(a,b):
    ''' return the divison of two integer a and b '''
    if b==0:
        print ' Divide by Zero '
        return None
    return (a/b, a%b)
    #pass 
    
    
def main():
    '''  Call to different arithmetic function eg: add, sub, mult, divide '''
    
    
    pass
    

if __def__ == '__main__':
    main() 
