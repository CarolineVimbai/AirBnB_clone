#!/usr/bin/python

import sys
#sys.path.append("..")

import cmd
import datetime
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    __current_datetime = datetime.datetime.now()
    intro = "Welcome to the hbnb command line. The current time is " + __current_datetime.isoformat()
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        #raise SystemExit
        return True

    def do_EOF(self, args):
        """Quit command to exit the program"""
        return True
    
    # hidden method ( to prevent 'undocumented commands error in console' when the 'Enter' key is pressed )
    def do_enter(self, args):
        if len(args) == 0:
            return True
        
    def do_create(self, *args):
        """Creates a new instance of BaseModel class"""
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != BaseModel().__class__.__name__:
            print("** class does not exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, *args):
        """Prints the string representation of an instance based on the class name and id"""
        print(args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != BaseModel().__class__.__name__:
            print("** class name does not exist **")
        else:
            pass

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id"""
        pass 

    def do_all(self, *args):
        """Prints all string representation of all instances based or not on the class name."""
        pass

    def do_update(self, *args):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
