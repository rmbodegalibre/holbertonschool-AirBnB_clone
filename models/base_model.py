#!/usr/bin/python3
"""class BaseModel"""
import uuid
from datetime import datetime

class BaseModel():

    def __init__(self, id = None, created_at = None, updated_at = None):
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()        
    

    


    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    def save(self):
        """
        updates the public instance attribute updated_at with the current datetime
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