#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    intro = 'welcome to the console'
    prompt = "(hbnb)"
    

    def do_quit(self, line):
        """to quit the commadline interpter use the command quit."""
        self.line = line
        return True
    
    def do_EOF(self, line):
        """when an EOF is met it goes to a new line """
        self.line = line
        print()
        return True

if __name__=='__main__':
    HBNBCommand().cmdloop()
