from PyQt5.QtWidgets import *
from Detached.Global.Functions.IndependentFunctions import get_list_of_subject_for
from GUI.IndividualWidgets.GUI_TimeTable_Output import *


class MapWindow:
    def __init__(self, parent=None, widget=None):
        # dependencies
        self.generateButton = widget               # refers to the 'Generate' button which is located in parent widget
        self.course = None                         # to be fetched from the admin class
        self.semester = None                       # will get updated by 'generate_time_table' function
        self.teachers = ["None", "Shared", "Manoj Kumar", "Narendra Kumar", "Sanjay Kumar Dwivedi", "Vipin Saxena", "Deepa Raj", "Shalini Chandra"]
        self.teacher_combo_boxes = []              # multiple comboBoxes are required to show dropDowns for each subject
        self.callingComboBoxIndex = None           # to identify which combo Box sent the signal or assigned a value
        self.subjectList = None
        self.windowOpened = False                  # used as a flag to know if 'share teacher' window is open or not
        self.sharingMade = False                   # used as a flag to know if sharing is made or not
        self.sharedList = []                       # contains subject-name along with names of teachers who shares it
        self.mapped_shared_subjects_index = []     # index numbers (of subjects) for which shared mapping has been done
        self.mapped_subjects_index = []            # index numbers (of subjects) for which mapping has been done
        self.teachersSelectedForSharing = 0        # counter, responsible for enabling/disabling 'share' button
        self.sharedTeachers = []                   # list of teachers which are selected to share same subject
        self.sharedSubjectIndex = None             # index of the subject which gets shared between teachers
        self.finalList = []

        # main widget containing dynamic contents
        self.mapSubWindow = QWidget(parent)

        # main layout (for dynamic contents)
        self.mappingSection = QHBoxLayout(self.mapSubWindow)

        # creating a vertical line
        self.VLine = QFrame(self.mapSubWindow)
        self.VLine.setFrameShape(QFrame.VLine)
        self.VLine.setFrameShadow(QFrame.Sunken)
        self.VLine.hide()

        # sub-layout1 (for subject-teacher 1 to 1 mapping)
        self.mapArea = QVBoxLayout(self.mapSubWindow)               # to be shown on the left

        # sub-layout2 (for subject-teacher 1 to n mapping)
        self.sharedMapArea = QVBoxLayout(self.mapSubWindow)         # to be shown on the right

        # sub-sub layout1 (nested in above layout)
        self.sharingTeacherLayout = QVBoxLayout(self.mapSubWindow)
        self.sharedMapArea.addLayout(self.sharingTeacherLayout)

        # sub x3 nested horizontal layout (for buttons of share-teacher sub window)
        self.shareButtonsLayout = QHBoxLayout(self.mapSubWindow)

        # putting the sub-layouts horizontally
        self.mappingSection.addLayout(self.mapArea)
        self.mappingSection.addWidget(self.VLine)
        self.mappingSection.addLayout(self.sharedMapArea)

        # self.mapSubWindow.setLayout(self.mappingSection)

    # function to display all teacher names that will share the same subject
    def process_combobox(self, index):
        # getting current value of selected combo box
        value = self.teacher_combo_boxes[index].currentText()
        index_of_teacher = self.teacher_combo_boxes[index].currentIndex()

        if value == 'None':
            mapping_already_removed = False

            # looking for the subject index if it exists already in shared-mapped list
            for i in self.mapped_shared_subjects_index:
                if i == index:                                          # means (shared) mapping exists
                    self.remove_shared_mapping(i)                       # remove existing mapping (from sharedList)
                    mapping_already_removed = True

            if not mapping_already_removed:                             # means (dedicated) mapping exists
                self.remove_mapping(index)                              # remove existing mapping (from finalList)

            # test outputs
            # for i in self.sharedList:
            #     print(i)
            # print(f'Shared Indexes mapped: {self.mapped_shared_subjects_index}')
            # print()
            # print('Final List is as follow:')
            # for i in self.finalList:
            #     print(i)
            # print(f'Indexes mapped: {self.mapped_subjects_index}')
            # print()

        elif value == 'Shared':
            # showing vertical line (to separate 2 sub windows)
            self.VLine.show()

            self.windowOpened = True                                       # to indicate that sharing window is open now

            # getting index of the operated combo box
            self.callingComboBoxIndex = index

            # disabling all the combo boxes till the sharing option window is open
            for i in range(len(self.teacher_combo_boxes)):
                self.disable_combo_box(i)

            # to generate the list for teachers which would be sharing a subject
            prompt = QLabel(f'Subject {self.subjectList[index]} will be shared by')
            prompt.setWordWrap(True)
            prompt.setContentsMargins(10, 0, 0, 20)
            self.sharingTeacherLayout.addWidget(prompt)

            # required but temporary
            self.checkBoxes = []

            # appending checkbox for each teacher
            # starting from 2 as the 1st two elements of teacher's list are 'none' and 'shared'
            for i in range(2, len(self.teachers)):
                checkbox = self.create_checkboxes(i, index)
                self.checkBoxes.append(checkbox)

            # displaying the teachers list (along with their checkboxes)
            for i in range(len(self.checkBoxes)):
                self.sharingTeacherLayout.addWidget(self.checkBoxes[i])

            self.sharingTeacherLayout.addStretch(1)

            # for 'share' and 'cancel' buttons layout
            self.shareButtonsLayout.addStretch(1)
            self.share_teacher_button = QPushButton('Share')
            self.share_teacher_button.setEnabled(False)
            self.share_teacher_button.clicked.connect(self.share_subject_between_teachers)
            self.shareButtonsLayout.addWidget(self.share_teacher_button)     # must be referenced to set other behaviour

            cancel_share_button = QPushButton('Cancel')
            cancel_share_button.clicked.connect(self.close_sharing_section)
            self.shareButtonsLayout.addWidget(cancel_share_button)
            self.sharingTeacherLayout.addLayout(self.shareButtonsLayout)

        else:
            # getting values
            teacher_name = self.teachers[index_of_teacher]
            subject_name = self.subjectList[index]

            # generating single mappings and updating finalList
            self.teacher_to_subjects_map(teacher_name, subject_name, index)

            # test outputs
            # print('Shared List is as follow:')
            # for i in self.sharedList:
            #     print(i)
            # print(f'Shared Indexes mapped: {self.mapped_shared_subjects_index}')
            # print()
            # print('Final List is as follow:')
            # for i in self.finalList:
            #     print(i)
            # print(f'Indexes mapped: {self.mapped_subjects_index}')
            # print()

        # enable 'Generate' button only when total mappings are equals to number of subjects
        total_mappings = len(self.mapped_subjects_index) + len(self.mapped_shared_subjects_index)
        if total_mappings == len(self.subjectList):
            self.generateButton.setEnabled(True)
        else:
            self.generateButton.setEnabled(False)

    # helper function for 'display_mapping_options()'
    def create_combo_box(self, for_index):
        teacher_options_widget = QComboBox()
        teacher_options_widget.addItems(self.teachers)            # same list of teacher is added as each comboBox items
        teacher_options_widget.currentIndexChanged.connect(lambda: self.process_combobox(for_index))
        return teacher_options_widget

    def display_mapping_options(self, for_semester):
        # updating semester value which will be passed to 'TimeTable' via 'generate_time_table' function
        self.semester = for_semester

        prompt = QLabel('Please assign the following subjects with their respective lecturer')
        prompt.setContentsMargins(0, 0, 0, 20)
        self.mapArea.addWidget(prompt)

        self.course = "MCA"                                      # This value is dependent on the Admin attribute
        semester = for_semester                             # getting semester number

        # getting list of subjects for the desired course and semester
        self.subjectList = get_list_of_subject_for(self.course, semester)

        self.teacher_combo_boxes = []                       # resetting list to be empty
        # creating list of comboBoxes with having same dropDown items
        for i in range(len(self.subjectList)):
            drop_down = self.create_combo_box(i)
            self.teacher_combo_boxes.append(drop_down)
            self.mapArea.addWidget(QLabel(self.subjectList[i]))
            self.mapArea.addWidget(self.teacher_combo_boxes[i])

    # function to close/hide dynamic content (teacher and subject lists)
    def close_map_window(self):
        # resetting values
        self.finalList = []
        self.mapped_subjects_index = []                             # decides enabling/disabling of 'Generate' button

        # external code to empty the (dynamic layout)
        while self.mapArea.count() > 0:
            item = self.mapArea.takeAt(0)
            if not item:
                continue

            widget = item.widget()
            if widget:
                widget.close()

        # emptying list of teachers that are selected for sharing
        self.sharedList = []

        # closing the opened window
        self.mapSubWindow.close()

    def close_sharing_section(self):
        # resetting dependencies
        self.teachersSelectedForSharing = 0
        self.sharedTeachers = []
        self.sharedSubjectIndex = None

        # setting 'None' in lieu of 'Shared' if cancel button is pressed
        if self.windowOpened:
            if self.sharingMade:
                self.teacher_combo_boxes[self.callingComboBoxIndex].setCurrentIndex(1)
            else:
                self.teacher_combo_boxes[self.callingComboBoxIndex].setCurrentIndex(0)

            # enabling all the disabled drop-downs)
            for i in range(len(self.teacher_combo_boxes)):
                self.enable_combo_box(i)

        # external code to empty the (dynamic layout)
        self.VLine.hide()

        # removing 'share' and 'cancel' button
        while self.shareButtonsLayout.count() > 0:
            item = self.shareButtonsLayout.takeAt(0)
            if not item:
                continue

            widget = item.widget()
            if widget:
                widget.close()

        # removing teacher's checkboxes
        while self.sharingTeacherLayout.count() > 0:
            item = self.sharingTeacherLayout.takeAt(0)
            if not item:
                continue

            widget = item.widget()
            if widget:
                widget.close()

        # resetting flag after their use
        self.windowOpened = False
        self.sharingMade = False

    # for disabling all the drop-downs (for selecting teacher) till sharing window is open
    def disable_combo_box(self, at_index):
        self.teacher_combo_boxes[at_index].setEnabled(False)

    # for enabling all the drop-downs (which were disable due to opening of sharing window)
    def enable_combo_box(self, at_index):
        self.teacher_combo_boxes[at_index].setEnabled(True)

    # creating checkboxes
    def create_checkboxes(self, index_of_teacher, for_subject):
        checkbox = QCheckBox(self.teachers[index_of_teacher])
        checkbox.toggled.connect(lambda: self.process_checkbox(index_of_teacher, for_subject))
        return checkbox

    # function called whenever teacher checkbox is toggled
    def process_checkbox(self, teacher_index, for_subject):
        # checkboxes are 2 less than elements in teacher list (as 'none' and 'Shared' are not included)
        checkbox_index = teacher_index - 2
        self.sharedSubjectIndex = for_subject

        selected_teacher = self.teachers[teacher_index]
        # increase or decrease number of teacher selected or checked
        if self.checkBoxes[checkbox_index].isChecked():
            self.teachersSelectedForSharing += 1                # increasing the counter
            self.sharedTeachers.append(selected_teacher)        # adding teacher for sharing subject
        else:
            self.teachersSelectedForSharing -= 1                # decreasing the counter

            # removing the teacher from the sharedTeacher list
            for i in range(len(self.sharedTeachers)):
                if selected_teacher == self.sharedTeachers[i]:
                    self.sharedTeachers.remove(self.sharedTeachers[i])

        # enabling 'Share' button only if more than 1 teacher is selected
        if self.teachersSelectedForSharing > 1:
            self.share_teacher_button.setEnabled(True)
        else:
            self.share_teacher_button.setEnabled(False)

    # updates the list of subjects that are shared by different teacher for a semester/batch
    def share_subject_between_teachers(self):
        # generating a subject-teacher mapping in the form dictionary
        subject = self.subjectList[self.sharedSubjectIndex]
        mapping = {subject: self.sharedTeachers}

        # removing dedicated mapping if exists in final list
        for index in self.mapped_subjects_index:
            if index == self.sharedSubjectIndex:
                self.remove_mapping(index)

        # update the value (ie teacher names) if mapping for the same subject already exists
        if len(self.sharedList) > 0:                                    # means some mappings exist
            subject_match_found = False
            for each_dictionary in self.sharedList:
                for key, values in each_dictionary.items():
                    if subject == key:
                        each_dictionary[key] = self.sharedTeachers      # updating the teacher names for the subject
                        subject_match_found = True
                        break

                if subject_match_found:
                    break                                               # stop looking for the subject
                else:                                                   # if mapping for the subject doesn't exists
                    # print('creating new mapping')
                    self.sharedList.append(mapping)                     # append the new mapping
                    self.mapped_shared_subjects_index.append(self.sharedSubjectIndex)
                    break

        else:                                                           # if no mapping exists
            self.sharedList.append(mapping)
            self.mapped_shared_subjects_index.append(self.sharedSubjectIndex)

        # updating the flag to refer sharing is made
        self.sharingMade = True

        # test output
        # print('Shared List is as follow:')
        # for i in self.sharedList:
        #     print(i)
        # print(f'Shared Indexes: {self.mapped_shared_subjects_index}')
        # print()
        # print('Final List is as follow:')
        # for i in self.finalList:
        #     print(i)
        # print(f'Indexes mapped: {self.mapped_subjects_index}')
        # print()

        # closing the shared window after done processing
        self.close_sharing_section()

    # function to remove subject-teachers mapping from shared list, for which a dedicated teacher mapping has been done
    def remove_shared_mapping(self, mapping_index):
        for mapping in self.sharedList:
            for subject, teachers in mapping.items():
                if subject == self.subjectList[mapping_index]:
                    self.sharedList.remove(mapping)
                    self.mapped_shared_subjects_index.remove(mapping_index)

    # function to remove teacher-subjects mapping, for which a shared mapping has been made
    def remove_mapping(self, mapping_index):
        for each_mapping in self.finalList:
            for teacher, subjects in each_mapping.items():
                for subject in subjects:
                    if subject == self.subjectList[mapping_index]:
                        self.finalList.remove(each_mapping)
                        self.mapped_subjects_index.remove(mapping_index)

    def teacher_to_subjects_map(self, teacher_name, subject_name, index):
        exists_subject_mapping = False
        teacher_to_replace = None
        found_subject = False

        # checking if a mapping for given subject already exists (in shared mapping list). If exists, delete the mapping
        for i in self.mapped_shared_subjects_index:
            if i == index:
                self.remove_shared_mapping(index)

        # checking if a mapping for given subject already exists (in dedicated mapping list)
        for i in self.mapped_subjects_index:
            if i == index:
                exists_subject_mapping = True

        if exists_subject_mapping:
            for each_mapping in self.finalList:
                for key, values in each_mapping.items():        # iterate on each mapping (ie dictionary),
                    for value in values:                        # iterate on dictionary values (ie a list) 1 by 1,
                        if value == self.subjectList[index]:    # checking if the subject is already mapped,
                            teacher_to_replace = key            # store name of teacher to be replaced for the subject
                            found_subject = True
                            break                               # stop iterating further on values

                if found_subject:
                    break                                       # stop iterating further on mappings (ie dictionaries)

            # iterate on finalList to find the teacher which has to be replaced
            for each_dictionary in self.finalList:
                for key, value in each_dictionary.items():
                    if key == teacher_to_replace:
                        mapping_to_remove = {key: value}            # fetching the desired dictionary
                        self.finalList.remove(mapping_to_remove)    # removing it from the list

            new_mapping = {teacher_name: [subject_name]}            # creating new mapping
            self.finalList.append(new_mapping)                      # appending it to list

        else:
            found_teacher_match = False
            mapping = {teacher_name: [subject_name]}                # creating mapping in form of dictionary

            if len(self.finalList) == 0:                            # when no 1 to 1 mapping is made
                self.finalList.append(mapping)                      # appending the mapping into final list
                self.mapped_subjects_index.append(index)

            else:                                                   # if some 1 to 1 mapping exists already
                for each_mapping in self.finalList:
                    for key, value in each_mapping.items():
                        if teacher_name == key:                     # if teacher is already teaching a subject
                            each_mapping[key].append(subject_name)  # append another subject
                            self.mapped_subjects_index.append(index)
                            found_teacher_match = True

                    if found_teacher_match:
                        break                                       # stop looking for teacher in finalList

                if not found_teacher_match:
                    self.finalList.append(mapping)                  # add a new mapping in finalList
                    self.mapped_subjects_index.append(index)

    # helper function used when converting subject-teacher mapping to teacher-subject mapping
    def get_index_for_subject(self, subject_name):
        for i in range(len(self.subjectList)):
            if subject_name == self.subjectList[i]:
                return i                                            # i is an index

    # generating time table after all required mappings are made
    def generate_time_table(self, batch, timing):
        # converting subject-teachers mapping into subject-teacher mappings
        for each_mapping in self.sharedList:
            for subject, teachers in each_mapping.items():
                sub_index = self.get_index_for_subject(subject)
                for teacher in teachers:
                    self.teacher_to_subjects_map(teacher, subject, sub_index)

        # calling time-table output class
        self.show_time_table(batch, timing)

    # calling another widget/window which displays the time-table
    def show_time_table(self, batch, timing):
        self.output = TimeTableDisplayWindow(None, self.finalList, self.course, self.semester, batch, timing)
        self.output.show()
