#!/usr/bin/python3
"""Command interpreter for the AirBnB clone."""

import cmd
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """AirBnB command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Quit command when EOF is received."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def _get_class(self, class_name):
        """Return a supported class."""
        classes = {
            "BaseModel": BaseModel,
            "User": User
        }
        return classes.get(class_name)

    def do_create(self, line):
        """Create a new instance of a class."""
        args = shlex.split(line)

        if not args:
            print("** class name missing **")
            return

        cls = self._get_class(args[0])
        if cls is None:
            print("** class doesn't exist **")
            return

        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance."""
        args = shlex.split(line)

        if not args:
            print("** class name missing **")
            return

        if self._get_class(args[0]) is None:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, line):
        """Delete an instance."""
        args = shlex.split(line)

        if not args:
            print("** class name missing **")
            return

        if self._get_class(args[0]) is None:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, line):
        """Print all instances or all instances of a class."""
        args = shlex.split(line)
        objects = storage.all()

        if args:
            cls = self._get_class(args[0])
            if cls is None:
                print("** class doesn't exist **")
                return

            result = [
                str(obj) for obj in objects.values()
                if isinstance(obj, cls)
            ]
        else:
            result = [str(obj) for obj in objects.values()]

        print(result)

    def do_update(self, line):
        """Update an instance with a new attribute value."""
        args = shlex.split(line)

        if not args:
            print("** class name missing **")
            return

        if self._get_class(args[0]) is None:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attribute = args[2]
        value = args[3]

        current_value = getattr(obj, attribute, None)

        if isinstance(current_value, int):
            value = int(value)
        elif isinstance(current_value, float):
            value = float(value)

        setattr(obj, attribute, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
