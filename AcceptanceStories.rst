=============================
Student Progress Tracking System
=============================

Student Progress Tracking System is a tool that would put student progress reports at teachers’ fingertips. This information always comes in handy to hold spur of the moment parent-teacher conferences.

Personas
========

[Maria Jones]
-----------------------

[A young educationalist]

Details
^^^^^^^

[A young educationalist, who is a full time teacher at a local private school. She is always well-prepared for regular PTMs. Interestingly, the school allows parents to swing by and meet with the teacher to discuss their child’s progress. These meetings pose a problem to Maria, and she is required to rush to the student record room and grab students’ files. With this tool, it will be easier for her to retrieve relevant information really fast.]

Goals
^^^^^

[To obtain student records in a very short span of time, in order to hold a successful parent-teacher conference.]

Problem Scenarios
=================

Maria is expected to be equipped with updated information as she holds the meeting with the parents. Unfortunately, the record room is in the basement. She teaches 5 classes and it’s practically impossible to remember the records of students from all her classes, therefore she needs to consult student records.


Current Alternatives
^^^^^^^^^^^^^^^^^^^

[ An alternative is to ask the school to make students’ records available on teacher PCs, but this would require some software that would be integrated and would run through the entire school system. It would take some time and finances to implement.]

Value Proposition
^^^^^^^^^^^^^^^^^

[As a cost effective make shift arrangement, use the Progress Tracking System that simplifies the whole procedure of retrieving relevant students’ records. ]

User Stories
============

As Maria, I want to use Progress Tracking System, so that I can retrieve students’ records easily. It would enable me not only to obtain individual/ whole class test scores, course by course reports of individual students, but also overall class averages etc. This would prepare me better for my parent-teacher conferences.


Acceptance Stories
^^^^^^^^^^^^^^^^^^

[Acceptance Story 1: Individual student report by course]
```````````````````````````````````````````````````````````````
::

    Given that I want to generate quick reports for each student, first the system should ask me if I need it for one course. On providing the name of the course for that particular student, an accurate report should be quickly generated.
        ...
[Acceptance Story 2: Individual student report for all courses]
````````````````````````````````````````````````````````````````````
::
    Given that there would be situations when I would require one student’s performance in all courses. In that case the system should ask me if the report is for one course or all courses, and then ask for the name and grade of the student. With this information a summary report of one student’s performance in all courses should quickly be prepared.
	...
[Acceptance Story 3: Class report by course]
`````````````````````````````````````````````````
::
    Given that in certain situations I need to see the performance of the whole class, when the system asks me if I need a report for one grade, and which course. Then on providing that information the system generates a class report for one specific course. 
	...
[Acceptance Story 4: Class report for all courses]
``````````````````````````````````````````````````````
::
    Given that in certain situations I need to see the performance of one class in all courses, when the system asks if I need data for one grade or all grades, I select one grade, and when the system asks if I need information for one specific course or all courses, I select all courses, then a quick summary report is generated containing one grade’s performance on all courses. 
	...
