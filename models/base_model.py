#!/usr/bin/python3

import sys
#sys.path.append("..")

import uuid
import datetime
from models.engine import storage

class BaseModel:

    # public instance attributes
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        # check if **kwargs is empty
        if len(kwargs) == 0:
            self.__dict__[self.__class__.__name__ + "." + self.id] = str(uuid.uuid4())
            self.__dict__['created_at'] = datetime.datetime.now()
            storage.new(self.__dict__)
        else:
            self.__dict__['created_at'] = datetime.datetime.now()
            self.__dict__.update(kwargs)

    def __str__(self):
        return "[" + str(self.__class__.__name__) + "]" + " " + "(" + self.id + ")" + " " + str(self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['id'] = self.id
        self.__dict__['created_at'] = self.created_at.now()
        self.__dict__['updated_at'] = self.updated_at.now()
        return self.__dict__
