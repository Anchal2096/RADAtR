import sys
from PyQt5.QtWidgets import *
from Detached.Global.Variables.varTimetableFile import *
from Detached.Classes.ExamScheduling import *


class ExamScheduleOutputWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main window properties

        self.setFixedSize(900, 520)
        self.setWindowTitle('Time Table Scheduling')

        """----------------------WIDGETS USED-------------------------------------------"""
        # central widget (main parent widget)
        self.container = QWidget(self)
        # self.container.setFixedSize(880, 480)
        self.container.setGeometry(10, 20, 880, 480)
        # self.container.setStyleSheet(" border:1px solid rgb(0, 0, 25);")

        # contains the text 'Time Table Scheduling'
        self.upper_Title_Widget = QWidget(self.container)
        # self.upper_Title_Widget.setFixedSize(880, 50)
        self.upper_Title_Widget.setGeometry(0, 5, 880, 40)
        # self.upper_Title_Widget.setStyleSheet(" border:1px solid rgb(0, 140, 255);")

        # contains the top horizontal line
        self.top_h_line_widget = QWidget(self.container)
        self.top_h_line_widget.setGeometry(0, 42, 880, 20)
        # self.top_h_line_widget.setStyleSheet(" border:1px solid rgb(70, 90, 255);")

        # contains a TimeTable
        self.Timetable_Widget = QWidget(self.container)
        # self.semester_Widget_Widget.setFixedSize(440, 300)
        self.Timetable_Widget.setGeometry(90, 55, 500, 380)
        # self.Timetable_Widget.setStyleSheet(" border:1px solid rgb(255, 45, 255);")

        # contains the last three buttons i.e. Submit, Reset, Cancel
        self.lower_Widget = QWidget(self.container)
        # self.lower_Widget.setFixedSize(880, 40)
        self.lower_Widget.setGeometry(400, 440, 480, 40)
        # self.lower_Widget.setStyleSheet(" border:1px solid rgb(0, 200, 45);")

        # contains the last vertical line used at the bottom of the window
        self.last_Line_widget = QWidget(self.container)
        # self.last_Line_widget.setFixedSize(880, 20)
        self.last_Line_widget.setGeometry(0, 420, 880, 20)
        # self.last_Line_widget.setStyleSheet(" border:1px solid rgb(0, 2, 45);")

        """------------------------INITIAL VALUES OF OBJECTS USED ----------------------"""

        """"----------------------- calling of functions ---------------------------------"""
        self.button_creation()
        self.title_label()
        self.add_top_h_line()
        # self.add_v_line()
        self.add_last_h_line()
        self.createtable()

    """this function creates the checkboxes for the user to select the semester"""

    def title_label(self):
        # self.TitleLayout = QVBoxLayout(self.upper_Title_Widget)
        self.SemesterLabel = QLabel(" EXAMINATION SCHEDULING ", self.upper_Title_Widget)
        self.SemesterLabel.setStyleSheet("font: 15pt Sans MS")

    """ this function adds the top horizontal line """

    def add_top_h_line(self):
        self.top_h_line_Layout = QVBoxLayout(self.top_h_line_widget)
        self.VLine = QFrame(self.top_h_line_widget)
        self.VLine.setFrameShape(QFrame.HLine)
        self.VLine.setFrameShadow(QFrame.Sunken)
        self.top_h_line_Layout.addWidget(self.VLine)

    """this function adds the last horizontal line"""

    def add_last_h_line(self):
        self.last_lineLayout = QVBoxLayout(self.last_Line_widget)
        self.VLine = QFrame(self.last_Line_widget)
        self.VLine.setFrameShape(QFrame.HLine)
        self.VLine.setFrameShadow(QFrame.Sunken)
        self.last_lineLayout.addWidget(self.VLine)

    def button_creation(self):
        self.buttonLayout = QHBoxLayout(self.lower_Widget)
        self.print = QPushButton("PRINT", self.lower_Widget)
        self.print.setFixedSize(100, 30)
        # self.Submit.clicked.connect(self.click_box)
        self.next_button = QPushButton("NEXT", self.lower_Widget)
        self.next_button.clicked.connect(lambda: self.assign_mappings())
        self.next_button.setFixedSize(100, 30)
        self.cancel = QPushButton("CANCEL", self.lower_Widget)
        self.cancel.setFixedSize(100, 30)
        self.cancel.clicked.connect(exit)
        # self.Reset.clicked.connect()

        self.buttonLayout.addWidget(self.print)
        self.buttonLayout.addWidget(self.next_button)
        self.buttonLayout.addWidget(self.cancel)

    def createtable(self):
        # Create table
        self.TimetableLayout = QHBoxLayout(self.Timetable_Widget)
        self.tableWidget = QTableWidget()
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tableWidget.setRowCount(ExamScheduleMappingObj.working_days)
        self.tableWidget.setColumnCount(ExamScheduleMappingObj.total_slots)

        self.tableWidget.setVerticalHeaderLabels(days_list)
        self.tableWidget.setHorizontalHeaderLabels(slot_list)

        # self.tableWidget.setHorizontalHeaderLabels()
        l = 0
        for rows in range(totalWorkingDays):
            column = 0

            while column <= total_slot_no - 1:
                # print(i , j)
                # print(l)
                self.tableWidget.setItem(rows, column,
                                         QTableWidgetItem(ExamScheduleMappingObj.random_list[l]))
                self.tableWidget.setRowHeight(column, 50)
                self.tableWidget.setRowHeight(rows, 50)
                # self.tableWidget.setColumnWidth(i, 50)
                column = column + 1
                if l < len(ExamScheduleMappingObj.random_list):
                    l = l + 1

        # self.tableWidget.resizeColumnsToContents()
        self.TimetableLayout.addWidget(self.tableWidget)

    def assign_mappings(self):
        for i in range(1):
            ExamScheduleMappingObj = ExamScheduleMapping()
            l = 0
            for rows in range(totalWorkingDays):
                column = 0

                while column <= total_slot_no - 1:
                    # print(i , j)
                    # print(l)
                    self.tableWidget.setItem(rows, column,
                                             QTableWidgetItem(ExamScheduleMappingObj.random_list[l]))
                    self.tableWidget.setRowHeight(column, 50)
                    self.tableWidget.setRowHeight(rows, 50)
                    # self.tableWidget.setColumnWidth(i, 50)
                    column = column + 1
                    if l < len(ExamScheduleMappingObj.random_list):
                        l = l + 1

def main():
    application = QApplication(sys.argv)
    scheduleoutput_window_obj = ExamScheduleOutputWindow()
    scheduleoutput_window_obj.show()
    sys.exit(application.exec_())

if __name__ == '__main__':
    main()

