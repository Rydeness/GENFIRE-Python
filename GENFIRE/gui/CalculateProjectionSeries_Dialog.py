# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculateprojectionseries_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CalculateProjectionSeries_Dialog(object):
    def setupUi(self, CalculateProjectionSeries_Dialog):
        CalculateProjectionSeries_Dialog.setObjectName(_fromUtf8("CalculateProjectionSeries_Dialog"))
        CalculateProjectionSeries_Dialog.resize(762, 352)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CalculateProjectionSeries_Dialog.sizePolicy().hasHeightForWidth())
        CalculateProjectionSeries_Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QtGui.QVBoxLayout(CalculateProjectionSeries_Dialog)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(CalculateProjectionSeries_Dialog)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_angleFile = QtGui.QLineEdit(CalculateProjectionSeries_Dialog)
        self.lineEdit_angleFile.setMinimumSize(QtCore.QSize(500, 0))
        self.lineEdit_angleFile.setObjectName(_fromUtf8("lineEdit_angleFile"))
        self.horizontalLayout_2.addWidget(self.lineEdit_angleFile)
        self.btn_selectAngleFile = QtGui.QPushButton(CalculateProjectionSeries_Dialog)
        self.btn_selectAngleFile.setObjectName(_fromUtf8("btn_selectAngleFile"))
        self.horizontalLayout_2.addWidget(self.btn_selectAngleFile)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.line = QtGui.QFrame(CalculateProjectionSeries_Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_8.addWidget(self.line)
        self.label_9 = QtGui.QLabel(CalculateProjectionSeries_Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_8.addWidget(self.label_9)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_7 = QtGui.QLabel(CalculateProjectionSeries_Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_2 = QtGui.QLabel(CalculateProjectionSeries_Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.label_8 = QtGui.QLabel(CalculateProjectionSeries_Dialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_5.addWidget(self.label_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.lineEdit_phi = QtGui.QLineEdit(CalculateProjectionSeries_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_phi.sizePolicy().hasHeightForWidth())
        self.lineEdit_phi.setSizePolicy(sizePolicy)
        self.lineEdit_phi.setMaxLength(4)
        self.lineEdit_phi.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_phi.setObjectName(_fromUtf8("lineEdit_phi"))
        self.verticalLayout_6.addWidget(self.lineEdit_phi)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit_thetaStart = QtGui.QLineEdit(CalculateProjectionSeries_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_thetaStart.sizePolicy().hasHeightForWidth())
        self.lineEdit_thetaStart.setSizePolicy(sizePolicy)
        self.lineEdit_thetaStart.setMaxLength(4)
        self.lineEdit_thetaStart.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_thetaStart.setObjectName(_fromUtf8("lineEdit_thetaStart"))
        self.verticalLayout.addWidget(self.lineEdit_thetaStart)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.lineEdit_psi = QtGui.QLineEdit(CalculateProjectionSeries_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_psi.sizePolicy().hasHeightForWidth())
        self.lineEdit_psi.setSizePolicy(sizePolicy)
        self.lineEdit_psi.setMinimumSize(QtCore.QSize(10, 20))
        self.lineEdit_psi.setBaseSize(QtCore.QSize(2, 0))
        self.lineEdit_psi.setMaxLength(4)
        self.lineEdit_psi.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_psi.setObjectName(_fromUtf8("lineEdit_psi"))
        self.verticalLayout_6.addWidget(self.lineEdit_psi)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.label_4 = QtGui.QLabel(CalculateProjectionSeries_Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lineEdit_thetaStep = QtGui.QLineEdit(CalculateProjectionSeries_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_thetaStep.sizePolicy().hasHeightForWidth())
        self.lineEdit_thetaStep.setSizePolicy(sizePolicy)
        self.lineEdit_thetaStep.setMaxLength(4)
        self.lineEdit_thetaStep.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_thetaStep.setObjectName(_fromUtf8("lineEdit_thetaStep"))
        self.verticalLayout_3.addWidget(self.lineEdit_thetaStep)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.label_5 = QtGui.QLabel(CalculateProjectionSeries_Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.lineEdit_thetaStop = QtGui.QLineEdit(CalculateProjectionSeries_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_thetaStop.sizePolicy().hasHeightForWidth())
        self.lineEdit_thetaStop.setSizePolicy(sizePolicy)
        self.lineEdit_thetaStop.setMaxLength(4)
        self.lineEdit_thetaStop.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_thetaStop.setObjectName(_fromUtf8("lineEdit_thetaStop"))
        self.verticalLayout_4.addWidget(self.lineEdit_thetaStop)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.label_6 = QtGui.QLabel(CalculateProjectionSeries_Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.checkBox_saveAngles = QtGui.QCheckBox(CalculateProjectionSeries_Dialog)
        self.checkBox_saveAngles.setObjectName(_fromUtf8("checkBox_saveAngles"))
        self.verticalLayout_8.addWidget(self.checkBox_saveAngles)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(CalculateProjectionSeries_Dialog)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.lineEdit_outputFilename = QtGui.QLineEdit(CalculateProjectionSeries_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_outputFilename.sizePolicy().hasHeightForWidth())
        self.lineEdit_outputFilename.setSizePolicy(sizePolicy)
        self.lineEdit_outputFilename.setObjectName(_fromUtf8("lineEdit_outputFilename"))
        self.horizontalLayout_6.addWidget(self.lineEdit_outputFilename)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.label_10 = QtGui.QLabel(CalculateProjectionSeries_Dialog)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_8.addWidget(self.label_10)
        self.line_2 = QtGui.QFrame(CalculateProjectionSeries_Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_8.addWidget(self.line_2)
        self.buttonBox = QtGui.QDialogButtonBox(CalculateProjectionSeries_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_8.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.retranslateUi(CalculateProjectionSeries_Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), CalculateProjectionSeries_Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), CalculateProjectionSeries_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CalculateProjectionSeries_Dialog)
        CalculateProjectionSeries_Dialog.setTabOrder(self.lineEdit_angleFile, self.btn_selectAngleFile)
        CalculateProjectionSeries_Dialog.setTabOrder(self.btn_selectAngleFile, self.lineEdit_phi)
        CalculateProjectionSeries_Dialog.setTabOrder(self.lineEdit_phi, self.lineEdit_thetaStart)
        CalculateProjectionSeries_Dialog.setTabOrder(self.lineEdit_thetaStart, self.lineEdit_thetaStep)
        CalculateProjectionSeries_Dialog.setTabOrder(self.lineEdit_thetaStep, self.lineEdit_thetaStop)
        CalculateProjectionSeries_Dialog.setTabOrder(self.lineEdit_thetaStop, self.lineEdit_psi)
        CalculateProjectionSeries_Dialog.setTabOrder(self.lineEdit_psi, self.lineEdit_outputFilename)

    def retranslateUi(self, CalculateProjectionSeries_Dialog):
        CalculateProjectionSeries_Dialog.setWindowTitle(_translate("CalculateProjectionSeries_Dialog", "Dialog", None))
        self.label_3.setText(_translate("CalculateProjectionSeries_Dialog", "Filename Containing Euler Angles", None))
        self.btn_selectAngleFile.setText(_translate("CalculateProjectionSeries_Dialog", "Browse", None))
        self.label_9.setText(_translate("CalculateProjectionSeries_Dialog", "Generate Euler Angles", None))
        self.label_7.setText(_translate("CalculateProjectionSeries_Dialog", "Phi", None))
        self.label_2.setText(_translate("CalculateProjectionSeries_Dialog", "Theta (Tilt)", None))
        self.label_8.setText(_translate("CalculateProjectionSeries_Dialog", "Psi", None))
        self.label_4.setText(_translate("CalculateProjectionSeries_Dialog", "Start", None))
        self.label_5.setText(_translate("CalculateProjectionSeries_Dialog", "Step", None))
        self.label_6.setText(_translate("CalculateProjectionSeries_Dialog", "Stop", None))
        self.checkBox_saveAngles.setText(_translate("CalculateProjectionSeries_Dialog", "Save Angles", None))
        self.label.setText(_translate("CalculateProjectionSeries_Dialog", "Projection Filename", None))
        self.label_10.setText(_translate("CalculateProjectionSeries_Dialog", "*.mrc, *.npy, or *.mat", None))

