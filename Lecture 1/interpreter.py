#ask user for arithetic expression
#calculates and outputs result as floating-point value
#formatted to one decimal place.
#assume input will be formatted as "x y z" with one space between each.
#x is an integer, y is +,-,*,/, z is an integer

def main():
    x, y, z = (input("please input a math equation: ").strip().split(" "))
    x = float(x)
    z = float(z)

    if y == "+":
        addition(x,z)
    elif y == "-":
        subtraction(x,z)
    elif y == "/":
        division(x,z)
    elif y == "*":
        multiplication(x,z)
    else:
        print("please input a valid equation")

def addition(num_1, num_2):
    print(num_1 + num_2)

def subtraction(num_1, num_2):
    print(num_1 - num_2)

def division(num_1, num_2):
    print(num_1 / num_2)

def multiplication(num_1, num_2):
    print(num_1 * num_2)

main()
