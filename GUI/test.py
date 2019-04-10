print("true")
import sys
from PyQt5.QtWidgets import *
from Detached.Global.Variables.varTimetableFile import *
from Detached.Classes.ExamScheduling import *
ExamScheduleMappingObj = ExamScheduleMapping()


class Timetable(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Time Table'
        self.mainwindowprop()

        # ExamScheduleMappingObj.place_subjects_to_list()

    def mainwindowprop(self):
        self.setWindowTitle(self.title)
        # self.setGeometry(300, 300, 800, 300)
        self.createtable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    def createtable(self):
        # Create table

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(totalWorkingDays)
        self.tableWidget.setColumnCount(total_slot_no)
        self.tableWidget.move(0, 0)

        self.tableWidget.setVerticalHeaderLabels(days_list)
        self.tableWidget.setHorizontalHeaderLabels(slot_list)

        # self.tableWidget.setHorizontalHeaderLabels()
        l = 0
        for i in range((totalWorkingDays)):
            j= 0

            while(j<=total_slot_no-1):
                # print(i , j)
                # print(l)
                self.tableWidget.setItem(i, j, QTableWidgetItem(ExamScheduleMappingObj.a[l]))
                j = j+1
                if (l < len(ExamScheduleMappingObj.a)):
                    l = l + 1
        """self.tableWidget.setItem(0, 0, QTableWidgetItem())
        self.tableWidget.setItem(0, 1, QTableWidgetItem())
        self.tableWidget.setItem(0, 2, QTableWidgetItem())"""

        self.tableWidget.resizeColumnsToContents()


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjQApplication.setStyle('Fusion')
    Objtimetable = Timetable()
    Objtimetable.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()
