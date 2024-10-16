import sys
from calculator.arithmetic_operations import add
from app.commands import Command
from calculator import full_calc

class AddCommand(Command):
    def execute(self):