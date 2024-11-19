"""
name = input("What's your name? ")
print ("hello, ")
print (name)

testing commentts
for multiple lines

"""
# Shortcut fir string str +vwhen suing print function it automatically  goes into a new line
# Print(*objects, sep'', end='\end") these are parametars what you can add to the function, but when you add vslues those are functional parameters
# Named paramerars example end='"\end" chaange to end= "????"

# If we wantv to pass second parantasies, fo example sarcasticly say firendd it would loook like:


"""

print('Hello, "friend"')

"""
# There is another method called escapng

"""

print("Hello, \"friend\"")

"""

# For formating string we will use F (function) {stringnae}

"""
name = input("What's your nanme")
print(f"hello, {name}")

"""

# When we have alot of extra spacing we are going to call str
# Eample in next line- we are using .strip() to remove extra white spcace

"""

#name = input("What's your name? ")
#name = name.strip()
#print(f"Hello, {name}")

"""
# Capitalizing letter
# The next practice is to capitalite name in case it's lower case 

"""
name = input("What's your name? ")
name = name.strip()
name = name.capitalize()
print(f"Hello, {name}")

"""

# For capitalizing all the letters we are going to use function title()

"""
name = input("What's your name? ")
name = name.title()
print(f"Hello, {name}")
"""

# For shortening entire string method we can place everything in the same line - use dont . - don't forget that

"""
name = input("What's your name? ").strip().title()

print(f"Hello, {name}")

"""

# Next is we use .split function like .strip()

"""
name = input("What's your name").strip().title()

firstlast = name.split(" ")

print(f"Hello, {name}")
hello(to="world")

"""

# Defining function for example word hello added also variation as this def  and aksi demonstration if definition is somwhere ver down bellow

"""
def hello(to):
    print("hello,", to)

name = input("What0ss your name?")
hello(name)

"""
# in order to fix this we wil use main example as below

"""
def main():
    name = input("Whats your name?")
    hello(name)
    
def hello(to="world"):
     print("hello,", to)
     
main()

"""
# return value is in documet calculator.py