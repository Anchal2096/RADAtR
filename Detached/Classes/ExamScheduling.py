from Detached.Global.Functions.IndependentFunctions import *
from GUI.GUI_ExaminationScheduling import *


class ExamScheduleMapping:
    def __init__(self):
        self.list_of_semester = [1, 3, 5]   # this must be dynamic
        self.list_of_subjects = []
        self.course = "MCA"
        self.working_days = 5
        self.total_slots = 2
        self.placing_all_papers_in_a_list()

    def placing_all_papers_in_a_list(self):
        for self.no_of_subjects in self.list_of_semester:
            self.list_of_subjects.append(get_list_of_subject_for(self.course, self.no_of_subjects))

        print(self.list_of_subjects)
        self.a = (sum(self.list_of_subjects, []))
        print (self.a)

    def create_a_2d_list(self):
        rows, cols = (self.working_days, self.total_slots)
        self.list = [["true"] * cols] * rows
        for row in self.list:
            print(row)
        # print(self.list)

    def place_subjects_to_list(self):
        print("true")

# ExamScheduleMappingObj = ExamScheduleMapping()


if __name__=="__main__":
    main()

    main_window_obj = MainWindow()
    # print(get_list_of_subject_for("MCA", 5))
    print(main_window_obj.click_box())
