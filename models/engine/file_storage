#!/usr/bin/python3

import sys
sys.path.append("..")

import os

import json

class FileStorage():
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #root folder of project
    __file_path = ROOT_DIR + '/file.json'
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects = obj

    def save(self):
        serialized_object_to_json = json.dumps(self.__objects, indent=4,default=str)
        with open(self.__file_path, 'w') as filepath:
            json.dump(serialized_object_to_json, filepath, indent=2)

    def reload(self):
        pass
        #with open(self.__file_path) as json_file:
            #pass
            #json.load(json_file)
