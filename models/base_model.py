#!/usr/bin/python3

import uuid
import models
from datetime import datetime

class BaseModel:
    """
    A base class that defines common attributes and methods for other classes.

    Public instance attributes:
        id (str): A unique identifier generated using UUID (Universally Unique Identifier).
        created_at (datetime): The datetime when an instance is created.
        updated_at (datetime): The datetime when an instance is created and updated.

    Public instance methods:
        save(): Updates the `updated_at` attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the instance.

    Public instance method:
        __str__(): Returns a string representation of the object.

    """

    def __init__(self,*args,**kwargs):
        """
        Initializes a new instance of the BaseModel class.
        - Assigns a unique UUID to the `id` attribute.
        - Sets the `created_at` attribute to the current datetime.
        - Sets the `updated_at` attribute to the `created_at` value.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the object.
        The string includes the class name, id, and dictionary representation of the object's attributes.

        Returns:
            str: A string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        - Copies the instance's attributes to a new dictionary.
        - Adds the '__class__' key with the class name.
        - Converts the 'created_at' and 'updated_at' attributes to ISO formatted strings.

        Returns:
            dict: A dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

