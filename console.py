<<<<<<< HEAD
#!/usr/bin/env python3
import cmd
import re
from shlex import split
=======
#!/usr/bin/python3
"""cmd class to command line interprete"""
import re
import models
import json
import cmd
>>>>>>> 46d5a0696a3f029edb62d03c94ef9868c18cacbd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

<<<<<<< HEAD
=======

>>>>>>> 46d5a0696a3f029edb62d03c94ef9868c18cacbd
def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

<<<<<<< HEAD

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
=======
class HBNBCommand(cmd.Cmd):
    """cmd class to command line interprete"""
    prompt = '(hbnb) '
>>>>>>> 46d5a0696a3f029edb62d03c94ef9868c18cacbd
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
<<<<<<< HEAD

=======
    
>>>>>>> 46d5a0696a3f029edb62d03c94ef9868c18cacbd
    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

<<<<<<< HEAD
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)"""
        print("")  # Print a newline for better formatting
=======
    def do_EOF(self, arg):
        """handles end of file"""
        print ()
        return True
   
    def emptyline(self):
        """don't do anything for emptyline"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
>>>>>>> 46d5a0696a3f029edb62d03c94ef9868c18cacbd
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

<<<<<<< HEAD
    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        args = parse(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            print(eval(class_name)().id)
            new_instance.save()
        
=======
    def my_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_create(self, arg):
        """Create a new instance of BaseModel, and print the id"""
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            key = (eval(args[0])().id)
            print key
            storage.save()
>>>>>>> 46d5a0696a3f029edb62d03c94ef9868c18cacbd

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = parse(arg)
        if not args:
            print("** class name missing **")
<<<<<<< HEAD
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in instances:
=======
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instances = storage.all()
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in instances:
>>>>>>> 46d5a0696a3f029edb62d03c94ef9868c18cacbd
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
<<<<<<< HEAD
        args = parse(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)
=======
        arg = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif (args) < 2:
            print("** instance id missing **")
        else
            instances = storage.all()
            instance_id = args[1]
            key = "{}.{}".format(args[0], instance_id)
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")
>>>>>>> 46d5a0696a3f029edb62d03c94ef9868c18cacbd

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = parse(arg)
<<<<<<< HEAD
        if args and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        else:
            objl = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(args) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = parse(arg)
        if not args:
            print("** class name missing **")
            return False
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        instances = storage.all()
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in instances:
            print("** no instance found **")
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            try:
                type(eval(args[2])) != dict
=======
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)
        
    def do_update(self, arg):

        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
>>>>>>> 46d5a0696a3f029edb62d03c94ef9868c18cacbd
            except NameError:
                print("** value missing **")
                return False

<<<<<<< HEAD
        if len(args) == 4:
            obj = instances["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = instances["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
=======
        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
>>>>>>> 46d5a0696a3f029edb62d03c94ef9868c18cacbd
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()