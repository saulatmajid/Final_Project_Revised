#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module containing various functions for Grade class"""


class Grade(object):
    """Represents a grade.
        Contains Sections which are part of this grade
    """

    def __init__(self, grade_number):
        """ A constructor for Grade class

        Args:
            grade_number: Identifies grade
        """
        self.__grade_number = grade_number
        self.__sections_dict = {}

    def get_grade_number(self):
        """Returns grade number of Grade object"""
        return self.__grade_number

    def get_sections(self):
        """Returns a dictionary of Section objets """
        return self.__sections_dict

    def set_sections(self, sections_dict):
        """Sets the dictionary of sections

        Args:
            sections_dict: A dictionary of Section objects
        """
        self.__sections_dict = sections_dict
