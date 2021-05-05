class Calculator:
    """
    Calculator
       - add()
       - subtract()
       - multiply()
       - divide()
       - nthRoot()
       - reset()
    
    x (int) : decimal number (required)
    y (int) : decimal number (not required)
    
    for example:
        Calculator.add(2,4)
        answer: 6
        Calculator.add(4)
        answer: 10
    
    """
    
    result=0                               # Calculator saves result
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def add(x:int=0,y:int=None) -> int:
        """Use the sum formula"""
        if y==None:
            answer = (x+Calculator.result)  
        else:
            answer = (x+y)                  
        Calculator.result=answer            # save answer to the memory
        return answer
    
    def subtract(x:int=0,y:int=None) -> int:
        """Use the subtract formula"""
        if y==None:
            answer = (Calculator.result-x)   
        else:
            answer = (x-y)
        Calculator.result=answer            # save answer to the memory
        return answer
    
    def multiply(x:int=0,y:int=None) -> int:
        """Use the multiply formula"""
        if y==None:
            answer = (x*Calculator.result)
        else:
            answer = (x*y)
        Calculator.result=answer            # save answer to the memory
        return answer
    
    def divide(x:int=0,y:int=None) -> int:
        """Use the divide formula"""
        if y==None:
            answer = (Calculator.result/x)
        else:
            answer = (x/y)
        Calculator.result=answer            # save answer to the memory
        return answer
    
    def nthRoot(x:int=0,y:int=None) -> int:
        """
        Use the root formula:
        Take (n) root of number
        """
        if y==None:
            answer = Calculator.result**(1/float(x))
        else:
            answer = x**(1/float(y))
        Calculator.result=answer            # save answer to the memory
        return answer
    
    def reset() -> int:
        """Use the reset function to reset calculator's memory to 0"""
        Calculator.result=0                 # clean memory/ assign to 0
        return Calculator.result