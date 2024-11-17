# even and odd method with 5 -  read number 10 and 11.

def main():
    x = int(input("What's x? "))
    if is_even(x):
           print("Even")    
    else:
        print("Odd")
        
def is_even(n):
    return True if n % 2 == 0 else False

# shorther version of is_even definition would be return n % 2 == 0

main()