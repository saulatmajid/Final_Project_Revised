#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exception handling classes for Final Project."""


class UserExitException(Exception):
    """A class that extends Exception class. An object of this class is thrown
        when user wants to exit the program.
    """
    pass


class IncorrectSubjectException(Exception):
    """A class that extends Exception class. An object of this class is thrown
        when user does not enter the correct subject.
    """
    pass


class IncorrectStudentException(Exception):
    """A class that extends Exception class. An object of this class is thrown
        when user does not enter the correct student name.
    """
    pass


class IncorrectSectionException(Exception):
    """A class that extends Exception class. An object of this class is thrown
        when user does not enter the correct section.
    """
    pass


class IncorrectGradeException(Exception):
    """A class that extends Exception class. An object of this class is thrown
        when user does not enter the correct grade
    """
    pass
