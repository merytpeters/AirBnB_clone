#!/usr/bin/python3
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
    def do_create(self):
        """creates a new instance of BaseModel, saves it and prints the Id"""
        pass
    def do_show(self):
        """prints the string representation of an instance.
           On the class name and Id. 
        """
        pass
    def do_destroy(self):
        """deletes an instance based on class name and id."""
        pass
    def do_all(self):
        """prints all string representation of all instances.
            it can be based on or not on the class name.
        """
        pass
    def update(self):
        """updates an instance based on the class name and id.
            this is by adding or updating attributes.
        """
        pass

if __name__=='__main__':
    HBNBCommand().cmdloop()
