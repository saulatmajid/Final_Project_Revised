#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final Project program to calculate students' score reports."""


from test import Test
from subject import Subject
from student import Student
from section import Section
from grade import Grade
from project_exception import UserExitException
from project_exception import IncorrectSubjectException
from project_exception import IncorrectStudentException
from project_exception import IncorrectSectionException
from project_exception import IncorrectGradeException


def prompt_menu(menu_choice):
    """A function that contains all user prompts. Depending upon the value
       passed, a prompt is printed.

    Args:
        menu_choice: identifies which prompt to print.

    Returns:
        A string that the user has typed

    Example:
        >>> Please choose what you want to do.
            1) Obtain a student's score in a specific course?
            2) Obtain a student's score in all courses?
            3) Obtain a section's peformance in a specific course
            4) Obtain a section's peformance in all courses
            Or type '0' to Quit
            Type Here:
    """

    if menu_choice == 0:
        print "Please select from the following menu options:"
        print "1) Obtain a student's score in a specific course?"
        print "2) Obtain a student's score in all courses?"
        print "3) Obtain a section's peformance in a specific course?"
        print "4) Obtain a section's peformance in all courses?"
    elif menu_choice == 1:
        print "Type the GRADE NUMBER (numeric value)"
    elif menu_choice == 2:
        print "Type the SECTION NUMBER (numeric value)"
    elif menu_choice == 3:
        print "Type COURSE NAME"
    elif menu_choice == 4:
        print "Type the STUDENT's NAME"
    print "Or type '0' to Quit"
    user_input = raw_input("Type Here: ")

    if user_input == "0":
        raise UserExitException()
    return user_input


def load_student_data(filename):
    """A function that reads data from a CSV file and stores it into objects.

    Args:
       filename: Name of the file

    Returns:
        A dictionary of Grade objects.

    """

    grades_dict = {}

    csv_f = open(filename, 'r')
    i = 0
    for line in csv_f:
        # print "line no:", i, "=", line
        if i > 0:
            # We don't need to read the header, so
            # we do not read line 0
            line_list = []
            line_list = line.split(',')

            grade_number = int(line_list[0])
            # Only create a grade object if it doesn't already exist
            if grade_number in grades_dict:
                grade_temp = grades_dict[grade_number]
            else:
                grade_temp = Grade(grade_number)

            sections_dict = grade_temp.get_sections()
            section_number = int(line_list[1])
            # Only create a section object if it doesn't already exist
            # in that grade
            if section_number in sections_dict:
                section_temp = sections_dict[section_number]
            else:
                section_temp = Section(section_number)

            students_dict = section_temp.get_students()
            student_name = line_list[2]
            # Only create a student object if it doesn't already exist
            # in that section
            if student_name in students_dict:
                student_temp = students_dict[student_name]
            else:
                student_temp = Student(student_name)

            subjects_dict = student_temp.get_subjects()
            subject_name = line_list[3]
            # Only create a subjects object if it doesn't already exist
            # in that student object
            if subject_name in subjects_dict:
                subject_temp = subjects_dict[subject_name]
            else:
                subject_temp = Subject(subject_name)

            tests_dict = subject_temp.get_tests()
            test_obj = Test(line_list[4], int(line_list[5]), int(line_list[6]),
                            line_list[7], line_list[8])

            tests_dict[test_obj.get_test_name()] = test_obj
            subject_temp.set_tests(tests_dict)

            subjects_dict[subject_temp.get_subject_name()] = subject_temp
            student_temp.set_subjects(subjects_dict)

            students_dict[student_temp.get_student_name()] = student_temp
            section_temp.set_students(students_dict)

            sections_dict[section_temp.get_section_number()] = section_temp
            grade_temp.set_sections(sections_dict)

            grades_dict[grade_temp.get_grade_number()] = grade_temp
        # variable i tracks line numbers read
        i = i + 1
    csv_f.close()
    return grades_dict


def print_test_stats(test_obj):
    """A function that prints the contents of Test object.

    Args:
       test_obj: Test object which is to be printed.

    """

    print "==================\nTest:", test_obj.get_test_name()
    print "Score=", test_obj.get_score()
    print "Possible Score=", test_obj.get_possible_score()
    print "Notes=", test_obj.get_notes()
    print "Test Date=", test_obj.get_test_date(), "\n"


def provide_student_subject_data(specific_subject_obj):
    """A function that extracts and prints data for Scenario 1.

    Args:
       specific_subject_obj: Subject object of a specific Student object

    Example:
        >>> Data for the subject: Math
    """

    print "Data for the subject:", specific_subject_obj.get_subject_name()
    retrieved_tests = specific_subject_obj.get_tests()
    for test_key in retrieved_tests:
        print_test_stats(retrieved_tests[test_key])


def provide_student_all_data(current_student):
    """A function that extracts and prints data for Scenario 2.

    Args:
       current_student: Student objects whose subjects are asked

    Example:
        >>> Data for the subject: Math
    """
    subjects_dict = current_student.get_subjects()
    for subject_key in subjects_dict:
        print "Data for the subject:", SUBJECTS[subject_key].get_subject_name()
        tests_list = SUBJECTS[subject_key].get_tests()
        for test_key in tests_list:
            print_test_stats(tests_list[test_key])


def print_subject_stats(key_list, score_list):
    """A function that prints summary report for a subject.

    Args:
        key_list: List objects which contains keys of subject names
        score_list: A list of student scores

    """
    print "\n===========\nSubject:", key_list[0]
    print "Test=", key_list[1]
    print "Test Date=", key_list[2]
    print "Average Score=", sum(score_list)/len(score_list)
    print "Minimum Score=", min(score_list)
    print "Maximum Score=", max(score_list)


def calc_subject_stats(section_2):
    """ A function that calculates subject statistics.

    Args:
        section_2: Section objet whose score data is summarized

    Returns:
        A dictionary of key and value, where value is
        the list of scores for subject/test_name/test_date combination
    """
    score_dict = {}
    students_dict = section_2.get_students()
    for student_key in students_dict:
        subjects_dict = students_dict[student_key].get_subjects()
        for subject_key in subjects_dict:
            subject_1 = subjects_dict[subject_key]
            tests_dict = subject_1.get_tests()
            for test_key in tests_dict:
                stat_key = subject_key + "," + test_key + "," +\
                    tests_dict[test_key].get_test_date()
                # print "stat_key=", stat_key
                if stat_key in score_dict:
                    test_scores_list = score_dict[stat_key]
                    test_scores_list.append(tests_dict[test_key].get_score())
                else:
                    test_scores_list = [tests_dict[test_key].get_score()]
                score_dict[stat_key] = test_scores_list
    return score_dict


def provide_section_subject_data(section_1, subject_name):
    """A function that summarizes all test results for a given section and a
        given subject.

    Args:
        section_1: Given section
        subject_name: Given subject
    """
    score_dict = calc_subject_stats(section_1)
    for score_key, score_value in score_dict.items():
        key_list = score_key.split(',')
        if key_list[0] == subject_name:
            print_subject_stats(key_list, score_value)


def provide_section_all_data(section_2):
    """A function that summarizes all test results for a given section.

    Args:
        section_2: Given section
    """
    score_dict = calc_subject_stats(section_2)
    for score_key, score_value in score_dict.items():
        key_list = score_key.split(',')
        print_subject_stats(key_list, score_value)

if __name__ == "__main__":

    try:
        GRADE_DATA = load_student_data('SchoolData.csv')

        print "Welcome to the Student Progress Tracking System!!"
        while True:
            try:
                SCENARIO = int(prompt_menu(0))
                if SCENARIO in [1, 2, 3, 4]:
                    while True:
                        try:
                            GRADE_CHOICE = int(prompt_menu(1))
                            # check if grade is correct, else throw an exception
                            if GRADE_CHOICE in GRADE_DATA:
                                GRADE_OBJ = GRADE_DATA[GRADE_CHOICE]
                                SECTIONS = GRADE_OBJ.get_sections()
                            else:
                                print "Choose one of these grades:",\
                                    GRADE_DATA.keys()
                                raise IncorrectGradeException()

                            SECTION_CHOICE = int(prompt_menu(2))
                            # check if section's correct,
                            # else throw an exception
                            if SECTION_CHOICE in SECTIONS:
                                SECTION_OBJ = SECTIONS[SECTION_CHOICE]
                                STUDENTS = SECTION_OBJ.get_students()
                            else:
                                print "Choose one of these SECTIONS:",\
                                      SECTIONS.keys()
                                raise IncorrectSectionException()
                            if SCENARIO in [1, 2]:
                                STUDENT_CHOICE = prompt_menu(4).title()
                                # check if student name is correct,
                                # else throw an exception
                                if STUDENT_CHOICE in STUDENTS:
                                    STUDENT_OBJ = STUDENTS[STUDENT_CHOICE]
                                    SUBJECTS = STUDENT_OBJ.get_subjects()
                                else:
                                    print "Choose one of these students:",\
                                          STUDENTS.keys()
                                    raise IncorrectStudentException()
                            if SCENARIO in [1]:
                                SUBJECT_CHOICE = prompt_menu(3).title()
                                # check if subject is correct,
                                # otherwise throw exception
                                if SUBJECT_CHOICE in SUBJECTS:
                                    STUDENT_OBJ = SUBJECTS[SUBJECT_CHOICE]
                                    TESTS = STUDENT_OBJ.get_tests()
                                else:
                                    print "Choose one of these subjects:",\
                                          SUBJECTS.keys()
                                    raise IncorrectSubjectException
                            if SCENARIO in [3]:
                                SUBJECT_CHOICE = prompt_menu(3).title()
                                # We get the list of subjects from any student
                                STUDENT_0 = STUDENTS[STUDENTS.keys()[0]]
                                SUBJECTS = STUDENT_0.get_subjects()
                                # check if subject is correct,
                                # otherwise throw exception
                                if SUBJECT_CHOICE in SUBJECTS:
                                    SUBJECT_OBJ = SUBJECTS[SUBJECT_CHOICE]
                                    TESTS = SUBJECT_OBJ.get_tests()
                                else:
                                    print "Choose one of these subjects:",\
                                          SUBJECTS.keys()
                                    raise IncorrectSubjectException
                            # All user inputs are valid
                            # perform calculations & print on screen
                            print "Calculating for SCENARIO:", SCENARIO
                            if SCENARIO == 1:
                                SUBJECT_OBJ = SUBJECTS[SUBJECT_CHOICE]
                                provide_student_subject_data(SUBJECT_OBJ)
                            elif SCENARIO == 2:
                                STUDENT_OBJ = STUDENTS[STUDENT_CHOICE]
                                provide_student_all_data(STUDENT_OBJ)
                            elif SCENARIO == 3:
                                SECTION_OBJ = SECTIONS[SECTION_CHOICE]
                                provide_section_subject_data(SECTION_OBJ,
                                                             SUBJECT_CHOICE)
                            else:
                                # Scenario 4
                                SECTION_OBJ = SECTIONS[SECTION_CHOICE]
                                provide_section_all_data(SECTION_OBJ)
                            # We exit the program as user request is complete
                            raise UserExitException()
                        except IncorrectGradeException:
                            print "Invalid Grade was entered"
                        except IncorrectSectionException:
                            print "Invalid Section was entered"
                        except IncorrectStudentException:
                            print "Invalid Student Name was entered"
                        except IncorrectSubjectException:
                            print "Invalid Subject was entered"
                        except ValueError:
                            print "Invalid value for grade or section's entered"
                            print "Please type a numeric value"
                else:
                    # User entered a number other than 1,2,3 or 4
                    raise ValueError()
            except ValueError:
                print "Invalid value was entered"
                print "Please type 1,2,3,4 or 0.\n"

    except (IOError, EOFError):
        print "Unable to read student data.\n\
                Check data file and/or its location"
    except UserExitException:
        pass
    print "Exiting...\nThank you for using this program"
