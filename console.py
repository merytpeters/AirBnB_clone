#!/usr/bin/python3

import cmd, sys

class HBNBCommand(cmd.Cmd):
    intro = 'welcome to the console'
    prompt = "(hbnb)"
    

def do_cmdloop(self):
    pass
def help(self):
    
    'provides the cmd loop'
    pass
def do_quit(self, args):
    'instructions on how to quit: press q then enter'
    pass
def EOF(self):
    pass
def do_help(self, args):
    pass


if __name__=='__main__':
    HBNBCommand().cmdloop()
