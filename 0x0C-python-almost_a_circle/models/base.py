#!/usr/bin/python3
"""
Base class definition
"""
import csv
import os
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Args:
            id (int): integer id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Args:
            list_dictionaries: a list of dictionaries
        Returns:
            the JSON string representation of list_dictionaries
            If list_dictionaries is None or empty, return the string: "[]"
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Args:
            json_string: string representing a list of dictionaries
        Returns:
            the list of the JSON string representation
            If json_string is None or empty, return an empty list
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        Args:
            list_objs: list of instances who inherits of Base
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Args:
            **dictionary: a double pointer to a dictionary
        Returns:
            an instance with all attributes already set
        """
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns:
            a list of instances
        """
        filename = f"{cls.__name__}.json"
        instance_list = []
        if os.path.isfile(filename):
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
                list_dictionary = cls.from_json_string(json_string)

                for dictionary in list_dictionary:
                    instance = cls.create(**dictionary)
                    instance_list.append(instance)
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize objects to a CSV file.
        Args:
            list_objs (list): List of instances to serialize.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            if cls.__name__ == 'Rectangle':
                header = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                header = ['id', 'size', 'x', 'y']

            writer.writerow(header)

            for obj in list_objs:
                data = [getattr(obj, attr) for attr in header]
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize objects from a CSV file.
        Returns:
            List of instances.
        """
        filename = f"{cls.__name__}.csv"
        instance_list = []

        if not os.path.isfile(filename):
            return instance_list

        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader)

            for row in reader:
                data_dict = {}
                for i, value in enumerate(row):
                    if value.isdigit():
                        data_dict[header[i]] = int(value)
                    else:
                        data_dict[header[i]] = value
                instance = cls.create(**data_dict)
                instance_list.append(instance)

        return instance_list
