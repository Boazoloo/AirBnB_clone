#!/usr/bin/python3
"""Defines the FileStorage class."""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict()
                    for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects, if it exists."""
        from models.base_model import BaseModel

        classes = {
            "BaseModel": BaseModel
        }

        try:
            with open(FileStorage.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value["__class__"]
                FileStorage.__objects[key] = classes[cls_name](**value)
        except FileNotFoundError:
            pass
