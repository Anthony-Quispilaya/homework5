from app.commands import CommandHandler
from app.commands.greet import GreetCommand
from app.commands.exit import ExitCommand
from app.commands.menu import MenuCommand

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        
    def start(self):
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("exit", ExitCommand())
        
        print("Type 'greet' for a greeting.")
        print("Type 'menu' for the menu list.")
        print("Type 'exit' to exit.")
        while True:
            self.command_handler.execute_command(input(">>").strip())