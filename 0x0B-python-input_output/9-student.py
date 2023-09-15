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

    def to_json(self):
        """A function that retrieves a dictionary representation"""
        return self.__dict__
