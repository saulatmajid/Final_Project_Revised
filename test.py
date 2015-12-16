#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module containing functions for Test class."""


class Test(object):
    """ Represents a Test taken by a student in a subject. """

    def __init__(self, test_name, score, possible_score, notes, test_date):
        """Constructor for the Test class.

            Args:
                test_name: Name of the test
                score: Score stored by this student on this test
                possible_score: Maximum score on this test
                notes: Notes on this student's performance on this test
                test_date: Date when this test was taken
        """
        self.__test_name = test_name
        self.__score = score
        self.__possible_score = possible_score
        self.__notes = notes
        self.__test_date = test_date

    def get_test_name(self):
        """Returns name of the test object."""
        return self.__test_name

    def get_score(self):
        """Returns score on this test by this student. """
        return self.__score

    def get_possible_score(self):
        """Returns total possible score on this test. """
        return self.__possible_score

    def get_notes(self):
        """Returns notes on this student's performance on this test. """
        return self.__notes

    def get_test_date(self):
        """Returns the date test was taken. """
        return self.__test_date
