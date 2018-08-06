from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from TimeTable import Ui_MainWindow
import chooseCourse


class main (QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.load)
        self.closeButton.clicked.connect(self.closeit)

    def closeit(self):
        self.close()

    def load(self):
        data = chooseCourse.creator()
        for i in data:
            for j in range(4, 18):
                for k in range(2, 16):
                    item = self.tableWidget.item(j, k)
                    if item.text() == i:
                        item.setBackground(QtGui.QColor(61, 234, 14))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = main()
    window.show()
    sys.exit(app.exec_())
