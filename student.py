#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A odule that contains various functions for the Student class."""


class Student(object):
    """Represents a student. Contains Subjects taken by this student."""

    def __init__(self, student_name):
        """A constructor for Student object.

        Args:
            student_name: Identifies student
        """
        self.__student_name = student_name
        self.__subjects_dict = {}

    def get_student_name(self):
        """Returns the student's name."""
        return self.__student_name

    def get_subjects(self):
        """Returns a dictionary of Subject objects."""
        return self.__subjects_dict

    def set_subjects(self, subjects_dict):
        """Sets the dictionary of Subject objects.

        Args:
            subjects_dict: A dictionary of Subjects object
            taken by this student
        """
        self.__subjects_dict = subjects_dict
