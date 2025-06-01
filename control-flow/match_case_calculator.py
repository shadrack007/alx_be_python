numb1  =  int(input("Enter the first number: "))
numb2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        result = numb1 + numb2
    case '-':
        result = numb1 - numb2
    case '*':
        result = numb1 * numb2
    case '/':  
        if numb2 != 0:
            result = numb1 / numb2
        else:
            result = "Can not divide by zero."
    case _:
        result = "Error: Invalid operation."
print(f"The result is {result}")
