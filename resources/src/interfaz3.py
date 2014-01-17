# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz3.ui'
#
# Created: Thu Jan 16 14:58:47 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from Convolution import ImageConvolution
import tempfile
import os
import shutil
import source_qr


class Ui_MainWindow(object):
    
    __originalImage=""
    __newImage=""
    __imageExtension=""
    __temporaltemporalDir="PyConvolution"
    __list=[]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(909, 562)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.widget_2 = QtGui.QWidget(self.frame_2)
        self.widget_2.setGeometry(QtCore.QRect(10, 20, 221, 191))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.doubleSpinBox_1 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_1.setObjectName("doubleSpinBox_1")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_1)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_2)
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_3)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_4)
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_5)
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.widget_3)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox_6)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtGui.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(self.widget_4)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_7)
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(self.widget_4)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_8)
        self.doubleSpinBox_9 = QtGui.QDoubleSpinBox(self.widget_4)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_9)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_5 = QtGui.QWidget(self.frame_2)
        self.widget_5.setGeometry(QtCore.QRect(10, 220, 221, 45))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_reset = QtGui.QPushButton(self.widget_5)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/source_img/img/icon/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_reset.setIcon(icon)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.verticalLayout_4.addWidget(self.pushButton_reset)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(500, 100))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_6 = QtGui.QWidget(self.frame_3)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea = QtGui.QScrollArea(self.widget_6)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 275, 357))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_original = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_original.setText("")
        self.label_original.setPixmap(QtGui.QPixmap("img.jpg"))
        self.label_original.setScaledContents(True)
        self.label_original.setWordWrap(False)
        self.label_original.setObjectName("label_original")
        self.verticalLayout_2.addWidget(self.label_original)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_openImg = QtGui.QPushButton(self.widget_6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/source_img/img/icon/Open_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_openImg.setIcon(icon1)
        self.pushButton_openImg.setObjectName("pushButton_openImg")
        self.horizontalLayout_5.addWidget(self.pushButton_openImg)
        self.pushButton_saveImgOriginal = QtGui.QPushButton(self.widget_6)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/source_img/img/icon/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_saveImgOriginal.setIcon(icon2)
        self.pushButton_saveImgOriginal.setObjectName("pushButton_saveImgOriginal")
        self.horizontalLayout_5.addWidget(self.pushButton_saveImgOriginal)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addWidget(self.widget_6)
        self.widget_7 = QtGui.QWidget(self.frame_3)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_2 = QtGui.QScrollArea(self.widget_7)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 274, 359))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_new = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.label_new.setText("")
        self.label_new.setPixmap(QtGui.QPixmap("img.jpg"))
        self.label_new.setScaledContents(True)
        self.label_new.setWordWrap(False)
        self.label_new.setObjectName("label_new")
        self.horizontalLayout.addWidget(self.label_new)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.addWidget(self.scrollArea_2)
        self.pushButton_saveImageNew = QtGui.QPushButton(self.widget_7)
        self.pushButton_saveImageNew.setIcon(icon2)
        self.pushButton_saveImageNew.setObjectName("pushButton_saveImageNew")
        self.verticalLayout_6.addWidget(self.pushButton_saveImageNew)
        self.horizontalLayout_6.addWidget(self.widget_7)
        self.gridLayout.addWidget(self.frame_3, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 909, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionAbout_project = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/source_img/img/icon/python.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_project.setIcon(icon3)
        self.actionAbout_project.setObjectName("actionAbout_project")
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAbout_project)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAbout_Qt)

        self.retranslateUi(MainWindow)
        
        self.doubleSpinBox_1.setMinimum(-5)
        self.doubleSpinBox_1.setMaximum(5)
        self.doubleSpinBox_2.setMinimum(-5)
        self.doubleSpinBox_2.setMaximum(5)
        self.doubleSpinBox_3.setMinimum(-5)
        self.doubleSpinBox_3.setMaximum(5)
        self.doubleSpinBox_4.setMinimum(-5)
        self.doubleSpinBox_4.setMaximum(5)
        self.doubleSpinBox_5.setMinimum(-5)
        self.doubleSpinBox_5.setMaximum(5)
        self.doubleSpinBox_6.setMinimum(-5)
        self.doubleSpinBox_6.setMaximum(5)
        self.doubleSpinBox_7.setMinimum(-5)
        self.doubleSpinBox_7.setMaximum(5)
        self.doubleSpinBox_8.setMinimum(-5)
        self.doubleSpinBox_8.setMaximum(5)
        self.doubleSpinBox_9.setMinimum(-5)
        self.doubleSpinBox_9.setMaximum(5)
        
        self.__MainWindow=MainWindow
        self.connectionSlots()
        self.__MainWindow.setWindowIcon(QtGui.QIcon(":/source_img/img/icon/python.png"));
        
        
        
        self.__temporaltemporalDir=tempfile.gettempdir()+os.sep+"PyComvolution"
        if not os.path.exists(self.__temporaltemporalDir):
            os.makedirs(self.__temporaltemporalDir)
        
        
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("PyConvolution", "PyConvolution", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_reset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_openImg.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_saveImgOriginal.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_saveImageNew.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_project.setText(QtGui.QApplication.translate("MainWindow", "About?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_project.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>About this Project</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("MainWindow", "About Qt?", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

    def connectionSlots(self):
        QtCore.QObject.connect(self.actionAbout_Qt, QtCore.SIGNAL("triggered()"), self.onClickAboutQt)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), self.__MainWindow.close)  
        QtCore.QObject.connect(self.actionAbout_project, QtCore.SIGNAL("triggered()"), self.onClickAboutProject)        
        QtCore.QMetaObject.connectSlotsByName(self.__MainWindow)
        self.pushButton_reset.clicked.connect(self.onResetPressed)
        self.pushButton_openImg.clicked.connect(self.setOpenFileName)
        self.pushButton_saveImageNew.clicked.connect(self.onSaveNewImagePressed)
        self.pushButton_saveImgOriginal.clicked.connect(self.onSaveOriginalImagePressed)
        self.doubleSpinBox_1.valueChanged.connect(self.OnCahngeValueSpinBox)
        self.doubleSpinBox_2.valueChanged.connect(self.OnCahngeValueSpinBox)
        self.doubleSpinBox_3.valueChanged.connect(self.OnCahngeValueSpinBox)
        self.doubleSpinBox_4.valueChanged.connect(self.OnCahngeValueSpinBox)
        self.doubleSpinBox_5.valueChanged.connect(self.OnCahngeValueSpinBox)
        self.doubleSpinBox_6.valueChanged.connect(self.OnCahngeValueSpinBox)
        self.doubleSpinBox_7.valueChanged.connect(self.OnCahngeValueSpinBox)
        self.doubleSpinBox_8.valueChanged.connect(self.OnCahngeValueSpinBox)
        self.doubleSpinBox_9.valueChanged.connect(self.OnCahngeValueSpinBox)

   
    def onClickAboutQt(self):
        QtGui.QMessageBox.aboutQt(self.__MainWindow)
        
    def onClickAboutProject(self):        
        QtGui.QMessageBox.about(self.__MainWindow,"About this Aplication",u"This application was created by:\n"+
        u"    Camilo Ramírez @camilortte on Twitter.\n"+
        "    Visiti my Gitpage: https://github.com/camilortte\n"+
        "\nTechnology: Python + Pyside + Numpy + opencv and Qt"+
        "\n This app is avaliable under License Gplv3")
   
    def onSaveNewImagePressed(self):  
        self.saveImage(self.__newImage)
        
    
    def onSaveOriginalImagePressed(self):  
        self.saveImage(self.__originalImage)        
    
    def saveImage(self,image):        
        if(self.__originalImage!=""):
            dst = QtGui.QFileDialog.getSaveFileName(self.__MainWindow,"Save as",
                                                     "myImage"+self.__imageExtension,
                                                     "Image Files (*.png *.jpg *.bmp)")[0]
            if dst:
                shutil.copyfile(image, dst)
                self.statusbar.showMessage("Imagen saved",3000)
   
    def OnCahngeValueSpinBox(self, value):
        self.__list=[]
        self.__list.append(self.doubleSpinBox_1.value())
        self.__list.append(self.doubleSpinBox_2.value())
        self.__list.append(self.doubleSpinBox_3.value())
        self.__list.append(self.doubleSpinBox_4.value())
        self.__list.append(self.doubleSpinBox_5.value())
        self.__list.append(self.doubleSpinBox_6.value())
        self.__list.append(self.doubleSpinBox_7.value())
        self.__list.append(self.doubleSpinBox_8.value())
        self.__list.append(self.doubleSpinBox_9.value())
        
        self.aplicateConvolve()
        

    def aplicateConvolve(self):
        import numpy as np
        array=np.asarray(self.__list)
        imageConvolution=    ImageConvolution(self.__originalImage)
        self.__newImage = self.__temporaltemporalDir+os.sep+"im1"+self.__imageExtension
        imageConvolution.saveImageAs(self.__newImage,array)
        self.label_new.setPixmap(QtGui.QPixmap(self.__newImage))
        self.statusbar.showMessage("Convolve aplicated",3000)
    
    def onResetPressed(self):
        self.doubleSpinBox_1.setValue(0)
        self.doubleSpinBox_2.setValue(0)
        self.doubleSpinBox_3.setValue(0)
        self.doubleSpinBox_4.setValue(0)
        self.doubleSpinBox_5.setValue(0)
        self.doubleSpinBox_6.setValue(0)
        self.doubleSpinBox_7.setValue(0)
        self.doubleSpinBox_8.setValue(0)
        self.doubleSpinBox_9.setValue(0)
        self.statusbar.showMessage("Filteres Resets",3000)
        
    def setOpenFileName(self):    
        correct=False
        options = QtGui.QFileDialog.Options()
        fileName = QtGui.QFileDialog.getOpenFileName(self.__MainWindow,caption="Open Imagen",
                                                     selectedFilter="Image Files (*.png *.jpg *.bmp)", 
                                                     options=options)[0]
        filters=['.png','.jpg','.bmp']
        if fileName:
            for filter in filters:
                if fileName.rfind(filter)!=-1:
                    self.__imageExtension=filter                    
                    self.__originalImage=fileName
                    self.label_original.setPixmap(QtGui.QPixmap(fileName))
                    self.aplicateConvolve()
                    self.statusbar.showMessage("Imagen load",3000)
                    correct=True
        
            if not correct:
                QtGui.QMessageBox.warning(self.__MainWindow, "Error Image",
                                   "You should import a valid image",                                  
                                   QtGui.QMessageBox.Accepted)
            

