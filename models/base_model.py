#!usr/bin/python3
"""Define BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """BaseModel for the project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of object"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary representation of the BaseModel instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
