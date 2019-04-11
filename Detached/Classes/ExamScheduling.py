from Detached.Global.Functions.IndependentFunctions import *
import random


class ExamScheduleMapping:
    def __init__(self):
        self.list_of_semester = [1, 3, 5]  # this must be dynamic
        self.list_of_subjects = []
        self.course = "MCA"
        self.working_days = 10
        self.total_slots = 2
        self.rows = self.working_days
        self.columns = self.total_slots
        self.two_d_random_var_matrix = []  # 2d matrix to store random variable
        self.random_list = []  # list that will contain the list of subjects chossen randomly
        self.placing_all_papers_in_a_list()
        self.create_a_two_d_list_Of_random_variable()
        self.create_a_dictionary_of_sem_sub()

    def placing_all_papers_in_a_list(self):
        for self.no_of_subjects in self.list_of_semester:
            self.list_of_subjects.append(get_list_of_subject_for(self.course, self.no_of_subjects))

        # print(self.list_of_subjects)
        self.single_dimension_array_of_subjects = (sum(self.list_of_subjects, []))
        """ this if statement checks if there are more working days than the no of subjects 
        then it will create appropriate gaps by subtracting"""
        if len(self.single_dimension_array_of_subjects) < self.working_days*self.total_slots:
            self.difference = self.working_days * self.total_slots -len(self.single_dimension_array_of_subjects)
            for gap in range(self.difference):
                self.single_dimension_array_of_subjects.append(" -- ")
            # print(self.single_dimension_array_of_subjects)

        # print(self.single_dimension_array_of_subjects)

        "using random function for the list"
        for subjects in range(len(self.single_dimension_array_of_subjects)):
            self.random_subject = (random.choice(self.single_dimension_array_of_subjects))
            self.random_list.append(self.random_subject)
            self.single_dimension_array_of_subjects.remove(self.random_subject)
        # print(self.random_list)

    """converts the 1d list to 2-d with corresponding rows and columns as there are no of days and columns"""

    def create_a_two_d_list_Of_random_variable(self):
        index = 0
        for i in range(0, self.rows):
            self.two_d_random_var_matrix.append([])
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                self.two_d_random_var_matrix[i].append(j)
                self.two_d_random_var_matrix[i][j] = 0
        # print(self.two_d_random_var_matrix)
        while index <= len(self.two_d_random_var_matrix):
            for i in range(0, self.rows):
                for j in range(0, self.columns):
                    # print('entry in row ', i + 1, 'entry in row ', i + 2)

                    self.two_d_random_var_matrix[i][j] = self.random_list[index]
                    index = index + 1

        print(self.two_d_random_var_matrix)# a 2d list containing subjects randomly

    def create_a_dictionary_of_sem_sub(self):
        dict_of_selected_sem = {}
        for semester in self.list_of_semester:
            key = semester
            value = get_list_of_subject_for(self.course, semester)
            dict_of_selected_sem[key] = value
        print(dict_of_selected_sem)

ExamScheduleMappingObj = ExamScheduleMapping()
