"""
Represent a window (Widget) for inputting all basic information about the school.
This window is meant for admins only and is displayed only after the admin login.
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget,  QHBoxLayout
)
from Global.Styles.Colors import *
from Interfaces.BasicInfo_Nav import BasicInfoNavSection


# represents whole window
class SchoolBasicInfoWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # title of the main window
        window_title = 'School Basic Information'
        self.setWindowTitle(window_title)

        # values are in pixels
        self.windowTopMargin = 30
        self.windowLeftMargin = 50
        self.windowHeight = 600
        self.windowWidth = 900

        # appearance of the window (changing background as dark)
        self.setAutoFillBackground(True)
        self.mainPalette = self.palette()
        self.mainPalette.setColor(self.backgroundRole(), darcula_background)
        self.setPalette(self.mainPalette)

        # initializing size and the location on screen for the window
        self.setGeometry(self.windowTopMargin, self.windowLeftMargin, self.windowWidth, self.windowHeight)

        # main layout of the widget
        self.mainLayout = QHBoxLayout(self)

        """the structure of the window is like follow:
             __________________________________________________
            |                       |                                                |
            |  navigation    |              context                     |
            |   section        |              section                      |
            |                       |                                                |
            ___________________________________________________
            
        """

        # navigation section widget (to be placed on the left side)
        self.navigationSection = BasicInfoNavSection(self)

        # context section widget (to be placed on the right side)
        self.contextSection = QWidget(self)

        # adding above sections (i.e. navigation and context) to the main layout
        self.mainLayout.addWidget(self.navigationSection, 1)
        self.mainLayout.addWidget(self.contextSection, 3)

        self.mainLayout.setContentsMargins(0, 0, 0, 0)         # remove margins
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    basic_info_window_object = SchoolBasicInfoWindow()
    basic_info_window_object.show()
    sys.exit(application.exec_())