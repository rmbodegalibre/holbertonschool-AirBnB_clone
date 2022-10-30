#!/usr/bin/python3
"""
class BaseModel that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models



class BaseModel:
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
    def __init__(self, *args, **kwargs):
        """
        Initialize an instance of BaseModel
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    dttime_ob = datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, dttime_ob)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            
    
    def __str__(self):
        """_str_ Method prints [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"  

    def save(self):
        """save Method updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
        

    def to_dict(self):
        """returns a dictionary containing all keys/values of _dict_ of
        the instance:"""
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
