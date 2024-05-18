#!/usr/bin/python3
"""The entry point of the command line."""


from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Prints help message for the quit command."""

        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """when an EOF is met it goes to a new line """
        print()
        return True

    def emptyline(self):
        """Don't execute anything on empty line"""

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
