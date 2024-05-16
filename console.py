#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    intro = 'welcome to the console'
    prompt = "(hbnb)"
    

    def do_cmdloop(self):
        """parse through the line when a command is entered."""

    def do_quit(self, args):
        print('instructions on how to quit: press q then enter')
    def do_EOF(self, line):
        return True
    def do_greet(self, person):
        """greet the person mentioned."""
        self.person = person
        if person:
                print(f"hello {self.person}")

if __name__=='__main__':
    HBNBCommand().cmdloop()
