#!/usr/bin/python3
"""Write a class LockedClass with no class or object attribute"""


class LockedClass:
    """
    Only allows instatiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
