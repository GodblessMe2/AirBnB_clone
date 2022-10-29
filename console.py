#!/usr/bin/python3
"""Defines the AirBnB Console"""
import cmd
import imp
import re
from shlex import split
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


def parse(arg):
    braces = re.search(r"\{(.*?\)}", arg)
    bracket = re.search(r"\{(.*?\)}", arg)
    if braces is None:
        if bracket is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:bracket.span()[0]])
            ret = [i.strip(",") for i in lexer]
            ret.append(bracket.group())
            return ret
    else:
        lexer = split(arg[:bracket.span()[0]])
        ret = [i.strip(",") for i in lexer]
        ret.append(braces.group())
        return ret


class AirBnBCommand(cmd.Cmd):
    """Defines the AirBnB Command console
    Attributes:
        prompt (str): The command prompt for Airbnb console project
    """
    prompt = "(abnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Return nothing when an empty line is receive"""
        pass

    def default(self, arg):
        """Default behavior CMD module"""
        argDict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            modules = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", modules[1])
            if match is not None:
                command =[modules[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argDict.keys():
                    call = "{} {}".format(modules[0], command[1])
                    return argDict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False
    
    def do_quit(self, arg):
        """Exit the command program"""
        return True
    
    def do_create(self, arg):
        """Create a new class instance for the User and print its Id"""
        new_user = parse(arg)
        if len(new_user) == 0:
            print("** class name missing **")
        elif new_user[0] not in AirBnBCommand.__classes:
            print("** Class doesn't exist **")
        else:
            print(eval(new_user[0]().id))
            #storage.save()
    
    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True
    
    def do_show(self, arg):
        """Display the string representation of a class instance of a given id"""
        user = parse(arg)
        objDict = storage.all()
        if len(user) == 0:
            print("** class name missing **")
        elif user[0] not in AirBnBCommand.__classes:
            print("** Class doesn't exist **")
        elif len(user) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(user[0], user[1]) not in objDict:
            print("** No instance found **")
        else:
            print(objDict["{}.{}".format(user[0], user[1])])

if __name__ == "__main__":
    AirBnBCommand().cmdloop()
