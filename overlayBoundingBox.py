import sys
from PyQt5 import QtGui, QtWidgets, QtCore

class mymainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
            )
        self.setGeometry(QtWidgets.QStyle.alignedRect(
            QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
            QtCore.QSize(220, 320),
            QtWidgets.qApp.desktop().availableGeometry()))

    def mousePressEvent(self, event):
        QtGui.qApp.quit()

app = QtWidgets.QApplication(sys.argv)
mywindow = mymainwindow()
mywindow.show()
app.exec_()
