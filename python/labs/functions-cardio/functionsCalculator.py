print("Welcome to Elpollotonios Functions Calculator")
num1 = int(raw_input("Give me a number: "))
num2 = int(raw_input("Give me a number: "))

def myAddFunction(add1, add2):
    sum = add1 + add2
    return sum

print("Here is the sum: " + str(myAddFunction(num1, num2)))

def mySubFunction(sub1, sub2):
    difference = sub1 - sub2
    return difference

 print("Here is the difference: " + str(mySubFunction(num1, num2)))

def myMultFunction(pro1, pro2):
    product = pro1 * pro2
    return product

print("Here is the product: " + str(myMultFunction(num1, num2)))
