from Detached.Global.Configurations.ConnectionEstablishment import *
from Detached.Global.Variables.varFile1 import totalWorkingDays, maximumSlots
from Detached.Global.Configurations.LocalUsersConfigurations import *           # local User configurations
import json


# Function that checks if a teacher could be available for teaching a subject or not.
# Arguments passed for this function is in respect to each individual teacher.
def check_teacher_availability(free_slots_each_day, subject_lecture_per_week, max_lecture_per_day, max_lecture_of_teacher):
    # summation of free lectures of each day (Monday + Tuesday + ... + Sunday)
    total_no_of_free_lectures = 0

    for i in range(len(free_slots_each_day)-1):
        total_no_of_free_lectures += free_slots_each_day[i]

    max_lectures = totalWorkingDays * maximumSlots                          # total no of lectures, possible in a week
    current_no_of_lectures = max_lectures - total_no_of_free_lectures       # total no of lectures taken by the teacher

    i = 0                                                                   # reinitializing i for list indexing
    lectures_left = subject_lecture_per_week                                # for better code readability
    while current_no_of_lectures <= max_lecture_of_teacher and lectures_left >= 0:
        if free_slots_each_day[i] >= max_lecture_per_day:
            """ if a teacher has more free lectures to teach the same subject in a day,
                then the maximum no of lectures (as per 'each day' constraint) could be assign
                for the same day"""
            lectures_left -= max_lecture_per_day
            i += 1                                                          # to iterate for the next day
        else:
            """ if a teacher has less or no free lectures to teach the same subject in a day,
                then the maximum no of lectures (that can be taken/assigned for the same subject)
                would be equals to no. of free slots available on that day"""
            lectures_left -= free_slots_each_day[i]
            i += 1                                                          # to iterate for the next day

    if lectures_left <= 0:
        return True                                                         # return 'true' if teacher is available
    else:
        return False                                                        # return 'false' for non availability


# Function to get details of the teacher for a given uID
def get_teacher_details(uid):
    return db[teacher_collection].find({"uid": uid})


# static address of JSON file, must be updated according to one's PC
def load_teachers_at_once():
    file_location = 'Detached/Database/teachers.json'
    complete_address = project_location + file_location

    with open(complete_address) as f:
        file_data = json.load(f)

    db[teacher_collection].insert(file_data)


# Function added for Teachers that are already added through teachers.json file
def add_course_attribute():
    db[teacher_collection].update_many({"department": "DCS"}, {"$set": {"course": "MCA"}})


"""To load all the teachers at once (from a JSON file) uncomment below line """
# load_teachers_at_once()

"""Too add the course = MCA for the above file load teachers at once uncomment below line
because the teachers .json file do not have the course field so this line will automatically 
create a field "course" for them and set the value "MCA".
Similarly for the newly inserted teachers will automatically be having the attribute "course" 
with None value unless provided a new value. This functionality has been added to the Teachers.py"""
# add_course_attribute()
