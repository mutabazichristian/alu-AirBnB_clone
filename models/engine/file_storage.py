#!/bin/python3

import models
import json

class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    def __init__(self):
        pass
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path) using JSON dump"""
        object_dict = {}
        for obj in self.__objects:
            object_dict[obj] = self.__objects[obj].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(object_dict, file)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as file:
                object_dict = json.load(file)
                for obj in object_dict:
                    self.__objects[obj] = models.classes[object_dict[obj]["__class__"]](**object_dict[obj])
        except FileNotFoundError:
            pass