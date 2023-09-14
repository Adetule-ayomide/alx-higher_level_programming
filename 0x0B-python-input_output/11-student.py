#!/usr/bin/python3

""" a class Student that defines a student by:

    first_name
    last_name
    age
"""


class Student:
    """ A class named student"""
    def __init__(self, first_name, last_name, age):
        """ A function that define a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A function that retrieves a dictionary representation"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """A function replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
