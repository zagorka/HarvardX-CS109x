""""
x = input("Whatt's X? ")
y = input("What's Y? ")
z = int(x) + int(y)

print (z)

"""

# Nsting functioins  - instead of calliing a variabl, we are going to wrap verything into integer

"""
x = int(input("what's x? "))
y = int(input("what's y? "))

print(x + y)
"""


# Next lession is about float - floating value with decimal numbers

"""
x = float(input("what's x? "))
y = float(input("what's y? "))

print(x + y)

"""

# Next lession is about intenger - int
# In ducumenation is round(number {, [ndigits]})
# function round takes one parmtar - one number -  coma meanse how many digits do you want that number to round to
#floats can't represent digits nubers indefnitelly, right now it's rounding ok for us, but it will be presened as fundamental problems 
# Example of addiig

"""
x = float(input("what's x? "))
y = float(input("what's y? "))

z = round(x + y)

print(f"{z:,}")
"""

# Eample of dividion with round

"""
x = float(input("what's x? "))
y = float(input("what's y? "))

z = round( x / y, 2)

print(z)

"""

# Eemaple woth function

"""
x = float(input("what's x? "))
y = float(input("what's y? "))

z = x / y

print(f"{z:.2f}")
"""

# For definitions we return to hello.py
# Definitions are demonstrated in hello.px. return wii be exampled here

"""
def main():
    int(input("What is x? "))
    
def square(n):
    return n * n
    
"""