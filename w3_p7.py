#Shiv Subedi
#This snippet of code computes the collatz function for a given input number 'num'

def collatz (num):
    """
    This function computes the collatz function for a given input number num
    """
    rem = num % 2
    if rem == 0:
        function = num//2
    else:
        function = num*3 + 1
    return function

num = 859
print("Value of the Collatz function =",collatz(num))

#takes the functional value of the collatz function as input from second time
#num=collatz(num)
#print("Value of the Collatz function =",num)
#print("Value of the Collatz function =",collatz(num))
