import sys
from GUI.GUI_ModulePanel import *
from GUI.GUI_NavigationPanel import *
from GUI.OutputWidgetsContainer import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main window properties
        self.setFixedSize(1080, 640)
        self.setWindowTitle('Main Window')

        # menu bar
        self.menuBar = QMenuBar(self)
        self.menuBar.setGeometry(0, 0, 1080, 29)
        # self.menuBar.setStyleSheet('background-color: red;')
        # adding Menu Tabs
        self.applicationTab = self.menuBar.addMenu('Application')
        self.aboutTab = self.menuBar.addMenu('About')
        self.helpTab = self.menuBar.addMenu('Help')

        # status bar properties
        self.statusBar().showMessage('This is a status bar.')

        # container of all widgets, except for menu bar and status bar
        self.rootContainer = QWidget(self)
        self.rootContainer.setGeometry(0, 30, 1080, 588)
        # self.rootContainer.setStyleSheet('border: 1px solid black')             # for testing purpose

        # layout of root container
        self.rootContainerLayout = QHBoxLayout(self.rootContainer)

        """---------------------- Root Container child Widgets ---------------------"""
        # Root container consists of 3 main areas in sequence (horizontally):
        # 1) Modules Panel      2) Options of Selected Modules          3) Container to show all outputs

        # A sub container (i.e. 3rd area) for displaying any required widget as output
        self.outputContainer = DynamicWidgets(self.rootContainer)
        self.changeDynamicWidgetRef = self.outputContainer.change_window

        # An Option list (i.e. 2nd area) for the selected module
        self.moduleOptions = NavigationPanel(self.rootContainer, self.changeDynamicWidgetRef)

        # A Navigation Panel (i.e. 1st area) containing each module of RADAtR
        self.modulesPanel = LeftModulePanel(self.rootContainer, self.moduleOptions)
        # self.modulesPanel.timeTableButton.clicked.connect(self.toggle_nav)

        # horizontally aligning the 3 main areas (modulesPanel, moduleOptions, outputContainer)
        self.rootContainerLayout.addWidget(self.modulesPanel.modulePanel)
        self.rootContainerLayout.addWidget(self.moduleOptions.navPanel)
        self.rootContainerLayout.addWidget(self.outputContainer.OutputWidgetsContainer)
        self.rootContainerLayout.setContentsMargins(0, 0, 0, 0)
        self.rootContainerLayout.setSpacing(0)


def main():
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    main_window_obj = MainWindow()
    main_window_obj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
