#Shiv Subedi
#This snippet of code shows how to return values from quadratic expression

def quad_fun(x):
    """
    Returns the value of the quadratic expression
    """
    function = -5*(x**5) + 67*(x**2) - 47
    return function

f_0 = quad_fun(0)
f_1 = quad_fun(1)
f_2 = quad_fun(2)
f_3 = quad_fun(3)
print("f(0):",f_0)
print("f(1):",f_1)
print("f(2):",f_2)
print("f(2):",f_3)
