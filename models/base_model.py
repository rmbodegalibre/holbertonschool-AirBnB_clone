#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes
"""
from time import strftime
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    This class defines all common attributes/methods for other classes:
    Public instance attributes:
    * id: string - assign with an uuid when an instance is created:
    - you can use uuid.uuid4() to generate unique id but don’t forget to convert
      to a string
    - the goal is to have unique id for each BaseModel
    - created_at: datetime - assign with the current datetime when an instance
      is created
    - updated_at: datetime - assign with the current datetime when an instance
      is created and it will be updated every time you change your object
    """
    def __init__(self, id=None, created_at=None, updated_at=None):
        "Initialization of class"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
    
    def __str__(self):
        """__str__ Method prints [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}"\
                .format(BaseModel.__name__, self.id, self.__dict__)  

    def save(self):
        """save Method updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of
        the instance:"""
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")        
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        #self.created_at = self.created_at.isoformat()
        #self.updated_at = self.updated_at.isoformat()
        return dictionary