#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self,arg):
        """Quit command to exit the program."""
        return True
    
    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)
    
    def do_EOF(self,arg):
        """Quit command to exit the program."""
        return True
    
    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()