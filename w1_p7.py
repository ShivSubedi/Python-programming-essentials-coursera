#Shiv Subedi
#This snippet of code finds the area of equilateral triangle given its length

def area_eq (length):
    """
    This function returns the area of equilateral triangle provided its length
    """
    area = ((3**0.5)/4)*(length**2)
    return area

print ("Area of an equilateral triangle with length 5 =", area_eq(5))
