x=50
y=10
z=20
"""
Performing the 
addition funtion

"""
#performing addition funtion
result = x + y + z
print("addition of numbers is:", result)

a = "Doremon"
b = "Shinchan"
c = "Bangtan"

print(a,b,c, sep='\n')

x = "amazing"

def myfunc():
    x = "its A bit difficult"
    print("Pyhton is not as easy as expected " + x)
myfunc()
print("python is " + x)
def myfunc():
    global x
    x = "Global variable inside the function"
myfunc()
    
print("Using global variable inside the function " + x)