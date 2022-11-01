#!/usr/bin/python3
"""Defines the AirBnB Console"""
import cmd
import re
import os
import sys
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


def parse(arg):
    braces = re.search(r"\{(.*?)\}", arg)
    bracket = re.search(r"\[(.*?)\]", arg)
    if braces is None:
        if bracket is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:bracket.span()[0]])
            ret = [i.strip(",") for i in lexer]
            ret.append(bracket.group())
            return ret
    else:
        lexer = split(arg[:braces.span()[0]])
        ret = [i.strip(",") for i in lexer]
        ret.append(braces.group())
        return ret


class AirBnBCommand(cmd.Cmd):
    """Defines the AirBnB Command console
    Attributes:
        prompt (str): The command prompt for Airbnb console project
    """
    prompt = "(hbnb)"
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
                command = [modules[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argDict.keys():
                    call = "{} {}".format(modules[0], command[1])
                    return argDict[command[0]](call)
        print(" *** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Create a new class instance for the User and print its Id"""
        new_user = parse(arg)
        if len(new_user) == 0:
            print("** class name missing **")
        elif new_user[0] not in AirBnBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(new_user[0])().id)
            storage.save()

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print("")
        return True

    def do_show(self, arg):
        """Display the string representation of a
           class instance of a given id.
        """
        user = parse(arg)
        objDict = storage.all()
        if len(user) == 0:
            print("** class name missing **")
        elif user[0] not in AirBnBCommand.__classes:
            print("** class doesn't exist **")
        elif len(user) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(user[0], user[1]) not in objDict:
            print("** no instance found **")
        else:
            print(objDict["{}.{}".format(user[0], user[1])])

    def do_destroy(self, arg):
        """Delete  a class instance of a given ID"""
        user = parse(arg)
        objDict = storage.all()
        if len(user) == 0:
            print("** class name missing **")
        elif user[0] not in AirBnBCommand.__classes:
            print("** class doesn't exist **")
        elif len(user) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(user[0], user[1]) not in objDict.keys():
            print("** no instance found **")
        else:
            del objDict["{}.{}".format(user[0], user[1])]
            storage.save()

    def do_all(self, arg):
        """Display string representation of all instance of a given class.
           if no class is specified, display all instantiated objects
        """
        usersObj = parse(arg)
        if len(usersObj) > 0 and usersObj[0] not in AirBnBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj1 = []
            for user in storage.all().values():
                if len(usersObj) > 0 and usersObj[0] == user.__class__.__name__:
                    obj1.append(user.__str__())
                elif len(usersObj) == 0:
                    obj1.append(user.__str__())
            print(obj1)

    def do_count(self, arg):
        """Count the number of instance of a given classes"""
        usersObj = parse(arg)
        count = 0
        for user in storage.all().values():
            if usersObj[0] == user.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Update a class instance of a given ID by adding or updating
           a given attribute keys/values pair or dictionary
        """

        user = parse(arg)
        objDict = storage.all()
        if len(user) == 0:
            print("** class name missing **")
            return False
        if user[0] not in AirBnBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(user) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(user[0], user[1]) not in objDict.keys():
            print("** no instance found **")
            return False
        if len(user) == 2:
            print("** attribute name missing **")
            return False
        if len(user) == 3:
            try:
                type(eval(user[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(user) == 4:
            obj = objDict["{}.{}".format(user[0], user[1])]
            if user[2] in obj.__class__.__dict__.keys():
                valType = type(obj.__class__.__dict__[user[2]])
                obj.__dict__[user[2]] = valType(user[3])
            else:
                obj.__dict__[user[2]] = user[3]
        elif type(eval(user[2])) == dict:
            obj = objDict["{}.{}".format(user[0], user[1])]
            for k, v in eval(user[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valType = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valType(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    AirBnBCommand().cmdloop()
