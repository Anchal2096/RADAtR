"""This class intents to provide modularity and hence, reducing the code of GUI_NavigationPanel.
    This file is not being used anywhere because of the unexpected error (class isn't accepting any arguments)"""


class TimeTableOptions:
    def __int__(self, parent=None):
        # used to help in determining the start index for another list, embedded in same stacking list
        self.totalOptions = 4                               # this must be update if new options are added

        self.testTimeTable = QWidget(parent)
        self.timeTableOptionsLayout = QVBoxLayout(self.testTimeTable)

        # heading for Time-Table List
        self.timeTableHead = QLabel('Time Table:', self.testTimeTable)

        # creating options list for time table module
        self.timeTableList = QListWidget(self.testTimeTable)

        # List items
        self.timeTableList.insertItem(0, 'Creation')
        self.timeTableList.insertItem(1, 'Viewing')
        self.timeTableList.insertItem(2, 'Editing')
        self.timeTableList.insertItem(3, 'Deletion')

        # stacking up all widgets in vertical layout
        self.timeTableOptionsLayout.addWidget(self.timeTableHead)
        self.timeTableOptionsLayout.addWidget(self.timeTableList)
        self.timeTableOptionsLayout.setContentsMargins(0, 3, 0, 3)
