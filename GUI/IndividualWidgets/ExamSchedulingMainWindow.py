import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main window properties
        self.setFixedSize(900, 520)
        self.setWindowTitle('Main Window')

        # central widget (main parent widget)
        self.container = QWidget(self)
        self.container.setGeometry(0, 21, 890, 400)
        # self.container.setStyleSheet(" border:1px solid rgb(255, 170, 255);")
        self.semSubButtonLayout = QVBoxLayout(self.container)
        self.combiningLayout = QHBoxLayout(self.container)
        self.listOfCombo = []

        self.semesterCheck()
        self.courseCombo()
        self.SubmitCancel()

    def semesterCheck(self):
        self.containerLayout = QVBoxLayout(self.container)
        self.checkBoxes = []
        self.checkBoxesList = []
        self.SemesterLabel = QLabel(" CHOOSE THE SEMESTERS ", self.container)
        self.containerLayout.addWidget(self.SemesterLabel)

        for semesters in range(6):
            # print (semesters+1)
            self.checkBoxes.append(str(semesters + 1))

        for semesters in self.checkBoxes:
            # print(semesters)
            self.returnFunctionCombo = self.comboCreation(semesters)
            self.checkBoxesList.append(self.returnFunctionCombo)
            # print(self.checkBoxesList)
            self.containerLayout.addWidget(self.returnFunctionCombo)

        self.combiningLayout.addLayout(self.containerLayout)

    def comboCreation(self, i):
        # print(i)
        self.multipleCheckboxes = QCheckBox(i, self.container)
        # self.multipleCheckboxes.stateChanged.connect(self.clickBox)
        return self.multipleCheckboxes

    def courseCombo(self):
        self.comboLayout = QVBoxLayout(self.container)
        self.comboBoxesList = ["MCA", "M Sc. IT", "MA(ENGLISH)", "MCA(EVENING)"]
        self.courseLabel = QLabel(" CHOOSE THE COURSE ", self.container)
        self.comboLayout.addWidget(self.courseLabel)

        self.comboBox = QComboBox(self.container)
        self.comboBox.addItems(self.comboBoxesList)
        self.comboLayout.addWidget(self.comboBox)

        self.combiningLayout.addLayout(self.comboLayout)

    def SubmitCancel(self):
        self.buttonLayout = QHBoxLayout(self.container)
        self.Submit = QPushButton("SUBMIT", self.container)
        self.Submit.clicked.connect(self.clickBox)
        self.Cancel = QPushButton("CANCEL", self.container)

        self.buttonLayout.addWidget(self.Submit)
        self.buttonLayout.addWidget(self.Cancel)

        self.semSubButtonLayout.addLayout(self.combiningLayout)
        self.semSubButtonLayout.addLayout(self.buttonLayout)

    def clickBox(self):
        cur_txt = self.comboBox.currentText()
        print(cur_txt)
        self.semestersSelected = []
        for i in range(6):
            if self.checkBoxesList[i].isChecked():
                # print(self.checkBoxesList[i].text())
                # print("checked")
                self.semestersSelected.append(self.checkBoxesList[i].text())

            else:
                pass
                # print(self.checkBoxesList[i].text())
                # print('Unchecked')
        print(self.semestersSelected)
        exit()


def main():
    application = QApplication(sys.argv)
    main_window_obj = MainWindow()
    main_window_obj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
