def perform_operation(numb1, numb2, operation):
    match operation:
        case 'add':
            result = numb1 + numb2
        case 'subtract':
            result = numb1 - numb2
        case 'multiply':
            result = numb1 * numb2
        case 'divide':
            if numb2 == 0:
                return "You can not divide by zero"
            result = numb1 / numb2
        case _:
            return 'Unknown operation specified'
    return result
            
        