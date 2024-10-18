from app.commands import Command
from calculator.arithmetic_operations import subtract

class SubtractCommand(Command):
    def execute(self):
        
        # User enters two number, (automatically float type)
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = subtract(a, b)
    
            print(f"The result of {a} - {b} = {result}")
        
        # Error if user does not enter float type
        except ValueError:
            print("Please enter valid numbers.")
