#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module containing various fnctions for Section class."""


class Section(object):
    """Represents a Section. Contains Students who attend this section."""

    def __init__(self, section_number):
        """ A constructor for Section class.

        Args:
            section_number: Identifies section
        """
        self.__section_number = section_number
        self.__students_dict = {}

    def get_section_number(self):
        """Returns section number of a Section object."""
        return self.__section_number

    def get_students(self):
        """Returns a dictionary containinig Student objects."""
        return self.__students_dict

    def set_students(self, students_dict):
        """Sets the dicitonary of students who attend this section.

        Args:
            students_dict: A dictionary of Student objects
        """
        self.__students_dict = students_dict
