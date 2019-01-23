# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from calibratie import CalibratieTrackers
from PongGame import Pong_demo

# global variables

PLAYERS = 1
THEME = 2
SPEED = 15
POINTS = 3
TIME = 120



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Bit9x9")
        MainWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.stackedWidget.setMinimumSize(QtCore.QSize(1920, 1080))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Bit9x9")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background-color: #000000;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.StartPage = QtWidgets.QWidget()
        self.StartPage.setObjectName("StartPage")
        self.LblTitle = QtWidgets.QLabel(self.StartPage)
        self.LblTitle.setGeometry(QtCore.QRect(650, 180, 591, 171))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.LblTitle.setFont(font)
        self.LblTitle.setStyleSheet("#LblTitle{\n"
"color: #FFFFFF;\n"
"font-size: 190px;\n"
"text-align: center;\n"
"border: 1px solid white;\n"
"\n"
"}")
        self.LblTitle.setObjectName("LblTitle")
        self.BtnStart = QtWidgets.QPushButton(self.StartPage)
        self.BtnStart.setGeometry(QtCore.QRect(550, 700, 821, 101))
        font = QtGui.QFont()
        font.setFamily("Bit9x9")
        font.setPointSize(1)
        self.BtnStart.setFont(font)
        self.BtnStart.setStyleSheet("#BtnStart {\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: 1px solid white;\n"
"font-size: 90px;\n"
"font-family: \'Bit9x9\';\n"
"}\n"
"#BtnStart:pressed\n"
"{\n"
"border: 1px solid black;\n"
"background-color: #FFFFFF;\n"
"color: #000000;\n"
"font-size: 90px;\n"
"}")
        self.BtnStart.setObjectName("BtnStart")
        self.BtnCalibrate = QtWidgets.QPushButton(self.StartPage)
        self.BtnCalibrate.setGeometry(QtCore.QRect(1590, 940, 261, 32))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.BtnCalibrate.setFont(font)
        self.BtnCalibrate.setStyleSheet("#BtnCalibrate{\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: 1px solid white;\n"
"font-size: 24px;\n"
"}\n"
"#BtnCalibrate:pressed\n"
"{\n"
"border: 1px solid black;\n"
"background-color: #FFFFFF;\n"
"color: #000000\n"
"}")
        self.BtnCalibrate.setObjectName("BtnCalibrate")
        self.stackedWidget.addWidget(self.StartPage)
        self.SettingsPage = QtWidgets.QWidget()
        self.SettingsPage.setObjectName("SettingsPage")
        self.Btn2p = QtWidgets.QPushButton(self.SettingsPage)
        self.Btn2p.setGeometry(QtCore.QRect(510, 530, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Bit9x9")
        font.setPointSize(1)
        self.Btn2p.setFont(font)
        self.Btn2p.setStyleSheet("#Btn2p {\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: 1px solid white;\n"
"font-size: 50px;\n"
"font-family: \'Bit9x9\';\n"
"}\n"
"#Btn2p:pressed\n"
"{\n"
"border: 1px solid black;\n"
"background-color: #FFFFFF;\n"
"color: #000000;\n"
"font-size: 50px;\n"
"font-family: \'Bit9x9\';\n"
"}")
        self.Btn2p.setObjectName("Btn2p")
        self.BtnRetro = QtWidgets.QPushButton(self.SettingsPage)
        self.BtnRetro.setIcon(QtGui.QIcon('assets/icons/ping-pong.png'))
        self.BtnRetro.setIconSize(QtCore.QSize(114,101))
        self.BtnRetro.setGeometry(QtCore.QRect(1120, 530, 114, 101))
        self.BtnRetro.setStyleSheet("#BtnRetro {\n"
"background-color: transparent;\n"
"border-image: url(:ping-pong.png);\n"
"background: none;\n"
"border: 1px solid white;\n"
"background-repeat: none;\n"
"}\n"
"#BtnRetro:pressed\n"
"{\n"
"   border-image: url(:ping-pongblack.png);\n"
"border: 1px solid white;\n"
"background-color: #FFFFFF\n"
"}")
        self.BtnRetro.setText("")
        self.BtnRetro.setObjectName("BtnRetro")
        self.BtnFortNite = QtWidgets.QPushButton(self.SettingsPage)
        self.BtnFortNite.setIcon(QtGui.QIcon('assets/icons/fortnite-logo.png'))
        self.BtnFortNite.setIconSize(QtCore.QSize(114,101))
        self.BtnFortNite.setGeometry(QtCore.QRect(1400, 530, 114, 101))
        self.BtnFortNite.setStyleSheet("#BtnFortNite {\n"
"background-color: transparent;\n"
"border-image: url(:fortnite-logo.png);\n"
"background: none;\n"
"border: 1px solid white;\n"
"background-repeat: none;\n"
"}\n"
"#BtnFortNite:pressed\n"
"{\n"
"   border-image: url(:fortnite-logo-512.png);\n"
"border: 1px solid white;\n"
"background-color: #FFFFFF\n"
"}")
        self.BtnFortNite.setText("")
        self.BtnFortNite.setObjectName("BtnFortNite")
        self.BtnCastle = QtWidgets.QPushButton(self.SettingsPage)
        self.BtnCastle.setIcon(QtGui.QIcon('assets/icons/snowman.png'))
        self.BtnCastle.setIconSize(QtCore.QSize(114,101))
        self.BtnCastle.setGeometry(QtCore.QRect(1680, 530, 114, 101))
        self.BtnCastle.setStyleSheet("#BtnCastle {\n"
"background-color: transparent;\n"
"border-image: url(:snowman.png);\n"
"background: none;\n"
"border: 1px solid white;\n"
"background-repeat: none;\n"
"}\n"
"#BtnCastle:pressed\n"
"{\n"
"   border-image: url(:assets/icons/snowmanblack.png);\n"
"border: 1px solid white;\n"
"background-color: #FFFFFF\n"
"}")
        self.BtnCastle.setText("")
        self.BtnCastle.setObjectName("BtnCastle")
        self.BtnStart_2 = QtWidgets.QPushButton(self.SettingsPage)
        self.BtnStart_2.setGeometry(QtCore.QRect(1530, 900, 361, 91))
        self.BtnStart_2.setStyleSheet("#BtnStart_2 {\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: 1px solid white;\n"
"font-size: 90px;\n"
"font-family: \'Bit9x9\';\n"
"}\n"
"#BtnStart_2:pressed\n"
"{\n"
"border: 1px solid black;\n"
"background-color: #FFFFFF;\n"
"color: #000000;\n"
"font-size: 90px;\n"
"}")
        self.BtnStart_2.setObjectName("BtnStart_2")
        self.BtnAdvanced = QtWidgets.QPushButton(self.SettingsPage)
        self.BtnAdvanced.setGeometry(QtCore.QRect(1510, 30, 381, 61))
        self.BtnAdvanced.setStyleSheet("#BtnAdvanced {\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: 1px solid white;\n"
"font-size: 65px;\n"
"font-family: \'Bit9x9\';\n"
"}\n"
"#BtnAdvanced:pressed\n"
"{\n"
"border: 1px solid black;\n"
"background-color: #FFFFFF;\n"
"color: #000000;\n"
"font-size: 65px;\n"
"}")
        self.BtnAdvanced.setObjectName("BtnAdvanced")
        self.BtnSettings = QtWidgets.QPushButton(self.SettingsPage)
        self.BtnSettings.setGeometry(QtCore.QRect(30, 30, 551, 61))
        self.BtnSettings.setStyleSheet("#BtnSettings {\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: 1px solid white;\n"
"font-size: 65px;\n"
"font-family: \'Bit9x9\';\n"
"}\n"
"#BtnSettings:pressed\n"
"{\n"
"border: 1px solid black;\n"
"background-color: #FFFFFF;\n"
"color: #000000;\n"
"font-size: 65px;\n"
"}")
        self.BtnSettings.setObjectName("BtnSettings")
        self.BtnNmbrPlayers = QtWidgets.QPushButton(self.SettingsPage)
        self.BtnNmbrPlayers.setGeometry(QtCore.QRect(120, 390, 691, 91))
        self.BtnNmbrPlayers.setStyleSheet("#BtnNmbrPlayers {\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border-bottom: 1px solid white;\n"
"\n"
"font-size: 65px;\n"
"font-family: \'Bit9x9\';\n"
"}\n"
"")
        self.BtnNmbrPlayers.setObjectName("BtnNmbrPlayers")
        self.Btn1p_2 = QtWidgets.QPushButton(self.SettingsPage)
        self.Btn1p_2.setGeometry(QtCore.QRect(130, 530, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Bit9x9")
        font.setPointSize(1)
        self.Btn1p_2.setFont(font)
        self.Btn1p_2.setStyleSheet("#Btn1p_2 {\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: 1px solid white;\n"
"font-size: 50px;\n"
"font-family: \'Bit9x9\';\n"
"}\n"
"#Btn1p_2:pressed\n"
"{\n"
"border: 1px solid black;\n"
"background-color: #FFFFFF;\n"
"color: #000000;\n"
"font-size: 50px;\n"
"font-family: \'Bit9x9\';\n"
"}")
        self.Btn1p_2.setObjectName("Btn1p_2")
        self.BtnChooseTheme = QtWidgets.QPushButton(self.SettingsPage)
        self.BtnChooseTheme.setGeometry(QtCore.QRect(1110, 390, 691, 91))
        self.BtnChooseTheme.setStyleSheet("#BtnChooseTheme {\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"\n"
"font-size: 70px;\n"
"font-family: \'Bit9x9\';\n"
"border-bottom: 1px solid white\n"
"}\n"
"")
        self.BtnChooseTheme.setObjectName("BtnChooseTheme")
        self.stackedWidget.addWidget(self.SettingsPage)
        self.AdvancedPage = QtWidgets.QWidget()
        self.AdvancedPage.setObjectName("AdvancedPage")
        self.BtnSettings_2 = QtWidgets.QPushButton(self.AdvancedPage)
        self.BtnSettings_2.setGeometry(QtCore.QRect(30, 30, 551, 61))
        self.BtnSettings_2.setStyleSheet("#BtnSettings_2 {\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: 1px solid white;\n"
"font-size: 65px;\n"
"font-family: \'Bit9x9\';\n"
"}\n"
"#BtnSettings_2s:pressed\n"
"{\n"
"border: 1px solid black;\n"
"background-color: #FFFFFF;\n"
"color: #000000;\n"
"font-size: 65px;\n"
"}")
        self.BtnSettings_2.setObjectName("BtnSettings_2")
        self.BtnAdvanced_2 = QtWidgets.QPushButton(self.AdvancedPage)
        self.BtnAdvanced_2.setGeometry(QtCore.QRect(1510, 30, 381, 61))
        self.BtnAdvanced_2.setStyleSheet("#BtnAdvanced_2 {\n"
"color: #FFFFFF;\n"
"background-color: #000000;\n"
"border: 1px solid white;\n"
"font-size: 65px;\n"
"font-family: \'Bit9x9\';\n"
"}\n"
"#BtnAdvanced_2:pressed\n"
"{\n"
"border: 1px solid black;\n"
"background-color: #FFFFFF;\n"
"color: #000000;\n"
"font-size: 65px;\n"
"}")
        self.BtnAdvanced_2.setObjectName("BtnAdvanced_2")
        self.LblTime = QtWidgets.QLabel(self.AdvancedPage)
        self.LblTime.setGeometry(QtCore.QRect(30, 220, 151, 51))
        self.LblTime.setStyleSheet("color:#FFFFFF;\n"
"font-size: 55px;\n"
"font-family: \'Bit9x9\';\n"
"")
        self.LblTime.setObjectName("LblTime")
        self.TxtTime = QtWidgets.QTextEdit(self.AdvancedPage)
        self.TxtTime.setGeometry(QtCore.QRect(580, 210, 161, 74))
        self.TxtTime.setStyleSheet("#TxtTime{\n"
"border: 1px solid white;\n"
"color: #FFFFFF;\n"
"font-size: 65px;\n"
"font-family: \'Bit9x9\';\n"
"}\n"
"#TxtTime:Hover{\n"
"\n"
"}")
        self.TxtTime.setObjectName("TxtTime")
        self.LblYear = QtWidgets.QLabel(self.AdvancedPage)
        self.LblYear.setGeometry(QtCore.QRect(30, 580, 451, 51))
        self.LblYear.setStyleSheet("color:#FFFFFF;\n"
"font-size: 55px;\n"
"font-family: \'Bit9x9\';\n"
"")
        self.LblYear.setObjectName("LblYear")
        self.LblPoints = QtWidgets.QLabel(self.AdvancedPage)
        self.LblPoints.setGeometry(QtCore.QRect(30, 400, 231, 51))
        self.LblPoints.setStyleSheet("color:#FFFFFF;\n"
"font-size: 55px;\n"
"font-family: \'Bit9x9\';\n"
"")
        self.LblPoints.setObjectName("LblPoints")
        self.TxtSpeed = QtWidgets.QTextEdit(self.AdvancedPage)
        self.TxtSpeed.textChanged.connect(self.GetSpeed)

        self.TxtSpeed.setGeometry(QtCore.QRect(580, 780, 161, 74))
        self.TxtSpeed.setStyleSheet("border: 1px solid white;\n"
"color: #FFFFFF;\n"
"font-size: 65px;\n"
"font-family: \'Bit9x9\';")
        self.TxtSpeed.setObjectName("TxtSpeed")
        self.LblSpeed = QtWidgets.QLabel(self.AdvancedPage)
        self.LblSpeed.setGeometry(QtCore.QRect(50, 790, 311, 51))
        self.LblSpeed.setStyleSheet("color:#FFFFFF;\n"
"font-size: 55px;\n"
"font-family: \'Bit9x9\';\n"
"")
        self.LblSpeed.setObjectName("LblSpeed")
        self.TxtPoints = QtWidgets.QTextEdit(self.AdvancedPage)
        self.TxtPoints.textChanged.connect(self.GetPoints)

        self.TxtPoints.setGeometry(QtCore.QRect(580, 390, 161, 74))
        self.TxtPoints.setStyleSheet("border: 1px solid white;\n"
"color: #FFFFFF;\n"
"font-size: 65px;\n"
"font-family: \'Bit9x9\';")
        self.TxtPoints.setObjectName("TxtPoints")
        self.checkBox = QtWidgets.QCheckBox(self.AdvancedPage)
        self.checkBox.setGeometry(QtCore.QRect(200, 230, 41, 41))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.AdvancedPage)
        self.checkBox_2.setGeometry(QtCore.QRect(280, 400, 41, 41))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.TxtYear = QtWidgets.QTextEdit(self.AdvancedPage)
        self.TxtYear.setGeometry(QtCore.QRect(580, 570, 161, 74))
        self.TxtYear.setStyleSheet("border: 1px solid white;\n"
"color: #FFFFFF;\n"
"font-size: 65px;\n"
"font-family: \'Bit9x9\';")
        self.TxtYear.setObjectName("TxtYear")
        self.LblTime_2 = QtWidgets.QLabel(self.AdvancedPage)
        self.TxtPoints.textChanged.connect(self.GetTime)

        self.LblTime_2.setGeometry(QtCore.QRect(760, 260, 171, 21))
        self.LblTime_2.setStyleSheet("color:#FFFFFF;\n"
"font-size: 30px;\n"
"font-family: \'Bit9x9\';\n"
"")
        self.LblTime_2.setObjectName("LblTime_2")
        self.stackedWidget.addWidget(self.AdvancedPage)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #Connectie met buttons

        self.BtnStart.clicked.connect(lambda *args: self.stackedWidget.setCurrentIndex(1))
        self.BtnAdvanced.clicked.connect(lambda *args: self.stackedWidget.setCurrentIndex(2))
        self.BtnSettings.clicked.connect(lambda *args: self.stackedWidget.setCurrentIndex(1))
        self.BtnSettings_2.clicked.connect(lambda *args: self.stackedWidget.setCurrentIndex(1))

        #CONNECTIE MET PLAYER BUTTONS

        self.Btn1p_2.clicked.connect(self.ChangePlayers1)
        self.Btn2p.clicked.connect(self.ChangePlayers2)

        # connectie met thema buttons

        self.BtnRetro.clicked.connect(self.ChangeTheme1)
        self.BtnFortNite.clicked.connect(self.ChangeTheme2)
        self.BtnCastle.clicked.connect(self.ChangeTheme3)

        #Game connection

        self.BtnStart_2.clicked.connect(self.OpenPongGame)

        #Spelers aanpassen
    def ChangePlayers1(self):
        global PLAYERS
        PLAYERS = 1
        print(PLAYERS)

    def ChangePlayers2(self):
        global PLAYERS
        PLAYERS = 2
        print(PLAYERS)

#Advanced Inputs
    def GetSpeed(self):
        global SPEED
        try:
                SPEED = int(self.TxtSpeed.toPlainText())
        except ValueError:
                print ("Invalid string found in: {}".format(SPEED))

    def GetPoints(self):
        global POINTS
        try:
                POINTS = int(self.TxtPoints.toPlainText())
        except ValueError:
                print ("Invalid string found in: {}".format(POINTS))

    def GetTime(self):
        global TIME
        try:
                TIME = int(self.TxtPoints.toPlainText())
        except ValueError:
                print ("Invalid string found in: {}".format(TIME))
        print(TIME)

    #playmode
    def Playmode(self):
        global PLAYMODE
        if self.checkBox == self.checkBox.QCheckBox.checkstate(True):
                PLAYMODE = "score"
        elif self.checkBox_2 == self.checkBox_2.checkstate(True):
            PLAYMODE = "time"
        print(PLAYMODE)


# Thema's aanpassen
    def ChangeTheme1(self):
            global THEME
            THEME = 3
            print(THEME)
    def ChangeTheme2(self):
            global THEME
            THEME = 1
            print(THEME)
    def ChangeTheme3(self):
            global THEME
            THEME = 2
            print( THEME)

    def OpenPongGame(self, mainwindow):
        print('Pong game is gestart')
        Pong_demo(mode = "PLAYMODE", paddle_speed=SPEED // 2, theme=THEME, play_time=TIME, players=PLAYERS, ball_speed=SPEED, win_score=POINTS)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LblTitle.setText(_translate("MainWindow", "PONG"))
        self.BtnStart.setText(_translate("MainWindow", "GET STARTED"))
        self.BtnCalibrate.setText(_translate("MainWindow", "Calibrate"))
        self.Btn2p.setText(_translate("MainWindow", "2"))
        self.BtnStart_2.setText(_translate("MainWindow", "START"))
        self.BtnAdvanced.setText(_translate("MainWindow", "ADMIN"))
        self.BtnSettings.setText(_translate("MainWindow", "INSTELLINGEN"))
        self.BtnNmbrPlayers.setText(_translate("MainWindow", "AANTAL SPELERS"))
        self.Btn1p_2.setText(_translate("MainWindow", "1"))
        self.BtnChooseTheme.setText(_translate("MainWindow", "KIES THEMA"))
        self.BtnSettings_2.setText(_translate("MainWindow", "INSTELLINGEN"))
        self.BtnAdvanced_2.setText(_translate("MainWindow", "ADMIN"))
        self.LblTime.setText(_translate("MainWindow", "TIJD"))
        self.LblYear.setText(_translate("MainWindow", "STUDIE JAAR"))
        self.LblPoints.setText(_translate("MainWindow", "PUNTEN"))
        self.LblSpeed.setText(_translate("MainWindow", "SNELHEID"))
        self.LblTime_2.setText(_translate("MainWindow", "Seconden"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
