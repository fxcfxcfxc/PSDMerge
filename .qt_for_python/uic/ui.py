# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TextureMange(object):
    def setupUi(self, TextureMange):
        if not TextureMange.objectName():
            TextureMange.setObjectName(u"TextureMange")
        TextureMange.setEnabled(True)
        TextureMange.resize(1880, 1019)
        TextureMange.setMinimumSize(QSize(1880, 1019))
        TextureMange.setMaximumSize(QSize(1880, 1200))
        TextureMange.setAutoFillBackground(False)
        TextureMange.setStyleSheet(u"color:rgb(176, 190, 199);\n"
"background-color: rgb(25, 34, 46);\n"
"")
        self.gridLayout_2 = QGridLayout(TextureMange)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(TextureMange)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setStyleSheet(u"QTabBar::tab{ background-color: #1a1f26}\n"
"QTabBar::tab:selected {\n"
"\n"
"background-color:rgb(59, 67, 71);\n"
"}\n"
"\n"
"\n"
"\n"
"QTabWidget::pane\n"
"\n"
"{\n"
"border-width: 0px;\n"
"\n"
"border-color:white;\n"
"\n"
"border-style:outset;\n"
"\n"
"border-radius: 3px;\n"
"\n"
"\n"
"}\u200b\n"
"\n"
"font: 12px \"Tahoma\";")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
#if QT_CONFIG(statustip)
        self.tab.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.tab.setAutoFillBackground(False)
        self.tab.setStyleSheet(u"")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 720, 901, 251))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"QLineEdit { background-color: rgb(29, 56, 89) }\n"
"\n"
"QPushButton {\n"
"\n"
" background-color: rgb(37, 79, 107) }\n"
"\n"
"QGroupBox {border-width: 1px;\n"
"    border-style: dashed;\n"
"    border-color: rgb(195, 199, 209);}\n"
"QLineEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(88, 88, 88);\n"
"}")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_8.addWidget(self.lineEdit_5)

        self.coust_Button = QPushButton(self.groupBox)
        self.coust_Button.setObjectName(u"coust_Button")

        self.horizontalLayout_8.addWidget(self.coust_Button)

        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_8.addWidget(self.checkBox_3)

        self.horizontalLayout_8.setStretch(0, 2)

        self.verticalLayout_17.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tex_json = QPushButton(self.groupBox)
        self.tex_json.setObjectName(u"tex_json")

        self.horizontalLayout_9.addWidget(self.tex_json)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_9.addWidget(self.pushButton)


        self.verticalLayout_17.addLayout(self.horizontalLayout_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout.addWidget(self.label_5)

        self.basename = QLineEdit(self.groupBox)
        self.basename.setObjectName(u"basename")

        self.horizontalLayout.addWidget(self.basename)

        self.r_name = QLineEdit(self.groupBox)
        self.r_name.setObjectName(u"r_name")

        self.horizontalLayout.addWidget(self.r_name)

        self.g_name = QLineEdit(self.groupBox)
        self.g_name.setObjectName(u"g_name")

        self.horizontalLayout.addWidget(self.g_name)

        self.b_name = QLineEdit(self.groupBox)
        self.b_name.setObjectName(u"b_name")

        self.horizontalLayout.addWidget(self.b_name)

        self.a_name = QLineEdit(self.groupBox)
        self.a_name.setObjectName(u"a_name")

        self.horizontalLayout.addWidget(self.a_name)

        self.tex_file_line = QLineEdit(self.groupBox)
        self.tex_file_line.setObjectName(u"tex_file_line")

        self.horizontalLayout.addWidget(self.tex_file_line)

        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBox_2)


        self.verticalLayout_17.addLayout(self.horizontalLayout)

        self.mergeButton = QPushButton(self.groupBox)
        self.mergeButton.setObjectName(u"mergeButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mergeButton.sizePolicy().hasHeightForWidth())
        self.mergeButton.setSizePolicy(sizePolicy1)
        self.mergeButton.setMaximumSize(QSize(16777215, 40))
        self.mergeButton.setStyleSheet(u"background-color: rgb(198, 132, 0);\n"
"color: rgb(0, 0, 0);")
        self.mergeButton.setAutoDefault(False)

        self.verticalLayout_17.addWidget(self.mergeButton)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 10, 901, 151))
        self.groupBox_2.setMouseTracking(False)
        self.groupBox_2.setTabletTracking(False)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet(u"QLineEdit { background-color: rgb(29, 56, 89) }\n"
"\n"
"QPushButton {\n"
"\n"
" background-color: rgb(37, 79, 107) }\n"
"\n"
"QGroupBox {border-width: 1px;\n"
"    border-style: dashed;\n"
"    border-color: rgb(195, 199, 209);}\n"
"QLineEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(88, 88, 88);\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.psd_lineEdit = QLineEdit(self.groupBox_2)
        self.psd_lineEdit.setObjectName(u"psd_lineEdit")

        self.horizontalLayout_5.addWidget(self.psd_lineEdit)

        self.psd_Button = QPushButton(self.groupBox_2)
        self.psd_Button.setObjectName(u"psd_Button")

        self.horizontalLayout_5.addWidget(self.psd_Button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.checkBox_4 = QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setChecked(True)

        self.horizontalLayout_6.addWidget(self.checkBox_4)

        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_6.addWidget(self.checkBox)

        self.out_Button = QPushButton(self.groupBox_2)
        self.out_Button.setObjectName(u"out_Button")
        self.out_Button.setStyleSheet(u"background-color: rgb(198, 132, 0);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_6.addWidget(self.out_Button)

        self.horizontalLayout_6.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.progressBar = QProgressBar(self.groupBox_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.show_box = QGroupBox(self.tab)
        self.show_box.setObjectName(u"show_box")
        self.show_box.setGeometry(QRect(910, 10, 931, 961))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.show_box.sizePolicy().hasHeightForWidth())
        self.show_box.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"BIZ UDPGothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.show_box.setFont(font)
        self.show_box.setAutoFillBackground(False)
        self.show_box.setStyleSheet(u"QGroupBox {border-width: 3px;\n"
"    border-style: dashed;\n"
"    border-color: rgba(71, 85, 104, 242);}\n"
"\n"
"QGroupBox {background-color: rgb(36, 49, 66);}")
        self.verticalLayout_6 = QVBoxLayout(self.show_box)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.label_image = QLabel(self.show_box)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setScaledContents(False)
        self.label_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_image)

        self.pngname_lineEdit = QLabel(self.show_box)
        self.pngname_lineEdit.setObjectName(u"pngname_lineEdit")
        self.pngname_lineEdit.setStyleSheet(u"background-color: rgb(36, 49, 66);")
        self.pngname_lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.pngname_lineEdit)

        self.verticalLayout_6.setStretch(1, 8)
        self.verticalLayout_6.setStretch(2, 1)
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 170, 901, 541))
        sizePolicy2.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy2)
        self.groupBox_5.setStyleSheet(u"QLineEdit { background-color: rgb(29, 56, 89) }\n"
"\n"
"QPushButton {\n"
"\n"
" background-color: rgb(37, 79, 107) }\n"
"\n"
"QGroupBox {border-width: 1px;\n"
"    border-style: dashed;\n"
"    border-color: rgb(195, 199, 209);}\n"
"QLineEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(88, 88, 88);\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fast_Button = QPushButton(self.groupBox_5)
        self.fast_Button.setObjectName(u"fast_Button")
        sizePolicy1.setHeightForWidth(self.fast_Button.sizePolicy().hasHeightForWidth())
        self.fast_Button.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.fast_Button)

        self.yushe01 = QHBoxLayout()
        self.yushe01.setObjectName(u"yushe01")
        self.mark_Button = QPushButton(self.groupBox_5)
        self.mark_Button.setObjectName(u"mark_Button")
        self.mark_Button.setStyleSheet(u"background-color: rgb(52, 126, 157);")

        self.yushe01.addWidget(self.mark_Button)

        self.mark_Button_3 = QPushButton(self.groupBox_5)
        self.mark_Button_3.setObjectName(u"mark_Button_3")
        self.mark_Button_3.setStyleSheet(u"background-color: rgb(52, 126, 157);")

        self.yushe01.addWidget(self.mark_Button_3)


        self.verticalLayout_2.addLayout(self.yushe01)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.groupBox1 = QGroupBox(self.groupBox_5)
        self.groupBox1.setObjectName(u"groupBox1")
        self.verticalLayout = QVBoxLayout(self.groupBox1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.R = QLabel(self.groupBox1)
        self.R.setObjectName(u"R")
        self.R.setCursor(QCursor(Qt.ArrowCursor))
        self.R.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.horizontalLayout_2.addWidget(self.R)

        self.mark_r = QLineEdit(self.groupBox1)
        self.mark_r.setObjectName(u"mark_r")

        self.horizontalLayout_2.addWidget(self.mark_r)

        self.r_lineEdit = QLineEdit(self.groupBox1)
        self.r_lineEdit.setObjectName(u"r_lineEdit")

        self.horizontalLayout_2.addWidget(self.r_lineEdit)

        self.r_pushButton = QPushButton(self.groupBox1)
        self.r_pushButton.setObjectName(u"r_pushButton")
        font1 = QFont()
        font1.setBold(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        self.r_pushButton.setFont(font1)
        self.r_pushButton.setAutoFillBackground(False)
        self.r_pushButton.setCheckable(False)
        self.r_pushButton.setAutoRepeat(False)
        self.r_pushButton.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.r_pushButton)

        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.groupBox1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.default_r = QLineEdit(self.groupBox1)
        self.default_r.setObjectName(u"default_r")

        self.horizontalLayout_10.addWidget(self.default_r)

        self.label_7 = QLabel(self.groupBox1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.merge_r_c = QLineEdit(self.groupBox1)
        self.merge_r_c.setObjectName(u"merge_r_c")

        self.horizontalLayout_10.addWidget(self.merge_r_c)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)
        self.horizontalLayout_10.setStretch(2, 1)
        self.horizontalLayout_10.setStretch(3, 2)
        self.horizontalLayout_10.setStretch(4, 8)

        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.verticalLayout_7.addWidget(self.groupBox1)

        self.groupBox2 = QGroupBox(self.groupBox_5)
        self.groupBox2.setObjectName(u"groupBox2")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.g_frame = QHBoxLayout()
        self.g_frame.setObjectName(u"g_frame")
        self.G = QLabel(self.groupBox2)
        self.G.setObjectName(u"G")
        self.G.setCursor(QCursor(Qt.ArrowCursor))
        self.G.setStyleSheet(u"color: rgb(39, 204, 20);")

        self.g_frame.addWidget(self.G)

        self.mark_g = QLineEdit(self.groupBox2)
        self.mark_g.setObjectName(u"mark_g")

        self.g_frame.addWidget(self.mark_g)

        self.g_lineEdit = QLineEdit(self.groupBox2)
        self.g_lineEdit.setObjectName(u"g_lineEdit")

        self.g_frame.addWidget(self.g_lineEdit)

        self.g_pushButton = QPushButton(self.groupBox2)
        self.g_pushButton.setObjectName(u"g_pushButton")

        self.g_frame.addWidget(self.g_pushButton)

        self.g_frame.setStretch(2, 1)

        self.verticalLayout_8.addLayout(self.g_frame)

        self.g2_frame = QHBoxLayout()
        self.g2_frame.setObjectName(u"g2_frame")
        self.label_8 = QLabel(self.groupBox2)
        self.label_8.setObjectName(u"label_8")

        self.g2_frame.addWidget(self.label_8)

        self.default_g = QLineEdit(self.groupBox2)
        self.default_g.setObjectName(u"default_g")

        self.g2_frame.addWidget(self.default_g)

        self.label_9 = QLabel(self.groupBox2)
        self.label_9.setObjectName(u"label_9")

        self.g2_frame.addWidget(self.label_9)

        self.merge_g_c = QLineEdit(self.groupBox2)
        self.merge_g_c.setObjectName(u"merge_g_c")

        self.g2_frame.addWidget(self.merge_g_c)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.g2_frame.addItem(self.horizontalSpacer_2)

        self.g2_frame.setStretch(0, 1)
        self.g2_frame.setStretch(1, 2)
        self.g2_frame.setStretch(2, 1)
        self.g2_frame.setStretch(3, 2)
        self.g2_frame.setStretch(4, 8)

        self.verticalLayout_8.addLayout(self.g2_frame)


        self.verticalLayout_7.addWidget(self.groupBox2)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.b_frame = QHBoxLayout()
        self.b_frame.setObjectName(u"b_frame")
        self.label_3 = QLabel(self.groupBox_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setCursor(QCursor(Qt.ArrowCursor))
        self.label_3.setStyleSheet(u"color: rgb(0, 166, 255);")

        self.b_frame.addWidget(self.label_3)

        self.mark_b = QLineEdit(self.groupBox_6)
        self.mark_b.setObjectName(u"mark_b")

        self.b_frame.addWidget(self.mark_b)

        self.b_lineEdit = QLineEdit(self.groupBox_6)
        self.b_lineEdit.setObjectName(u"b_lineEdit")

        self.b_frame.addWidget(self.b_lineEdit)

        self.b_pushButton = QPushButton(self.groupBox_6)
        self.b_pushButton.setObjectName(u"b_pushButton")

        self.b_frame.addWidget(self.b_pushButton)

        self.b_frame.setStretch(2, 1)

        self.verticalLayout_9.addLayout(self.b_frame)

        self.b2_frame = QHBoxLayout()
        self.b2_frame.setObjectName(u"b2_frame")
        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")

        self.b2_frame.addWidget(self.label_15)

        self.default_b = QLineEdit(self.groupBox_6)
        self.default_b.setObjectName(u"default_b")

        self.b2_frame.addWidget(self.default_b)

        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")

        self.b2_frame.addWidget(self.label_16)

        self.merge_b_c = QLineEdit(self.groupBox_6)
        self.merge_b_c.setObjectName(u"merge_b_c")

        self.b2_frame.addWidget(self.merge_b_c)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.b2_frame.addItem(self.horizontalSpacer_5)

        self.b2_frame.setStretch(0, 1)
        self.b2_frame.setStretch(1, 2)
        self.b2_frame.setStretch(2, 1)
        self.b2_frame.setStretch(3, 2)
        self.b2_frame.setStretch(4, 8)

        self.verticalLayout_9.addLayout(self.b2_frame)


        self.verticalLayout_7.addWidget(self.groupBox_6)

        self.groupBox3 = QGroupBox(self.groupBox_5)
        self.groupBox3.setObjectName(u"groupBox3")
        self.verticalLayout_10 = QVBoxLayout(self.groupBox3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.a_frame = QHBoxLayout()
        self.a_frame.setObjectName(u"a_frame")
        self.A = QLabel(self.groupBox3)
        self.A.setObjectName(u"A")
        self.A.setCursor(QCursor(Qt.ArrowCursor))

        self.a_frame.addWidget(self.A)

        self.mark_a = QLineEdit(self.groupBox3)
        self.mark_a.setObjectName(u"mark_a")

        self.a_frame.addWidget(self.mark_a)

        self.a_lineEdit = QLineEdit(self.groupBox3)
        self.a_lineEdit.setObjectName(u"a_lineEdit")

        self.a_frame.addWidget(self.a_lineEdit)

        self.a_pushButton = QPushButton(self.groupBox3)
        self.a_pushButton.setObjectName(u"a_pushButton")

        self.a_frame.addWidget(self.a_pushButton)

        self.a_frame.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.a_frame)

        self.a2_frmae = QHBoxLayout()
        self.a2_frmae.setObjectName(u"a2_frmae")
        self.label_19 = QLabel(self.groupBox3)
        self.label_19.setObjectName(u"label_19")

        self.a2_frmae.addWidget(self.label_19)

        self.default_a = QLineEdit(self.groupBox3)
        self.default_a.setObjectName(u"default_a")

        self.a2_frmae.addWidget(self.default_a)

        self.label_20 = QLabel(self.groupBox3)
        self.label_20.setObjectName(u"label_20")

        self.a2_frmae.addWidget(self.label_20)

        self.merge_a_c = QLineEdit(self.groupBox3)
        self.merge_a_c.setObjectName(u"merge_a_c")

        self.a2_frmae.addWidget(self.merge_a_c)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.a2_frmae.addItem(self.horizontalSpacer_7)

        self.a2_frmae.setStretch(0, 1)
        self.a2_frmae.setStretch(1, 2)
        self.a2_frmae.setStretch(2, 1)
        self.a2_frmae.setStretch(3, 2)
        self.a2_frmae.setStretch(4, 8)

        self.verticalLayout_10.addLayout(self.a2_frmae)


        self.verticalLayout_7.addWidget(self.groupBox3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"QLineEdit { background-color: rgb(29, 56, 89) }\n"
"\n"
"QPushButton {\n"
"\n"
" background-color: rgb(37, 79, 107) }\n"
"\n"
"QGroupBox {border-width: 1px;\n"
"    border-style: dashed;\n"
"    border-color: rgb(195, 199, 209);}\n"
"QLineEdit {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(88, 88, 88);\n"
"}")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)


        self.retranslateUi(TextureMange)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TextureMange)
    # setupUi

    def retranslateUi(self, TextureMange):
        TextureMange.setWindowTitle(QCoreApplication.translate("TextureMange", u"TextureManger_v1.0", None))
        self.groupBox.setTitle(QCoreApplication.translate("TextureMange", u"\u8f93\u51fa\u8bbe\u7f6e", None))
        self.coust_Button.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.checkBox_3.setText(QCoreApplication.translate("TextureMange", u"\u81ea\u5b9a\u4e49\u8def\u5f84\uff08\u5f00\u53d1\u4e2d\uff09", None))
        self.tex_json.setText(QCoreApplication.translate("TextureMange", u"\u4fdd\u5b58\u9884\u8bbe", None))
        self.pushButton.setText(QCoreApplication.translate("TextureMange", u"\u91cd\u7f6e", None))
        self.label_5.setText(QCoreApplication.translate("TextureMange", u"\u6587\u4ef6\u540d", None))
        self.basename.setText(QCoreApplication.translate("TextureMange", u"T", None))
        self.r_name.setText(QCoreApplication.translate("TextureMange", u"_Rock", None))
        self.g_name.setText(QCoreApplication.translate("TextureMange", u"_01", None))
        self.b_name.setText(QCoreApplication.translate("TextureMange", u"_m", None))
        self.a_name.setText("")
        self.tex_file_line.setText(QCoreApplication.translate("TextureMange", u".tga", None))
        self.checkBox_2.setText(QCoreApplication.translate("TextureMange", u"\u5220\u9664\u62c6\u89e3\u7684PNG", None))
        self.mergeButton.setText(QCoreApplication.translate("TextureMange", u"\u5408\u5e76\u8f93\u51fa", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TextureMange", u"Psd", None))
        self.label.setText(QCoreApplication.translate("TextureMange", u"PSD", None))
        self.psd_Button.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.label_2.setText(QCoreApplication.translate("TextureMange", u"\u6ce8\uff1a\u9ed8\u8ba4PNG\u62c6\u5206\u5230psd\u76ee\u5f55\u4e2d", None))
        self.checkBox_4.setText(QCoreApplication.translate("TextureMange", u"\u6309\u7167\u6807\u7b7e\u62c6\u5206\u9700\u8981\u901a\u9053", None))
        self.checkBox.setText(QCoreApplication.translate("TextureMange", u"\u6807\u7b7e\u81ea\u52a8\u5bfc\u5165", None))
        self.out_Button.setText(QCoreApplication.translate("TextureMange", u"PSD\u5206\u89e3\u8f93\u51fa", None))
        self.show_box.setTitle(QCoreApplication.translate("TextureMange", u"\u9884\u89c8", None))
        self.label_image.setText(QCoreApplication.translate("TextureMange", u"image", None))
        self.pngname_lineEdit.setText(QCoreApplication.translate("TextureMange", u"name", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("TextureMange", u"RGBA", None))
        self.fast_Button.setText(QCoreApplication.translate("TextureMange", u"\u624b\u52a8\u9009\u62e9\u5feb\u901f\u5bfc\u5165(\u5f00\u53d1\u4e2d)", None))
        self.mark_Button.setText(QCoreApplication.translate("TextureMange", u"\u4fdd\u5b58\u6807\u7b7e\u540d\u79f0\u9884\u8bbe", None))
        self.mark_Button_3.setText(QCoreApplication.translate("TextureMange", u"\u4fdd\u5b58\u989c\u8272\u8bbe\u7f6e\u9884\u8bbe", None))
        self.groupBox1.setTitle(QCoreApplication.translate("TextureMange", u"R", None))
        self.R.setText(QCoreApplication.translate("TextureMange", u"R\uff1a", None))
        self.mark_r.setText(QCoreApplication.translate("TextureMange", u"\u91d1\u5c5e ", None))
        self.r_pushButton.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.label_6.setText(QCoreApplication.translate("TextureMange", u"\u9ed8\u8ba4\u52a0\u8f7d\u989c\u8272", None))
        self.default_r.setText(QCoreApplication.translate("TextureMange", u"#000000", None))
        self.label_7.setText(QCoreApplication.translate("TextureMange", u"\u5408\u5e76\u989c\u8272", None))
        self.merge_r_c.setText(QCoreApplication.translate("TextureMange", u"#000000", None))
        self.groupBox2.setTitle(QCoreApplication.translate("TextureMange", u"G", None))
        self.G.setText(QCoreApplication.translate("TextureMange", u"G\uff1a", None))
        self.mark_g.setText(QCoreApplication.translate("TextureMange", u"\u5185\u63cf\u8fb9", None))
        self.g_pushButton.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.label_8.setText(QCoreApplication.translate("TextureMange", u"\u9ed8\u8ba4\u52a0\u8f7d\u989c\u8272", None))
        self.default_g.setText(QCoreApplication.translate("TextureMange", u"#000000", None))
        self.label_9.setText(QCoreApplication.translate("TextureMange", u"\u5408\u5e76\u989c\u8272", None))
        self.merge_g_c.setText(QCoreApplication.translate("TextureMange", u"#808080", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("TextureMange", u"B", None))
        self.label_3.setText(QCoreApplication.translate("TextureMange", u"B\uff1a", None))
        self.mark_b.setText(QCoreApplication.translate("TextureMange", u"\u9ad8\u5149", None))
        self.b_pushButton.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.label_15.setText(QCoreApplication.translate("TextureMange", u"\u9ed8\u8ba4\u52a0\u8f7d\u989c\u8272", None))
        self.default_b.setText(QCoreApplication.translate("TextureMange", u"#000000", None))
        self.label_16.setText(QCoreApplication.translate("TextureMange", u"\u5408\u5e76\u989c\u8272", None))
        self.merge_b_c.setText(QCoreApplication.translate("TextureMange", u"#808080", None))
        self.groupBox3.setTitle(QCoreApplication.translate("TextureMange", u"A", None))
        self.A.setText(QCoreApplication.translate("TextureMange", u"A\uff1a", None))
        self.mark_a.setText(QCoreApplication.translate("TextureMange", u"\u5916\u63cf\u8fb9", None))
        self.a_pushButton.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.label_19.setText(QCoreApplication.translate("TextureMange", u"\u9ed8\u8ba4\u52a0\u8f7d\u989c\u8272", None))
        self.default_a.setText(QCoreApplication.translate("TextureMange", u"#000000", None))
        self.label_20.setText(QCoreApplication.translate("TextureMange", u"\u5408\u5e76\u989c\u8272", None))
        self.merge_a_c.setText(QCoreApplication.translate("TextureMange", u"#808080", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TextureMange", u"TextureMerge", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TextureMange", u"More", None))
    # retranslateUi

