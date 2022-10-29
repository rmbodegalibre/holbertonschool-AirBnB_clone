#!/usr/bin/python3
"""
This module contains a class BaseModel that defines
all common attributes/methods for other classes:
"""
import uuid
from datetime import datetime


class BaseModel():
    """
    This class defines all common attributes/methods for other classes:
    Public instance attributes:
    id: string - assign with an uuid when an instance is created:
        * It can use uuid.uuid4() to generate unique id but
          needs be converted to a string.
        * the goal is to have unique id for each BaseModel
    created_at: datetime - assign with the current datetime when an instance
        is created
    updated_at: datetime - assign with the current datetime when an instance
        is created and it will be updated every time you change your object
    __str__: should print: [<class name>] (<self.id>) <self.__dict__>
    Public instance methods:
    save(self): updates the public instance attribute updated_at with the
    current datetime
    to_dict(self): returns a dictionary containing all keys/values of __dict__
    of the instance
    by using self.__dict__, only instance attributes set will be returned
    a key __class__ must be added to this dictionary with the class name of
    the object created_at and updated_at must be converted to string object
    in ISO format:
    format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
    you can use isoformat() of datetime object
    This method will be the first piece of the serialization/deserialization
    process:
    create a dictionary representation with “simple object type” of our
    BaseModel
    """
    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""
        return ("[{}] ({}) {}".
        format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at with the current
        datetime
        """
        # self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
