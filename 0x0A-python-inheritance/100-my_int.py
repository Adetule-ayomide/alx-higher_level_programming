#!/usr/bin/python3

"""a class MyInt that inherits from int"""


class MyInt(int):
    """ myint inverted operator == and != """
    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        return super().__ne__(value)

    def __ne__(self, value):
        """override !=operator qith == behavior"""
        return super().__eq__(value)

