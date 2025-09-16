# Problem 1 #

def my_gcd(a, b):
    if b == 0:
        return a
    else:
        return my_gcd(b, a % b)

def lcm(a, b):
    return abs(a * b) // my_gcd(a, b)

x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

if x <= 0 or y <= 0:
    print("Error: Please enter positive integers only.")
else:
    print(f"The LCM of {x} and {y} is = {lcm(x, y)}")