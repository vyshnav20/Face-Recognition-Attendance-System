import os
import sys

from st_ui import *
import ctypes

from Custom_Widgets.Widgets import *

settings = QSettings()
class MainWind(QMainWindow,):
    def __init__(self):
        
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        icon=QIcon('icon.ico')
        self.setWindowIcon(icon)
        loadJsonStyle(self, self.ui, jsonFiles = {"style2.json"}) 

if __name__ == "__main__":
    myappid = 'fras' 
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    app = QApplication(sys.argv)
    window = MainWind()
    icon=QIcon('icon.ico')
    app.setWindowIcon(icon)
    window.showMaximized()  
    sys.exit(app.exec_())

