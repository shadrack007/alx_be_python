class SimpleCalculator:
    def addition(self, num1, num2):
        try:
            result = num1 + num2
            return result
        except ValueError:
            return f'Error: Provide valid number'
    
    def multiply(Self, num1, num2):
        try:
            result = num1 * num2
            return result
        except ValueError:
            return f'Error: Provide valid number'
    
    def subtract(self, num1, num2):
        try:
            result = num1 - num2
            return result
        except ValueError:
            return f'Error: Provide valid number'
    
    
    def divide(Self, num1, num2):
        try:
            result = num1 / num2
            return result
        except ZeroDivisionError:
            return 'Error: can not divide by zero'
        
        except ValueError:
            return 'Error: Provide Valid numbers'

   