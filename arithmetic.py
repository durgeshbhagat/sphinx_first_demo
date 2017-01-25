#!usr/bin/python -tt

''' This file provides function for the basic arithmetic operation of two integers 
  - Sphinx Demo containing just bunch of functions


'''
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
    parser = optparse.OptionParser()
    parser.add_option("-a", dest="a",type="int", help="First Integer", default=1)
    parser.add_option("-b", dest="b",type="int", help="Second Integer", default=2)
    (options, args) = parser.parse_args()
    #if not (options.filename or options.corpus): parser.error("need corpus filename(-f) or corpus range(-c)")
    c = add(options.a,options.b) 
    print ' Addition of  %d and %d is  %d ' %(options.a,options.b,c)
    #pass
    

if __name__ == '__main__':
    main() 
