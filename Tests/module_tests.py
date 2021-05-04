# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:23:17 2021

@author: greta
"""

from calculator import Calculator           #Importing calculator module

def test_add():
    assert Calculator.add(2,7) == 9 

def test_subtract():
    assert Calculator.subtract(10,7) == 3 

def test_multiply():
    assert Calculator.multiply(2,7) == 14 

def test_divide():
    assert Calculator.divide(8,2) == 4
    
def test_nthRoot():
    assert Calculator.nthRoot(9,3) == 3
    
def test_reset():
    assert Calculator.reset() == 0

if __name__ == "__main__":
    test_add()
    print("Everything passed")

