from Detached.Global.Functions.IndependentFunctions import *
import random
# from GUI.GUI_ExaminationScheduling import *


class ExamScheduleMapping:
    def __init__(self):
        self.list_of_semester = [1, 3, 5]   # this must be dynamic
        self.list_of_subjects = []
        self.course = "MCA"
        self.working_days = 5
        self.total_slots = 2
        self.random_subject =[]
        self.placing_all_papers_in_a_list()
        # self.create_a_2d_list()

    def placing_all_papers_in_a_list(self):
        for self.no_of_subjects in self.list_of_semester:
            self.list_of_subjects.append(get_list_of_subject_for(self.course, self.no_of_subjects))

        s = set(range(1, 6))
        # print(self.list_of_subjects)
        self.single_dimension_array_of_subjects = (sum(self.list_of_subjects, []))
        self.random_subject = (random.choice(self.single_dimension_array_of_subjects))
        s.remove(self.random_subject)
        print (self.single_dimension_array_of_subjects)
        self.randomlist.append(self.random_subject)


    def create_a_2d_list(self):
        rows, cols = (self.working_days, self.total_slots)
        self.list = [["true"] * cols] * rows
        for row in self.list:
            print(row)
        # print(self.list)

    def place_subjects_to_list(self):
        pass

ExamScheduleMappingObj = ExamScheduleMapping()


