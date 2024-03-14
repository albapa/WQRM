# Mark Davenport 2112658
# ES327 Project

import sys
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

import numpy as np

import serial.tools.list_ports
import serial

from DataGenerator1 import DataGenerator

ConRunning = "O"
port = 'COM3'
Key = ["X", "X", "X", "X", "X"]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MainTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.MainTabs.setGeometry(QtCore.QRect(0, 0, 1191, 761))
        self.MainTabs.setMaximumSize(QtCore.QSize(1191, 761))
        self.MainTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.MainTabs.setDocumentMode(True)
        self.MainTabs.setTabsClosable(False)
        self.MainTabs.setMovable(False)
        self.MainTabs.setObjectName("MainTabs")
        self.Start = QtWidgets.QWidget()
        self.Start.setMaximumSize(QtCore.QSize(1191, 740))
        self.Start.setObjectName("Start")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Start)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 10, 362, 721))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.StartLeft = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.StartLeft.setContentsMargins(0, 0, 0, 0)
        self.StartLeft.setObjectName("StartLeft")
        self.Info1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Info1.setMinimumSize(QtCore.QSize(360, 0))
        self.Info1.setMaximumSize(QtCore.QSize(360, 16777215))
        self.Info1.setWordWrap(True)
        self.Info1.setObjectName("Info1")
        self.StartLeft.addWidget(self.Info1)
        self.Info2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Info2.setMinimumSize(QtCore.QSize(360, 0))
        self.Info2.setWordWrap(True)
        self.Info2.setObjectName("Info2")
        self.StartLeft.addWidget(self.Info2)
        self.Info3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Info3.setMinimumSize(QtCore.QSize(360, 0))
        self.Info3.setWordWrap(True)
        self.Info3.setObjectName("Info3")
        self.StartLeft.addWidget(self.Info3)
        self.Info4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Info4.setMinimumSize(QtCore.QSize(360, 0))
        self.Info4.setWordWrap(True)
        self.Info4.setObjectName("Info4")
        self.StartLeft.addWidget(self.Info4)
        self.Info5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Info5.setMinimumSize(QtCore.QSize(360, 0))
        self.Info5.setWordWrap(True)
        self.Info5.setObjectName("Info5")
        self.StartLeft.addWidget(self.Info5)
        self.Line1 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Line1.setMinimumSize(QtCore.QSize(360, 0))
        self.Line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line1.setObjectName("Line1")
        self.StartLeft.addWidget(self.Line1)
        self.Connect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Connect.setMinimumSize(QtCore.QSize(360, 0))
        self.Connect.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.Connect.setObjectName("Connect")
        self.StartLeft.addWidget(self.Connect)
        self.StartStatus = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.StartStatus.setMinimumSize(QtCore.QSize(360, 0))
        self.StartStatus.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.StartStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.StartStatus.setObjectName("StartStatus")
        self.StartLeft.addWidget(self.StartStatus)
        self.Lin2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Lin2.setMinimumSize(QtCore.QSize(360, 0))
        self.Lin2.setFrameShape(QtWidgets.QFrame.HLine)
        self.Lin2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Lin2.setObjectName("Lin2")
        self.StartLeft.addWidget(self.Lin2)
        spacerItem = QtWidgets.QSpacerItem(360, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.StartLeft.addItem(spacerItem)
        self.Line3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.Line3.setFrameShape(QtWidgets.QFrame.VLine)
        self.Line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line3.setObjectName("Line3")
        self.StartLeft.addWidget(self.Line3)
        self.Mark = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Mark.setMinimumSize(QtCore.QSize(360, 0))
        self.Mark.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Mark.setObjectName("Mark")
        self.StartLeft.addWidget(self.Mark)
        self.Project = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Project.setMinimumSize(QtCore.QSize(360, 0))
        self.Project.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Project.setObjectName("Project")
        self.StartLeft.addWidget(self.Project)
        self.WarwickLogo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.WarwickLogo.setMaximumSize(QtCore.QSize(170, 55))
        self.WarwickLogo.setText("")
        self.WarwickLogo.setPixmap(QtGui.QPixmap("WarwickLogo.png"))
        self.WarwickLogo.setScaledContents(True)
        self.WarwickLogo.setObjectName("WarwickLogo")
        self.StartLeft.addWidget(self.WarwickLogo)
        self.WQRMPicture = QtWidgets.QLabel(self.Start)
        self.WQRMPicture.setGeometry(QtCore.QRect(470, 80, 661, 581))
        self.WQRMPicture.setText("")
        self.WQRMPicture.setPixmap(QtGui.QPixmap("Background2.png"))
        self.WQRMPicture.setScaledContents(True)
        self.WQRMPicture.setObjectName("WQRMPicture")
        self.MainTabs.addTab(self.Start, "")
        self.Calibrate = QtWidgets.QWidget()
        self.Calibrate.setObjectName("Calibrate")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Calibrate)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 362, 721))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.CalibrateLeft = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.CalibrateLeft.setContentsMargins(0, 0, 0, 0)
        self.CalibrateLeft.setObjectName("CalibrateLeft")
        self.Info6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Info6.setMinimumSize(QtCore.QSize(360, 0))
        self.Info6.setMaximumSize(QtCore.QSize(200000, 16777215))
        self.Info6.setWordWrap(True)
        self.Info6.setObjectName("Info6")
        self.CalibrateLeft.addWidget(self.Info6)
        self.Line4 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.Line4.setMinimumSize(QtCore.QSize(360, 0))
        self.Line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line4.setObjectName("Line4")
        self.CalibrateLeft.addWidget(self.Line4)
        self.Info7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Info7.setObjectName("Info7")
        self.CalibrateLeft.addWidget(self.Info7)
        self.CalibrateStatus = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.CalibrateStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.CalibrateStatus.setObjectName("CalibrateStatus")
        self.CalibrateLeft.addWidget(self.CalibrateStatus)
        self.Align = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Align.setMinimumSize(QtCore.QSize(360, 0))
        self.Align.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.Align.setObjectName("Align")
        self.CalibrateLeft.addWidget(self.Align)
        self.Line5 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.Line5.setMinimumSize(QtCore.QSize(360, 0))
        self.Line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line5.setObjectName("Line5")
        self.CalibrateLeft.addWidget(self.Line5)
        spacerItem1 = QtWidgets.QSpacerItem(360, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.CalibrateLeft.addItem(spacerItem1)
        self.MainTabs.addTab(self.Calibrate, "")
        self.Correlate = QtWidgets.QWidget()
        self.Correlate.setObjectName("Correlate")
        self.CorrelateRight = QtWidgets.QTabWidget(self.Correlate)
        self.CorrelateRight.setGeometry(QtCore.QRect(400, 10, 791, 721))
        self.CorrelateRight.setObjectName("CorrelateRight")
        
        ## Acceleration Framework
        self.CorrelateAcceleration = QtWidgets.QWidget()
        self.CorrelateAcceleration.setObjectName("CorrelateAcceleration")
        self.CorrelateAccelerationFrame = QtWidgets.QFrame(self.CorrelateAcceleration)
        self.CorrelateAccelerationFrame.setGeometry(QtCore.QRect(10, 10, 771, 681))
        self.CorrelateAccelerationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CorrelateAccelerationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CorrelateAccelerationFrame.setObjectName("CorrelateAccelerationFrame")

        # Create horizontal layout
        self.HorizontalLayout4 = QtWidgets.QHBoxLayout(self.CorrelateAccelerationFrame)
        self.HorizontalLayout4.setObjectName("HorizontalLayout4")

        # Canvas
        self.CorrelateAccelerationFigure = plt.figure()
        self.CorrelateAccelerationCanvas = FigureCanvas(self.CorrelateAccelerationFigure)

        # Add Canvas
        self.HorizontalLayout4.addWidget(self.CorrelateAccelerationCanvas)

        # End

        self.CorrelateRight.addTab(self.CorrelateAcceleration, "")

        ## Velocity Framework
        self.CorrelateVelocity = QtWidgets.QWidget()
        self.CorrelateVelocity.setObjectName("CorrelateVelocity")
        self.CorrelateVelocityFrame = QtWidgets.QFrame(self.CorrelateVelocity)
        self.CorrelateVelocityFrame.setGeometry(QtCore.QRect(10, 10, 771, 681))
        self.CorrelateVelocityFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CorrelateVelocityFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CorrelateVelocityFrame.setObjectName("CorrelateVelocityFrame")
 
        # Create horizontal layout
        self.HorizontalLayout5 = QtWidgets.QHBoxLayout(self.CorrelateVelocityFrame)
        self.HorizontalLayout5.setObjectName("HorizontalLayout5")

        # Canvas
        self.CorrelateVelocityFigure = plt.figure()
        self.CorrelateVelocityCanvas = FigureCanvas(self.CorrelateVelocityFigure)

        # Add Canvas
        self.HorizontalLayout5.addWidget(self.CorrelateVelocityCanvas)

        # End
       
        self.CorrelateRight.addTab(self.CorrelateVelocity, "")

        ## Displacement Framework
        self.CorrelateDisplacement = QtWidgets.QWidget()
        self.CorrelateDisplacement.setObjectName("CorrelateDisplacement")
        self.CorrelateDisplacementFrame = QtWidgets.QFrame(self.CorrelateDisplacement)
        self.CorrelateDisplacementFrame.setGeometry(QtCore.QRect(10, 10, 771, 681))
        self.CorrelateDisplacementFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CorrelateDisplacementFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CorrelateDisplacementFrame.setObjectName("CorrelateDisplacementFrame")
 
        # Create horizontal layout
        self.HorizontalLayout6 = QtWidgets.QHBoxLayout(self.CorrelateDisplacementFrame)
        self.HorizontalLayout6.setObjectName("HorizontalLayout6")

        # Canvas
        self.CorrelateDisplacementFigure = plt.figure()
        self.CorrelateDisplacementCanvas = FigureCanvas(self.CorrelateDisplacementFigure)

        # Add Canvas
        self.HorizontalLayout6.addWidget(self.CorrelateDisplacementCanvas)

        # End
              
        self.CorrelateRight.addTab(self.CorrelateDisplacement, "")


        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.Correlate)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 10, 362, 721))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.CorrelateLeft = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.CorrelateLeft.setContentsMargins(0, 0, 0, 0)
        self.CorrelateLeft.setObjectName("CorrelateLeft")
        self.Info8 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.Info8.setMinimumSize(QtCore.QSize(360, 0))
        self.Info8.setMaximumSize(QtCore.QSize(200000, 16777215))
        self.Info8.setWordWrap(True)
        self.Info8.setObjectName("Info8")
        self.CorrelateLeft.addWidget(self.Info8)
        self.Info9 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.Info9.setMinimumSize(QtCore.QSize(360, 0))
        self.Info9.setWordWrap(True)
        self.Info9.setObjectName("Info9")
        self.CorrelateLeft.addWidget(self.Info9)
        self.Info10 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.Info10.setMinimumSize(QtCore.QSize(360, 0))
        self.Info10.setWordWrap(True)
        self.Info10.setObjectName("Info10")
        self.CorrelateLeft.addWidget(self.Info10)
        self.Line6 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.Line6.setMinimumSize(QtCore.QSize(360, 0))
        self.Line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line6.setObjectName("Line6")
        self.CorrelateLeft.addWidget(self.Line6)
        self.CRaa = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.CRaa.setObjectName("CRaa")
        self.CRaa.addItem("")
        self.CRaa.addItem("")
        self.CorrelateLeft.addWidget(self.CRaa)
        self.CRiav = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.CRiav.setObjectName("CRiav")
        self.CRiav.addItem("")
        self.CRiav.addItem("")
        self.CRiav.addItem("")
        self.CRiav.addItem("")
        self.CRiav.addItem("")
        self.CRiav.addItem("")
        self.CorrelateLeft.addWidget(self.CRiav)
        self.CRnc = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.CRnc.setObjectName("CRnc")
        self.CRnc.addItem("")
        self.CRnc.addItem("")
        self.CRnc.addItem("")
        self.CRnc.addItem("")
        self.CorrelateLeft.addWidget(self.CRnc)
        self.CRcl = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.CRcl.setObjectName("CRcl")
        self.CRcl.addItem("")
        self.CRcl.addItem("")
        self.CRcl.addItem("")
        self.CorrelateLeft.addWidget(self.CRcl)
        self.Line7 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.Line7.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line7.setObjectName("Line7")
        self.CorrelateLeft.addWidget(self.Line7)
        self.CorrelateStatus = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.CorrelateStatus.setMinimumSize(QtCore.QSize(360, 0))
        self.CorrelateStatus.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.CorrelateStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.CorrelateStatus.setObjectName("CorrelateStatus")
        self.CorrelateLeft.addWidget(self.CorrelateStatus)
        self.CRStart = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.CRStart.setMinimumSize(QtCore.QSize(360, 0))
        self.CRStart.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.CRStart.setObjectName("CRStart")
        self.CorrelateLeft.addWidget(self.CRStart)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_4)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.CorrelateLeft.addWidget(self.progressBar)
        self.Line8 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.Line8.setMinimumSize(QtCore.QSize(360, 0))
        self.Line8.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line8.setObjectName("Line8")
        self.CorrelateLeft.addWidget(self.Line8)
        spacerItem2 = QtWidgets.QSpacerItem(360, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.CorrelateLeft.addItem(spacerItem2)
        self.Info11 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Info11.setFont(font)
        self.Info11.setObjectName("Info11")
        self.CorrelateLeft.addWidget(self.Info11)
        self.CRS1X = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.CRS1X.setObjectName("CRS1X")
        self.CorrelateLeft.addWidget(self.CRS1X)
        self.CRS1Y = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.CRS1Y.setObjectName("CRS1Y")
        self.CorrelateLeft.addWidget(self.CRS1Y)
        self.CRS2X = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.CRS2X.setObjectName("CRS2X")
        self.CorrelateLeft.addWidget(self.CRS2X)
        self.Line9 = QtWidgets.QFrame(self.verticalLayoutWidget_4)
        self.Line9.setFrameShape(QtWidgets.QFrame.VLine)
        self.Line9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line9.setObjectName("Line9")
        self.CorrelateLeft.addWidget(self.Line9)
        self.MainTabs.addTab(self.Correlate, "")
        self.Continuous = QtWidgets.QWidget()
        self.Continuous.setObjectName("Continuous")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Continuous)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 10, 362, 721))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.ContinuousLeft = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.ContinuousLeft.setContentsMargins(0, 0, 0, 0)
        self.ContinuousLeft.setObjectName("ContinuousLeft")
        self.Info12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Info12.setMinimumSize(QtCore.QSize(360, 0))
        self.Info12.setMaximumSize(QtCore.QSize(200000, 16777215))
        self.Info12.setWordWrap(True)
        self.Info12.setObjectName("Info12")
        self.ContinuousLeft.addWidget(self.Info12)
        self.Info14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Info14.setMinimumSize(QtCore.QSize(360, 0))
        self.Info14.setWordWrap(True)
        self.Info14.setObjectName("Info14")
        self.ContinuousLeft.addWidget(self.Info14)
        self.Info15 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Info15.setMinimumSize(QtCore.QSize(360, 0))
        self.Info15.setWordWrap(True)
        self.Info15.setObjectName("Info15")
        self.ContinuousLeft.addWidget(self.Info15)
        self.Line10 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.Line10.setMinimumSize(QtCore.QSize(360, 0))
        self.Line10.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line10.setObjectName("Line10")
        self.ContinuousLeft.addWidget(self.Line10)
        self.CNav = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.CNav.setObjectName("CNav")
        self.CNav.addItem("")
        self.CNav.addItem("")
        self.CNav.addItem("")
        self.CNav.addItem("")
        self.CNav.addItem("")
        self.CNav.addItem("")
        self.ContinuousLeft.addWidget(self.CNav)
        self.CNcl = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.CNcl.setObjectName("CNcl")
        self.CNcl.addItem("")
        self.CNcl.addItem("")
        self.CNcl.addItem("")
        self.ContinuousLeft.addWidget(self.CNcl)
        self.Line13 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.Line13.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line13.setObjectName("Line13")
        self.ContinuousLeft.addWidget(self.Line13)
        self.ContinuousStatus = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.ContinuousStatus.setMinimumSize(QtCore.QSize(360, 0))
        self.ContinuousStatus.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.ContinuousStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.ContinuousStatus.setObjectName("ContinuousStatus")
        self.ContinuousLeft.addWidget(self.ContinuousStatus)
        self.CNStart = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.CNStart.setMinimumSize(QtCore.QSize(360, 0))
        self.CNStart.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.CNStart.setObjectName("CNStart")
        self.ContinuousLeft.addWidget(self.CNStart)
        self.Info18 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Info18.setObjectName("Info18")
        self.ContinuousLeft.addWidget(self.Info18)
        self.CNcycles = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CNcycles.setFont(font)
        self.CNcycles.setAlignment(QtCore.Qt.AlignCenter)
        self.CNcycles.setObjectName("CNcycles")
        self.ContinuousLeft.addWidget(self.CNcycles)
        self.Line11 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.Line11.setMinimumSize(QtCore.QSize(360, 0))
        self.Line11.setFrameShape(QtWidgets.QFrame.HLine)
        self.Line11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line11.setObjectName("Line11")
        self.ContinuousLeft.addWidget(self.Line11)
        spacerItem3 = QtWidgets.QSpacerItem(360, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ContinuousLeft.addItem(spacerItem3)
        self.Info17 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Info17.setFont(font)
        self.Info17.setObjectName("Info17")
        self.ContinuousLeft.addWidget(self.Info17)
        self.CNS1X = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.CNS1X.setObjectName("CNS1X")
        self.ContinuousLeft.addWidget(self.CNS1X)
        self.CNS1Y = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.CNS1Y.setObjectName("CNS1Y")
        self.ContinuousLeft.addWidget(self.CNS1Y)
        self.CNS2X = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.CNS2X.setObjectName("CNS2X")
        self.ContinuousLeft.addWidget(self.CNS2X)
        self.Line12 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.Line12.setFrameShape(QtWidgets.QFrame.VLine)
        self.Line12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Line12.setObjectName("Line12")
        self.ContinuousLeft.addWidget(self.Line12)
        self.ContinuousRight = QtWidgets.QTabWidget(self.Continuous)
        self.ContinuousRight.setGeometry(QtCore.QRect(400, 10, 791, 721))
        self.ContinuousRight.setObjectName("ContinuousRight")
        self.ContinuousAcceleration = QtWidgets.QWidget()

        ## Acceleration Framework
        self.ContinuousAcceleration.setObjectName("ContinuousAcceleration")
        self.ContinuousAccelerationFrame = QtWidgets.QFrame(self.ContinuousAcceleration)
        self.ContinuousAccelerationFrame.setGeometry(QtCore.QRect(10, 10, 771, 681))
        self.ContinuousAccelerationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ContinuousAccelerationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContinuousAccelerationFrame.setObjectName("ContinuousAccelerationFrame")

        # Create horizontal layout
        self.HorizontalLayout3 = QtWidgets.QHBoxLayout(self.ContinuousAccelerationFrame)
        self.HorizontalLayout3.setObjectName("HorizontalLayout3")

        # Canvas
        self.ContinuousAccelerationFigure = plt.figure()
        self.ContinuousAccelerationCanvas = FigureCanvas(self.ContinuousAccelerationFigure)

        # Add Canvas
        self.HorizontalLayout3.addWidget(self.ContinuousAccelerationCanvas)

        # End

        self.ContinuousRight.addTab(self.ContinuousAcceleration, "")
        self.ContinuousDisplacement = QtWidgets.QWidget()


        self.ContinuousRight.addTab(self.ContinuousAcceleration, "")
        self.ContinuousVelocity = QtWidgets.QWidget()

        ## Velocity Framework
        self.ContinuousVelocity.setObjectName("ContinuousVelocity")
        self.ContinuousVelocityFrame = QtWidgets.QFrame(self.ContinuousVelocity)
        self.ContinuousVelocityFrame.setGeometry(QtCore.QRect(10, 10, 771, 681))
        self.ContinuousVelocityFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ContinuousVelocityFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContinuousVelocityFrame.setObjectName("ContinuousVelocityFrame")

        # Create horizontal layout
        self.HorizontalLayout2 = QtWidgets.QHBoxLayout(self.ContinuousVelocityFrame)
        self.HorizontalLayout2.setObjectName("HorizontalLayout2")

        # Canvas
        self.ContinuousVelocityFigure = plt.figure()
        self.ContinuousVelocityCanvas = FigureCanvas(self.ContinuousVelocityFigure)

        # Add Canvas
        self.HorizontalLayout2.addWidget(self.ContinuousVelocityCanvas)

        # End

        self.ContinuousRight.addTab(self.ContinuousVelocity, "")
        self.ContinuousDisplacement = QtWidgets.QWidget()


        ## Displacement Framework
        self.ContinuousDisplacement.setObjectName("ContinuousDisplacement")
        self.ContinuousDisplacementFrame = QtWidgets.QFrame(self.ContinuousDisplacement)
        self.ContinuousDisplacementFrame.setGeometry(QtCore.QRect(10, 10, 771, 681))
        self.ContinuousDisplacementFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ContinuousDisplacementFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ContinuousDisplacementFrame.setObjectName("ContinuousDisplacementFrame")

        # Create horizontal layout
        self.HorizontalLayout1 = QtWidgets.QHBoxLayout(self.ContinuousDisplacementFrame)
        self.HorizontalLayout1.setObjectName("HorizontalLayout1")

        # Canvas
        self.ContinuousDisplacementFigure = plt.figure()
        self.ContinuousDisplacementCanvas = FigureCanvas(self.ContinuousDisplacementFigure)

        # Add Canvas
        self.HorizontalLayout1.addWidget(self.ContinuousDisplacementCanvas)

        # End


        self.ContinuousRight.addTab(self.ContinuousDisplacement, "")
        self.MainTabs.addTab(self.Continuous, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionCorellate = QtWidgets.QAction(MainWindow)
        self.actionCorellate.setObjectName("actionCorellate")
        self.actionContiniuous = QtWidgets.QAction(MainWindow)
        self.actionContiniuous.setObjectName("actionContiniuous")

        self.retranslateUi(MainWindow)
        self.MainTabs.setCurrentIndex(0)
        self.CorrelateRight.setCurrentIndex(2)
        self.ContinuousRight.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WQRM Controller v1.0"))
        self.Info1.setText(_translate("MainWindow", "Welcome to the WQRM Controller. Above this box there are tabs from these can select the mode you wish to use. The moves include:"))
        self.Info2.setText(_translate("MainWindow", "• Calibrate allows the device to zero itself using the magnetic reed switch."))
        self.Info3.setText(_translate("MainWindow", "• Correlate will plot the values obtained from the device against theoretical predicted values."))
        self.Info4.setText(_translate("MainWindow", "• Continuous will operate the device continuously while displaying the values from the model. "))
        self.Info5.setText(_translate("MainWindow", "When you are ready to get started, please click connect to Arduino and wait for the port number before selecting a mode."))
        self.Connect.setText(_translate("MainWindow", "Connect to Arduino"))
        self.StartStatus.setText(_translate("MainWindow", "Awaiting Connection"))
        self.Mark.setText(_translate("MainWindow", "Mark Davenport 2024"))
        self.Project.setText(_translate("MainWindow", "ES327 Individual Project"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.Start), _translate("MainWindow", "Start"))
        self.Info6.setText(_translate("MainWindow", "To zero the device select align below:"))
        self.Info7.setText(_translate("MainWindow", "Current Status:"))
        self.CalibrateStatus.setText(_translate("MainWindow", "Unconnected, Unaligned"))
        self.Align.setText(_translate("MainWindow", "Align"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.Calibrate), _translate("MainWindow", "Calibrate"))
        self.CorrelateRight.setTabText(self.CorrelateRight.indexOf(self.CorrelateAcceleration), _translate("MainWindow", "Acceleration"))
        self.CorrelateRight.setTabText(self.CorrelateRight.indexOf(self.CorrelateVelocity), _translate("MainWindow", "Velocity"))
        self.CorrelateRight.setTabText(self.CorrelateRight.indexOf(self.CorrelateDisplacement), _translate("MainWindow", "Displacement"))
        self.Info8.setText(_translate("MainWindow", "Corelate receives data from the mechanisms Arduino sensor and plots those values against the value obtained by the kinematic analysis of the system. It allows the comparison of the theoretical and predicted values."))
        self.Info9.setText(_translate("MainWindow", "To get started defining the angular acceleration, initial angular velocity, number of cycles and the crank length."))
        self.Info10.setText(_translate("MainWindow", "Once started the values will begin populating the plot on the right. Once completed you will be able to select the displacement, velocity, and acceleration tabs."))
        self.CRaa.setCurrentText(_translate("MainWindow", "Angular Acceleration"))
        self.CRaa.setItemText(0, _translate("MainWindow", "Angular Acceleration"))
        self.CRaa.setItemText(1, _translate("MainWindow", "0 ms^-2"))
        self.CRiav.setItemText(0, _translate("MainWindow", "Initial Angular Velocity"))
        self.CRiav.setItemText(1, _translate("MainWindow", "20 rpm"))
        self.CRiav.setItemText(2, _translate("MainWindow", "30 rpm"))
        self.CRiav.setItemText(3, _translate("MainWindow", "40 rpm"))
        self.CRiav.setItemText(4, _translate("MainWindow", "50 rpm"))
        self.CRiav.setItemText(5, _translate("MainWindow", "60 rpm"))
        self.CRnc.setItemText(0, _translate("MainWindow", "Number of Cycles"))
        self.CRnc.setItemText(1, _translate("MainWindow", "One"))
        self.CRnc.setItemText(2, _translate("MainWindow", "Two"))
        self.CRnc.setItemText(3, _translate("MainWindow", "Three"))
        self.CRcl.setItemText(0, _translate("MainWindow", "Crank Length"))
        self.CRcl.setItemText(1, _translate("MainWindow", "Extended"))
        self.CRcl.setItemText(2, _translate("MainWindow", "Shortened"))
        self.CorrelateStatus.setText(_translate("MainWindow", "Ready to Start"))
        self.CRStart.setText(_translate("MainWindow", "Start"))
        self.Info11.setText(_translate("MainWindow", "Key"))
        self.CRS1X.setText(_translate("MainWindow", "AS1X"))
        self.CRS1Y.setText(_translate("MainWindow", "AS1Y"))
        self.CRS2X.setText(_translate("MainWindow", "AS2X"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.Correlate), _translate("MainWindow", "Correlate"))
        self.Info12.setText(_translate("MainWindow", "Continuous will run the mechanism continuously, while it’s moving a scan line will move across the plot to show which point in the cycle the mechanism is at. The values plotted are the predicted values."))
        self.Info14.setText(_translate("MainWindow", "To get started defining the angular velocity and the crank length."))
        self.Info15.setText(_translate("MainWindow", "You can switch between the displacement, velocity, and acceleration tabs."))
        self.CNav.setItemText(0, _translate("MainWindow", "Angular Velocity"))
        self.CNav.setItemText(1, _translate("MainWindow", "20 rpm"))
        self.CNav.setItemText(2, _translate("MainWindow", "30 rpm"))
        self.CNav.setItemText(3, _translate("MainWindow", "40 rpm"))
        self.CNav.setItemText(4, _translate("MainWindow", "50 rpm"))
        self.CNav.setItemText(5, _translate("MainWindow", "60 rpm"))
        self.CNcl.setItemText(0, _translate("MainWindow", "Crank Length"))
        self.CNcl.setItemText(1, _translate("MainWindow", "Extended"))
        self.CNcl.setItemText(2, _translate("MainWindow", "Shortened"))
        self.ContinuousStatus.setText(_translate("MainWindow", "Ready to Start"))
        self.CNStart.setText(_translate("MainWindow", "Start"))
        self.Info18.setText(_translate("MainWindow", "Cycles Completed:"))
        self.CNcycles.setText(_translate("MainWindow", "6"))
        self.Info17.setText(_translate("MainWindow", "Key"))
        self.CNS1X.setText(_translate("MainWindow", "S1X"))
        self.CNS1Y.setText(_translate("MainWindow", "S1Y"))
        self.CNS2X.setText(_translate("MainWindow", "S2X"))
        self.ContinuousRight.setTabText(self.ContinuousRight.indexOf(self.ContinuousAcceleration), _translate("MainWindow", "Acceleration"))
        self.ContinuousRight.setTabText(self.ContinuousRight.indexOf(self.ContinuousVelocity), _translate("MainWindow", "Velocity"))
        self.ContinuousRight.setTabText(self.ContinuousRight.indexOf(self.ContinuousDisplacement), _translate("MainWindow", "Displacement"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.Continuous), _translate("MainWindow", "Continuous"))
        self.actionStart.setText(_translate("MainWindow", "Calibrate"))
        self.actionStart.setStatusTip(_translate("MainWindow", "Start here! Select the mode you would like."))
        self.actionCorellate.setText(_translate("MainWindow", "Corellate"))
        self.actionContiniuous.setText(_translate("MainWindow", "Continiuous"))

        self.Align.clicked.connect(self.CalibrateArm)
        self.Connect.clicked.connect(self.ConnectArduino)
        self.CRStart.clicked.connect(self.CorrelateOp)
        self.CNStart.clicked.connect(self.ContinuousOpA)

    def ConnectArduino(self):
        global port
        self.StartStatus.setText("Connecting...")
        ports = list(serial.tools.list_ports.comports())
        coned = ""
        for p in ports:
            coned += str(p)
        if coned.count("Arduino") == 2:
            self.StartStatus.setText("Multiple Arduinos Detected! Please disconnect Additional Arduino.")
        elif coned.count("Arduino") == 1:
            index = coned.find("Arduino")
            port = coned[index - 7:index]
            port = port[:-3]
            self.StartStatus.setText("Device found on port: " + str(port) + ". Please continue.")
            ser = serial.Serial(str(port), 9600, timeout=1)
            value_to_send = "PythonArduinoConnected"
            ser.write(value_to_send.encode())
            ser.close()
            ## Lubrication PopUp
            popup = QMessageBox()
            popup.setWindowTitle("Lubrication Notice")
            popup.setText("Please note that if you haven’t already, please lubricate the conrod cut out which are populated with metal fixtures. Lubricate the while length of the cut outs on both sides. Use silicone or petroleum-based lubricant previously Vaseline applied with a cotton bud was used. If lubrication is not applied or an insignificant amount is applied the device will be seen to 'jitter'.")
            self.CalibrateStatus.setText("Connected, Unaligned")

            #image_label = QLabel()
            #image_path = r"C:\Users\Mark Davenport\OneDrive - University of Warwick\1. University Work\Year 3\ES327 Individual Project\Coding\GUI\GUI2\Lubrication.png"
            #image_pixmap = QPixmap(image_path)
            #image_label.setPixmap(image_pixmap)
            #image_label.setAlignment(Qt.AlignCenter)

            #layout = QVBoxLayout()
            #layout.addWidget(image_label)
            #popup.setLayout(layout)

            popup.exec_()

        elif coned.count("Arduino") == 0:
            self.StartStatus.setText("WQRM Not Detected. Please Check Connection.")
        self.Connect.setText("Recheck Connection")

    def CalibrateArm(self):
        global port
        print("Calibrate")
        ser = serial.Serial(str(port), 9600, timeout=1)
        value_to_send = "P"
        time.sleep(1)
        ser.write(value_to_send.encode())
        self.CalibrateStatus.setText("Connected, Aligned")

    def CorrelateOp(self):
        global Key
        global ConRunning
        global port

        Key = ["O", "X", "X", "X", "X"]
        step1 = False
        step2 = False
        step3 = False
        step4 = False

        map1 = {0: "", 1: "A"}
        current_index = self.CRaa.currentIndex()
        if current_index == 0:
            self.CorrelateStatus.setText("Please define the angular acceleration.")
        else:
         Key[1] = map1.get(current_index, "")
         step1 = True

        map2 = {0: "", 1: "20", 2: "30", 3: "40", 4: "50", 5: "60"}
        current_index = self.CRiav.currentIndex()
        if current_index == 0:
            self.CorrelateStatus.setText("Please define the initial angular velocity.")
        else:
         Key[2] = map2.get(current_index, "")
         step2 = True

        map3 = {0: "", 1: "1", 2: "2", 3: "3"}
        current_index = self.CRnc.currentIndex()
        if current_index == 0:
            self.CorrelateStatus.setText("Please define the nymber of cycles.")
        else:
         Key[3] = map3.get(current_index, "")
         step3 = True

        map4 = {0: "", 1: "E", 2: "S"}
        current_index = self.CRcl.currentIndex()
        if current_index == 0:
            self.CorrelateStatus.setText("Please define the crank length.")
        else:
         Key[4] = map4.get(current_index, "")
         step4 = True
        
        if step1 and step2 and step3 and step4:
            self.CorrelateStatus.setText("Spinning... Code: " + ''.join(Key))
            ser = serial.Serial(str(port), 9600, timeout=1)
            value_to_send = ''.join(Key)
            time.sleep(1)
            ser.write(value_to_send.encode())
            self.CorrelateOpB()
            

    def CorrelateOpB(self):
        global Key
        global port

        theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X = DataGenerator(Key)
        
        ## Displacement Animation
        self.CorrelateDisplacementFigure.clear()
        self.CorrelateDisplacementCanvas.draw()
        plt4 = self.CorrelateDisplacementFigure.add_subplot(111)
        plt4.set_xlim(0, int(Key[3]) * 360)
        plt4.set_ylim(-0.2, 0.2)
        x = np.arange(0, (int(Key[3]) * 360) + 1, 45)
        y = np.array([-0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15, 0.2])
        plt4.set_xticks(x)
        plt4.set_yticks(y)
        plt4.grid(axis='x')
        plt4.grid(axis='y')

        line_xs1x, = plt4.plot([], [], lw=2, color='#A9BF04')
        line_xs1y, = plt4.plot([], [], lw=2, color='#F24405')
        line_xs2x, = plt4.plot([], [], lw=2, color='#0096FF')

        def init():
            line_xs1x.set_data([], [])
            line_xs1y.set_data([], [])
            line_xs2x.set_data([], [])
            return line_xs1x, line_xs1y, line_xs2x

        def animate(i, theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X):
            x = theta[:i]
            y_xs1x = XS1X[:i]
            y_xs1y = XS1Y[:i]
            y_xs2x = XS2X[:i]
            line_xs1x.set_data(x, y_xs1x)
            line_xs1y.set_data(x, y_xs1y)
            line_xs2x.set_data(x, y_xs2x)
            return line_xs1x, line_xs1y, line_xs2x
        
        frames = len(theta)
        duration2 = (60/(int(Key[2])))*(int(Key[3]))*1000
        interval2 = duration2 / frames
        print(interval2)
        self.anim = FuncAnimation(self.CorrelateDisplacementFigure, animate, fargs=(theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X), init_func=init, frames=frames, interval=interval2, blit=True, repeat=False)
        self.CorrelateDisplacementFigure.canvas.draw()

        ## Velocity Animation
        self.CorrelateVelocityFigure.clear()
        self.CorrelateVelocityCanvas.draw()        
        plt5 = self.CorrelateVelocityFigure.add_subplot(111)
        plt5.set_xlim(0, int(Key[3]) * 360)
        plt5.set_ylim(-2, 2)
        x = np.arange(0, (int(Key[3]) * 360) + 1, 45)
        y = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
        plt5.set_xticks(x)
        plt5.set_yticks(y)
        plt5.grid(axis='x')
        plt5.grid(axis='y')

        line_vs1x, = plt5.plot([], [], lw=2, color='#A9BF04')
        line_vs1y, = plt5.plot([], [], lw=2, color='#F24405')
        line_vs2x, = plt5.plot([], [], lw=2, color='#0096FF')

        def init():
            line_vs1x.set_data([], [])
            line_vs1y.set_data([], [])
            line_vs2x.set_data([], [])
            return line_vs1x, line_vs1y, line_vs2x

        def animate(i, theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X):
            x = theta[:i]
            y_vs1x = VS1X[:i]
            y_vs1y = VS1Y[:i]
            y_vs2x = VS2X[:i]
            line_vs1x.set_data(x, y_vs1x)
            line_vs1y.set_data(x, y_vs1y)
            line_vs2x.set_data(x, y_vs2x)
            return line_vs1x, line_vs1y, line_vs2x
        
        frames = len(theta)
        duration = (60/(int(Key[2])))*(int(Key[3]))*1000
        interval = duration / frames
        self.anim2 = FuncAnimation(self.CorrelateVelocityFigure, animate, fargs=(theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X), init_func=init, frames=frames, interval=interval, blit=True, repeat=False)
        self.CorrelateVelocityFigure.canvas.draw()

        self.CNS1X.setStyleSheet("color: {};".format("#A9BF04"))
        self.CNS1Y.setStyleSheet("color: {};".format("#F24405"))
        self.CNS2X.setStyleSheet("color: {};".format("#0096FF"))

        ## Acceleration Animation
        self.CorrelateAccelerationFigure.clear()
        self.CorrelateAccelerationCanvas.draw()           
        plt6 = self.CorrelateAccelerationFigure.add_subplot(111)
        plt6.set_xlim(0, int(Key[3]) * 360)
        plt6.set_ylim(-6, 6)
        x = np.arange(0, (int(Key[3]) * 360) + 1, 45)
        y = np.array([-8, -6, -4, -2, 0, 2, 4, 6, 8])
        plt6.set_xticks(x)
        plt6.set_yticks(y)
        plt6.grid(axis='x')
        plt6.grid(axis='y')

        line_as1x, = plt6.plot([], [], lw=2, color='#A9BF04')
        line_as1y, = plt6.plot([], [], lw=2, color='#F24405')
        line_as2x, = plt6.plot([], [], lw=2, color='#0096FF')

        def init():
            line_as1x.set_data([], [])
            line_as1y.set_data([], [])
            line_as2x.set_data([], [])
            return line_as1x, line_as1y, line_as2x

        def animate(i, theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X):
            x = theta[:i]
            y_as1x = AS1X[:i]
            y_as1y = AS1Y[:i]
            y_as2x = AS2X[:i]
            line_as1x.set_data(x, y_as1x)
            line_as1y.set_data(x, y_as1y)
            line_as2x.set_data(x, y_as2x)
            return line_as1x, line_as1y, line_as2x
        
        frames = len(theta)
        duration3 = ((60000*int(Key[3]))/(int(Key[2])))
        interval3 = duration3 / frames
        self.anim2 = FuncAnimation(self.CorrelateAccelerationFigure, animate, fargs=(theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X), frames=frames, interval=interval3, blit=True, repeat=False)
        self.CorrelateAccelerationFigure.canvas.draw()

  

    def ContinuousOpA(self):
        global Key
        global ConRunning
        global port

        ## Logic for starting or stopping
                
        if self.CNStart.text() == "Start":
            Key = ["S", "A", "X", "2", "X"]
            step2 = False
            step4 = False

            map2 = {0: "", 1: "20", 2: "30", 3: "40", 4: "50", 5: "60"}
            current_index = self.CNav.currentIndex()
            if current_index == 0:
                self.ContinuousStatus.setText("Please define the angular velocity")
            else:
                Key[2] = map2.get(current_index, "")
                step2 = True

            map4 = {0: "", 1: "E", 2: "S"}
            current_index = self.CNcl.currentIndex()
            if current_index == 0:
                self.ContinuousStatus.setText("Please define the crank length")
            else:
                Key[4] = map4.get(current_index, "")
                step4 = True
            
            if step2 and step4:
                self.CNStart.setText("Stop")
                self.ContinuousOpB()
        elif self.CNStart.text() == "Stop":
           print("CNStart - Stop")
           self.anim.event_source.stop()
           self.anim2.event_source.stop()
           self.ContinuousDisplacementFigure.clear()
           ConRunning = "F"
           self.CNStart.setText("Start")
           print("End" + ConRunning + ''.join(Key))
           ser = serial.Serial(str(port), 9600, timeout=1)
           value_to_send = "Q"
           ser.write(value_to_send.encode()) 

       
    def ContinuousOpB(self):
        global port
        global Key
        global ConRunning  
        
        ser = serial.Serial(str(port), 9600, timeout=1)
        value_to_send = ''.join(Key)
        time.sleep(1)
        ser.write(value_to_send.encode())        
        print(value_to_send)
        self.ContinuousDisplacementFigure.clear()
        self.ContinuousVelocityFigure.clear()
        self.ContinuousStatus.setText("Spinning... Code: " + ''.join(Key))
        (theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X) = DataGenerator(Key)

        ## Displacement Animation
        self.ContinuousDisplacementFigure.clear()
        self.ContinuousDisplacementCanvas.draw()        
        plt = self.ContinuousDisplacementFigure.add_subplot(111)
        plt.set_xlim(0, 720)
        plt.set_ylim(-0.2, 0.2)
        x = np.array([0, 45, 90, 135, 180, 225, 270, 315, 360, 405, 450, 495, 540, 585, 630, 675, 720])
        y = np.array([-0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15, 0.2])
        plt.set_xticks(x)
        plt.set_yticks(y)
        plt.grid(axis='x')
        plt.grid(axis='y')

        line_xs1x, = plt.plot([], [], lw=2, color='#A9BF04')
        line_xs1y, = plt.plot([], [], lw=2, color='#F24405')
        line_xs2x, = plt.plot([], [], lw=2, color='#0096FF')

        def init():
            line_xs1x.set_data([], [])
            line_xs1y.set_data([], [])
            line_xs2x.set_data([], [])
            return line_xs1x, line_xs1y, line_xs2x

        def animate(i, theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X):
            x = theta[:i]
            y_xs1x = XS1X[:i]
            y_xs1y = XS1Y[:i]
            y_xs2x = XS2X[:i]
            line_xs1x.set_data(x, y_xs1x)
            line_xs1y.set_data(x, y_xs1y)
            line_xs2x.set_data(x, y_xs2x)
            return line_xs1x, line_xs1y, line_xs2x
        
        frames = len(theta)
        duration4 = ((60000*int(Key[3]))/(int(Key[2])))
        interval4 = duration4 / frames
        self.anim = FuncAnimation(self.ContinuousDisplacementFigure, animate, fargs=(theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X), init_func=init,
                            frames=frames, interval=interval4, blit=True)
        self.ContinuousDisplacementFigure.canvas.draw()

        ## Velocity Animation
        self.ContinuousVelocityFigure.clear()
        self.ContinuousVelocityCanvas.draw()          
        plt2 = self.ContinuousVelocityFigure.add_subplot(111)
        plt2.set_xlim(0, 720)
        plt2.set_ylim(-2, 2)
        x = np.array([0, 45, 90, 135, 180, 225, 270, 315, 360, 405, 450, 495, 540, 585, 630, 675, 720])
        y = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
        plt2.set_xticks(x)
        plt2.set_yticks(y)
        plt2.grid(axis='x')
        plt2.grid(axis='y')

        line_vs1x, = plt2.plot([], [], lw=2, color='#A9BF04')
        line_vs1y, = plt2.plot([], [], lw=2, color='#F24405')
        line_vs2x, = plt2.plot([], [], lw=2, color='#0096FF')

        def init():
            line_vs1x.set_data([], [])
            line_vs1y.set_data([], [])
            line_vs2x.set_data([], [])
            return line_vs1x, line_vs1y, line_vs2x

        def animate(i, theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X):
            x = theta[:i]
            y_vs1x = VS1X[:i]
            y_vs1y = VS1Y[:i]
            y_vs2x = VS2X[:i]
            line_vs1x.set_data(x, y_vs1x)
            line_vs1y.set_data(x, y_vs1y)
            line_vs2x.set_data(x, y_vs2x)
            return line_vs1x, line_vs1y, line_vs2x
        
        frames = len(theta)
        duration = 120000*(1/(int(Key[2])))
        interval = duration / frames
        self.anim2 = FuncAnimation(self.ContinuousVelocityFigure, animate, fargs=(theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X), init_func=init,
                            frames=frames, interval=interval, blit=True)
        self.ContinuousVelocityFigure.canvas.draw()


        self.CNS1X.setStyleSheet("color: {};".format("#A9BF04"))
        self.CNS1Y.setStyleSheet("color: {};".format("#F24405"))
        self.CNS2X.setStyleSheet("color: {};".format("#0096FF"))


        ## Acceleration Animation
        self.ContinuousAccelerationFigure.clear()
        self.ContinuousAccelerationCanvas.draw()        
        plt3 = self.ContinuousAccelerationFigure.add_subplot(111)
        plt3.set_xlim(0, 720)
        plt3.set_ylim(-6, 6)
        x = np.array([0, 45, 90, 135, 180, 225, 270, 315, 360, 405, 450, 495, 540, 585, 630, 675, 720])
        y = np.array([-8, -6, -4, -2, 0, 2, 4, 6, 8])
        plt3.set_xticks(x)
        plt3.set_yticks(y)
        plt3.grid(axis='x')
        plt3.grid(axis='y')

        line_as1x, = plt3.plot([], [], lw=2, color='#A9BF04')
        line_as1y, = plt3.plot([], [], lw=2, color='#F24405')
        line_as2x, = plt3.plot([], [], lw=2, color='#0096FF')

        def init():
            line_as1x.set_data([], [])
            line_as1y.set_data([], [])
            line_as2x.set_data([], [])
            return line_as1x, line_as1y, line_as2x

        def animate(i, theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X):
            x = theta[:i]
            y_as1x = AS1X[:i]
            y_as1y = AS1Y[:i]
            y_as2x = AS2X[:i]
            line_as1x.set_data(x, y_as1x)
            line_as1y.set_data(x, y_as1y)
            line_as2x.set_data(x, y_as2x)
            return line_as1x, line_as1y, line_as2x
        
        frames = len(theta)
        duration = 120000*(1/(int(Key[2])))
        interval = duration / frames
        self.anim2 = FuncAnimation(self.ContinuousAccelerationFigure, animate, fargs=(theta, XS1X, XS1Y, XS2X, VS1X, VS1Y, VS2X, AS1X, AS1Y, AS2X), init_func=init,
                            frames=frames, interval=interval, blit=True)
        self.ContinuousAccelerationFigure.canvas.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
