#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A class called subject."""


class Subject(object):
    """Represents a subject taken by a student."""

    def __init__(self, subject_name):
        """Constructor for the Subject object.

        Args:
            subject_name: Name of the subject taken by this student
        """
        self.__subject_name = subject_name
        self.__tests_dict = {}

    def get_subject_name(self):
        """Returns the name of the subject."""
        return self.__subject_name

    def get_tests(self):
        """Returns a dictionary of test objects in this Subject."""
        return self.__tests_dict

    def set_tests(self, tests_dict):
        """Sets the dictionary of Test objects.

        Args:
            tests_dict: A dictionary of tests offered in this Subject
                        taken by this student
        """
        self.__tests_dict = tests_dict
