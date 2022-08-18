# Example of built in function

s = [2,3,5]
len(s)


from math import sqrt
import  math

sqrt(4)
math.log10(2)


# custom function definition using Key words

def func_1():
    print("running the func_1")

func_1()

# passing argument to function
# note that ther is no type to the argument passed to a function in python but the argument can be annotate

def func_2(a,b):
    return a*b

#sample of annotated function
def func_3(a: int,b: int):
    return a*b

#lamda express is just a nameless functiom
x = 3
lambda x : x**2

print(x)
