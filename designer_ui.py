# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.wtabUpdates = QtWidgets.QWidget()
        self.wtabUpdates.setObjectName("wtabUpdates")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wtabUpdates)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.wtabUpdates)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_7 = QtWidgets.QFrame(self.groupBox)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.tpytubeStatus = QtWidgets.QLabel(self.frame_7)
        self.tpytubeStatus.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.tpytubeStatus.setFont(font)
        self.tpytubeStatus.setText("")
        self.tpytubeStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.tpytubeStatus.setObjectName("tpytubeStatus")
        self.verticalLayout_3.addWidget(self.tpytubeStatus)
        self.verticalLayout.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(self.groupBox)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setMinimumSize(QtCore.QSize(90, 0))
        self.label_8.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.tcurrentVersion = QtWidgets.QLineEdit(self.frame_6)
        self.tcurrentVersion.setText("")
        self.tcurrentVersion.setReadOnly(True)
        self.tcurrentVersion.setObjectName("tcurrentVersion")
        self.horizontalLayout_8.addWidget(self.tcurrentVersion)
        self.verticalLayout.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.groupBox)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setMinimumSize(QtCore.QSize(90, 0))
        self.label_6.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.tversionList = QtWidgets.QComboBox(self.frame_4)
        self.tversionList.setEditable(False)
        self.tversionList.setObjectName("tversionList")
        self.tversionList.addItem("")
        self.tversionList.setItemText(0, "")
        self.tversionList.addItem("")
        self.horizontalLayout_6.addWidget(self.tversionList)
        self.verticalLayout.addWidget(self.frame_4)
        self.bupdatePytube = QtWidgets.QPushButton(self.groupBox)
        self.bupdatePytube.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bupdatePytube.setFont(font)
        self.bupdatePytube.setObjectName("bupdatePytube")
        self.verticalLayout.addWidget(self.bupdatePytube)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.wtabUpdates)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.tytdlStatus = QtWidgets.QLabel(self.widget_3)
        self.tytdlStatus.setMinimumSize(QtCore.QSize(0, 40))
        self.tytdlStatus.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        self.tytdlStatus.setFont(font)
        self.tytdlStatus.setText("")
        self.tytdlStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.tytdlStatus.setObjectName("tytdlStatus")
        self.verticalLayout_4.addWidget(self.tytdlStatus)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(90, 0))
        self.label_7.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.tytdlVersion = QtWidgets.QLineEdit(self.widget)
        self.tytdlVersion.setReadOnly(True)
        self.tytdlVersion.setObjectName("tytdlVersion")
        self.horizontalLayout_7.addWidget(self.tytdlVersion)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.widget_2)
        self.label_9.setMinimumSize(QtCore.QSize(90, 0))
        self.label_9.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.tytdlLatest = QtWidgets.QLineEdit(self.widget_2)
        self.tytdlLatest.setReadOnly(True)
        self.tytdlLatest.setObjectName("tytdlLatest")
        self.horizontalLayout_9.addWidget(self.tytdlLatest)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.bopenGit = QtWidgets.QPushButton(self.groupBox_2)
        self.bopenGit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        self.bopenGit.setFont(font)
        self.bopenGit.setObjectName("bopenGit")
        self.verticalLayout_2.addWidget(self.bopenGit)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.brefreshVersions = QtWidgets.QPushButton(self.wtabUpdates)
        self.brefreshVersions.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        self.brefreshVersions.setFont(font)
        self.brefreshVersions.setObjectName("brefreshVersions")
        self.gridLayout_2.addWidget(self.brefreshVersions, 1, 0, 1, 2)
        self.tabWidget.addTab(self.wtabUpdates, "")
        self.wtabDownload = QtWidgets.QWidget()
        self.wtabDownload.setObjectName("wtabDownload")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.wtabDownload)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.wdownloadSettings = QtWidgets.QGroupBox(self.wtabDownload)
        self.wdownloadSettings.setObjectName("wdownloadSettings")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.wdownloadSettings)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.wdownloadURL = QtWidgets.QWidget(self.wdownloadSettings)
        self.wdownloadURL.setObjectName("wdownloadURL")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.wdownloadURL)
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tdownloadURL = QtWidgets.QLabel(self.wdownloadURL)
        self.tdownloadURL.setMinimumSize(QtCore.QSize(75, 0))
        self.tdownloadURL.setMaximumSize(QtCore.QSize(75, 16777215))
        self.tdownloadURL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tdownloadURL.setObjectName("tdownloadURL")
        self.horizontalLayout_11.addWidget(self.tdownloadURL)
        self.idownloadURL = QtWidgets.QLineEdit(self.wdownloadURL)
        self.idownloadURL.setObjectName("idownloadURL")
        self.horizontalLayout_11.addWidget(self.idownloadURL)
        self.verticalLayout_5.addWidget(self.wdownloadURL)
        self.wdownloadMode = QtWidgets.QWidget(self.wdownloadSettings)
        self.wdownloadMode.setObjectName("wdownloadMode")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.wdownloadMode)
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.idownloadMode = QtWidgets.QLabel(self.wdownloadMode)
        self.idownloadMode.setMinimumSize(QtCore.QSize(75, 0))
        self.idownloadMode.setMaximumSize(QtCore.QSize(75, 16777215))
        self.idownloadMode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.idownloadMode.setObjectName("idownloadMode")
        self.horizontalLayout_12.addWidget(self.idownloadMode)
        self.bdownloadModePlaylist = QtWidgets.QRadioButton(self.wdownloadMode)
        self.bdownloadModePlaylist.setChecked(True)
        self.bdownloadModePlaylist.setObjectName("bdownloadModePlaylist")
        self.horizontalLayout_12.addWidget(self.bdownloadModePlaylist)
        self.bdownloadModeVideo = QtWidgets.QRadioButton(self.wdownloadMode)
        self.bdownloadModeVideo.setObjectName("bdownloadModeVideo")
        self.horizontalLayout_12.addWidget(self.bdownloadModeVideo)
        self.verticalLayout_5.addWidget(self.wdownloadMode)
        self.woutputPath = QtWidgets.QWidget(self.wdownloadSettings)
        self.woutputPath.setObjectName("woutputPath")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.woutputPath)
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.toutputPath = QtWidgets.QLabel(self.woutputPath)
        self.toutputPath.setMinimumSize(QtCore.QSize(75, 0))
        self.toutputPath.setMaximumSize(QtCore.QSize(75, 16777215))
        self.toutputPath.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.toutputPath.setObjectName("toutputPath")
        self.horizontalLayout_10.addWidget(self.toutputPath)
        self.ioutputPath = QtWidgets.QLineEdit(self.woutputPath)
        self.ioutputPath.setText("")
        self.ioutputPath.setObjectName("ioutputPath")
        self.horizontalLayout_10.addWidget(self.ioutputPath)
        self.boutputPath = QtWidgets.QPushButton(self.woutputPath)
        self.boutputPath.setMinimumSize(QtCore.QSize(50, 0))
        self.boutputPath.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.boutputPath.setFont(font)
        self.boutputPath.setObjectName("boutputPath")
        self.horizontalLayout_10.addWidget(self.boutputPath)
        self.verticalLayout_5.addWidget(self.woutputPath)
        self.wdownloadConvert = QtWidgets.QWidget(self.wdownloadSettings)
        self.wdownloadConvert.setObjectName("wdownloadConvert")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.wdownloadConvert)
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.tdownloadConvert = QtWidgets.QLabel(self.wdownloadConvert)
        self.tdownloadConvert.setMinimumSize(QtCore.QSize(75, 0))
        self.tdownloadConvert.setMaximumSize(QtCore.QSize(75, 16777215))
        self.tdownloadConvert.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tdownloadConvert.setObjectName("tdownloadConvert")
        self.horizontalLayout_14.addWidget(self.tdownloadConvert)
        self.idownloadConvert = QtWidgets.QComboBox(self.wdownloadConvert)
        self.idownloadConvert.setEditable(True)
        self.idownloadConvert.setObjectName("idownloadConvert")
        self.horizontalLayout_14.addWidget(self.idownloadConvert)
        self.verticalLayout_5.addWidget(self.wdownloadConvert)
        self.bdownloadURL = QtWidgets.QPushButton(self.wdownloadSettings)
        self.bdownloadURL.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.bdownloadURL.setFont(font)
        self.bdownloadURL.setObjectName("bdownloadURL")
        self.verticalLayout_5.addWidget(self.bdownloadURL)
        self.verticalLayout_6.addWidget(self.wdownloadSettings)
        self.wdownloadLog = QtWidgets.QGroupBox(self.wtabDownload)
        self.wdownloadLog.setObjectName("wdownloadLog")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.wdownloadLog)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.tdownloadLog = QtWidgets.QTextEdit(self.wdownloadLog)
        self.tdownloadLog.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tdownloadLog.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tdownloadLog.setReadOnly(True)
        self.tdownloadLog.setObjectName("tdownloadLog")
        self.horizontalLayout_13.addWidget(self.tdownloadLog)
        self.verticalLayout_6.addWidget(self.wdownloadLog)
        self.tabWidget.addTab(self.wtabDownload, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.idownloadConvert.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "PyTube"))
        self.label_11.setText(_translate("MainWindow", "Status:"))
        self.label_8.setText(_translate("MainWindow", "Current version:"))
        self.label_6.setText(_translate("MainWindow", "Available versions:"))
        self.tversionList.setItemText(1, _translate("MainWindow", "owo"))
        self.bupdatePytube.setText(_translate("MainWindow", "Update PyTube"))
        self.groupBox_2.setTitle(_translate("MainWindow", "YTDL"))
        self.label_10.setText(_translate("MainWindow", "Status:"))
        self.label_7.setText(_translate("MainWindow", "Current version:"))
        self.label_9.setText(_translate("MainWindow", "Latest version:"))
        self.bopenGit.setText(_translate("MainWindow", "Open Github"))
        self.brefreshVersions.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wtabUpdates), _translate("MainWindow", "Updates"))
        self.wdownloadSettings.setTitle(_translate("MainWindow", "Settings"))
        self.tdownloadURL.setToolTip(_translate("MainWindow", "The URL of the video/playlist.\n"
"You can also just provide the ID, E.G v=HQC9sToSdmM"))
        self.tdownloadURL.setText(_translate("MainWindow", "YouTube URL:"))
        self.idownloadURL.setToolTip(_translate("MainWindow", "The URL of the video/playlist.\n"
"You can also just provide the ID, E.G v=HQC9sToSdmM"))
        self.idownloadURL.setText(_translate("MainWindow", "https://www.youtube.com/watch?v=HQC9sToSdmM"))
        self.idownloadMode.setToolTip(_translate("MainWindow", "Video: Download a single video\n"
"Playlist: Download a whole playlist."))
        self.idownloadMode.setText(_translate("MainWindow", "Mode:"))
        self.bdownloadModePlaylist.setToolTip(_translate("MainWindow", "Video: Download a single video\n"
"Playlist: Download a whole playlist."))
        self.bdownloadModePlaylist.setText(_translate("MainWindow", "Playlist"))
        self.bdownloadModeVideo.setToolTip(_translate("MainWindow", "Video: Download a single video\n"
"Playlist: Download a whole playlist."))
        self.bdownloadModeVideo.setText(_translate("MainWindow", "Video"))
        self.toutputPath.setToolTip(_translate("MainWindow", "Where to save the file"))
        self.toutputPath.setText(_translate("MainWindow", "Output Path:"))
        self.ioutputPath.setToolTip(_translate("MainWindow", "Where to save the file"))
        self.boutputPath.setText(_translate("MainWindow", "..."))
        self.tdownloadConvert.setToolTip(_translate("MainWindow", "Convert downloaded file to a different format.\n"
"Leave blank for no conversion.\n"
"\n"
"Type in your own valid audio/video format, or use one of the presets."))
        self.tdownloadConvert.setText(_translate("MainWindow", "Convert:"))
        self.idownloadConvert.setToolTip(_translate("MainWindow", "Convert downloaded file to a different format.\n"
"Leave blank for no conversion.\n"
"\n"
"Type in your own valid audio/video format, or use one of the presets."))
        self.bdownloadURL.setText(_translate("MainWindow", "Download"))
        self.wdownloadLog.setTitle(_translate("MainWindow", "Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wtabDownload), _translate("MainWindow", "Donwload"))
