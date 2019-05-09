import json
from Detached.Global.Configurations.ConnectionEstablishment import *

"""File which consist of user dependent configurations. These probably be different for each user.
   Hence, if this file doesn't exists, create manually at following location (within the project):
   Detached/Global/Configurations/LocalUsersConfigurations.py
   
   File definition:
   project_location = 'absolute address to the project on your machine'
   e.g. : project_location = '/home/dev/Documents/PycharmProjects/RADAtR/'
   
   Note that this file is not supposed to be on tracking."""
from Detached.Global.Configurations.LocalUsersConfigurations import *


# This function should be called for creating a subject list for a new course.
def insert_course_and_subjects():
    course_name = input("Type the course name")
    total_semesters = int(input("Provide total semesters"))

    # creating an empty data structure for storing subjects
    document = {course_name: [{str(sem_number): []} for sem_number in range(1, total_semesters + 1)]}

    # adding subjects in required empty lists
    for i in range(total_semesters):
        while True:
            subject = input(f"Add Subject for semester {i + 1}")
            document[course_name][i][str(i + 1)].append(subject)
            add_more = input("Any more subjects\n1.True\n2.False")
            if add_more == "2":
                break

    db[collection].insert(document)
    db[collection].find()


def subject_removal():
    """Define a function to remove a subject/s from given course
       of a particular semester"""
    # include a function to display list of subjects from which to remove it.


def display():
    pass


def update_subject(course, sem, replacing, replaced_by):
    course_sem = str(str(course) + "." + str(sem))
    to_be_changed = course_sem + ".$"
    db[collection].find_one_and_update({course_sem: replacing}, {"$set": {to_be_changed: replaced_by}})


# give absolute address of the records.json file to load at once
def insert_all():
    # location (within the project) of the file to be loaded
    file_location = 'Detached/Database/records.json'

    # address (from the root location) of file
    complete_location = project_location + file_location
    with open(complete_location) as f:
        file_data = json.load(f)

    db[collection].insert(file_data)
    print(db[collection].find())


# function to get subjects list of a given course and respective semester
def get_list_of_subject_for(course, semester):
    sub_list = []
    course_sem = str(str(course) + "." + str(semester))
    cursor = db[collection].find_one({course: {"$exists": "true"}}, {course_sem: "true", "_id": 0})
    for subject in cursor[str(course)][str(semester)]:
        sub_list.append(subject)
    return sub_list


# function to add minutes to given time and return the result in 24-hour format
def add_time_to(initial_time, minutes_to_add):
    initial_time = str(initial_time)
    minutes_to_add = str(minutes_to_add)
    # validation of arguments
    if minutes_to_add[0] == '-':
        print('Cannot add negative values')
        return -1
    if initial_time[0] == '-':
        print('You seems to use a watch from different world')
        return -1

    # have use in representations and conversions
    zeros_in_hours_part = 0
    zeros_in_minutes_part = 0
    hour_carry = 0

    if len(initial_time) == 4:                      # validation of initial time (must be of 4 digits)
        # storing hours and minutes digits separately
        hours_part = initial_time[0:2]
        minutes_part = initial_time[2:4]

        # getting the non zero digits only for hours part
        for i in range(len(hours_part)):
            if hours_part[i] == '0':
                zeros_in_hours_part += 1
            else:
                break                               # stop as soon as a non-zero digit is encountered

        # conversion of hours part from string to integer
        if zeros_in_hours_part == 2:
            hours_part = 0                          # direct assignment due to base 10 conversion issue
        else:
            hours_part = int(hours_part[zeros_in_hours_part:2])

        # getting the non zero digits only for minutes part
        for i in range(len(minutes_part)):
            if minutes_part[i] == '0':
                zeros_in_minutes_part += 1
            else:
                break                               # stop as soon as a non-zero digit is encountered

        # conversion of minutes part from string to integer
        if zeros_in_minutes_part == 2:
            minutes_part = 0  # direct assignment due to base 10 conversion issue
        else:
            minutes_part = int(minutes_part[zeros_in_minutes_part:2])

        # conversion of minutes_to_add from string to integer
        if minutes_to_add == '00':
            minutes_to_add = 0
        else:
            minutes_to_add = int(minutes_to_add)

        # adding (minutes) time
        minutes_part = minutes_part + minutes_to_add

        if minutes_part >= 60:
            hour_carry = minutes_part // 60
            minutes_part = minutes_part % 60

        # adding (hours) time
        hours_part = hours_part + hour_carry

        if hours_part >= 24:
            hours_part = hours_part % 24

        # converting numeric time value back to string
        minutes_part = str(minutes_part)
        hours_part = str(hours_part)

        if len(hours_part) == 1:
            hours_part = '0' + hours_part

        if len(minutes_part) == 1:
            minutes_part = '0' + minutes_part

        resultant_time = hours_part + minutes_part
        print(resultant_time)
        return resultant_time

    else:
        print('Invalid input for initial time. Must be of 4 digits')
        return -1


# function to shorten name by returning only last name
def last_name_only(name):
    short_name = ''                                 # initially empty
    words_in_name = name.split()        # create a list of words present in whole name

    # if name consists of single word only, return name as it is.
    if len(words_in_name) == 1:
        return name
    else:
        # creating acronym for name
        for i in range(len(words_in_name) - 1):
            word = words_in_name[i]
            short_name = short_name + word[0] + '. '

        # appending the last name in acronym
        short_name = short_name + words_in_name[-1]
        return short_name
