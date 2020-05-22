#T: Test Class
#P: Consists of various functions and syntax to test the autoDoc 
class MyClass:
#sT: Constructor.
#P: Takes in the x,y and z parameters that signify other parameters feed into python functions
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

#sT: my_function
"""
P: Prints out hello world
"""
    def my_function(self):
        print("Hello world")
    
#sT:add function
#P: This is a static method that adds 2 parameters given to it
    @staticmethod
    def add(a,b):
        return a+b

'''
    Python is a good programming language
'''