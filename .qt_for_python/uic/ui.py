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
        TextureMange.resize(1398, 713)
        TextureMange.setMinimumSize(QSize(1398, 713))
        TextureMange.setMaximumSize(QSize(1398, 713))
        TextureMange.setAutoFillBackground(False)
        TextureMange.setStyleSheet(u"color:rgb(176, 190, 199);\n"
"background-color: rgb(25, 34, 46);\n"
"")
        self.tabWidget = QTabWidget(TextureMange)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(0, 0, 1441, 721))
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
"}\u200b")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
#if QT_CONFIG(statustip)
        self.tab.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.tab.setAutoFillBackground(False)
        self.tab.setStyleSheet(u"")
        self.show_box = QGroupBox(self.tab)
        self.show_box.setObjectName(u"show_box")
        self.show_box.setGeometry(QRect(700, 10, 691, 671))
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
        self.label_image = QLabel(self.show_box)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(20, 30, 651, 591))
        self.label_image.setScaledContents(False)
        self.label_image.setAlignment(Qt.AlignCenter)
        self.pngname_lineEdit = QLabel(self.show_box)
        self.pngname_lineEdit.setObjectName(u"pngname_lineEdit")
        self.pngname_lineEdit.setGeometry(QRect(230, 630, 221, 20))
        self.pngname_lineEdit.setStyleSheet(u"background-color: rgb(36, 49, 66);")
        self.pngname_lineEdit.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 10, 671, 81))
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
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
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


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_6.addItem(self.verticalSpacer_10)

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

        self.horizontalLayout_6.addWidget(self.out_Button)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(3, 1)
        self.horizontalLayout_6.setStretch(4, 5)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 520, 671, 161))
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
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_8 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

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

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalSpacer_9 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tex_json = QPushButton(self.groupBox)
        self.tex_json.setObjectName(u"tex_json")

        self.horizontalLayout_9.addWidget(self.tex_json)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_9.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

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


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.mergeButton = QPushButton(self.groupBox)
        self.mergeButton.setObjectName(u"mergeButton")
        self.mergeButton.setAutoDefault(False)

        self.verticalLayout_3.addWidget(self.mergeButton)

        self.RGBA = QGroupBox(self.tab)
        self.RGBA.setObjectName(u"RGBA")
        self.RGBA.setGeometry(QRect(20, 100, 671, 401))
        self.RGBA.setStyleSheet(u"QLineEdit { background-color: rgb(29, 56, 89) }\n"
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
        self.verticalLayout_2 = QVBoxLayout(self.RGBA)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.fast_Button = QPushButton(self.RGBA)
        self.fast_Button.setObjectName(u"fast_Button")

        self.verticalLayout_2.addWidget(self.fast_Button)

        self.mark_Button = QPushButton(self.RGBA)
        self.mark_Button.setObjectName(u"mark_Button")

        self.verticalLayout_2.addWidget(self.mark_Button)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.R = QLabel(self.RGBA)
        self.R.setObjectName(u"R")
        self.R.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_2.addWidget(self.R)

        self.mark_r = QLineEdit(self.RGBA)
        self.mark_r.setObjectName(u"mark_r")

        self.horizontalLayout_2.addWidget(self.mark_r)

        self.r_lineEdit = QLineEdit(self.RGBA)
        self.r_lineEdit.setObjectName(u"r_lineEdit")

        self.horizontalLayout_2.addWidget(self.r_lineEdit)

        self.r_pushButton = QPushButton(self.RGBA)
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

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.G = QLabel(self.RGBA)
        self.G.setObjectName(u"G")
        self.G.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_3.addWidget(self.G)

        self.mark_g = QLineEdit(self.RGBA)
        self.mark_g.setObjectName(u"mark_g")

        self.horizontalLayout_3.addWidget(self.mark_g)

        self.g_lineEdit = QLineEdit(self.RGBA)
        self.g_lineEdit.setObjectName(u"g_lineEdit")

        self.horizontalLayout_3.addWidget(self.g_lineEdit)

        self.g_pushButton = QPushButton(self.RGBA)
        self.g_pushButton.setObjectName(u"g_pushButton")

        self.horizontalLayout_3.addWidget(self.g_pushButton)

        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.RGBA)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.mark_b = QLineEdit(self.RGBA)
        self.mark_b.setObjectName(u"mark_b")

        self.horizontalLayout_4.addWidget(self.mark_b)

        self.b_lineEdit = QLineEdit(self.RGBA)
        self.b_lineEdit.setObjectName(u"b_lineEdit")

        self.horizontalLayout_4.addWidget(self.b_lineEdit)

        self.b_pushButton = QPushButton(self.RGBA)
        self.b_pushButton.setObjectName(u"b_pushButton")

        self.horizontalLayout_4.addWidget(self.b_pushButton)

        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_6 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.A = QLabel(self.RGBA)
        self.A.setObjectName(u"A")
        self.A.setCursor(QCursor(Qt.ArrowCursor))

        self.horizontalLayout_7.addWidget(self.A)

        self.mark_a = QLineEdit(self.RGBA)
        self.mark_a.setObjectName(u"mark_a")

        self.horizontalLayout_7.addWidget(self.mark_a)

        self.a_lineEdit = QLineEdit(self.RGBA)
        self.a_lineEdit.setObjectName(u"a_lineEdit")

        self.horizontalLayout_7.addWidget(self.a_lineEdit)

        self.a_pushButton = QPushButton(self.RGBA)
        self.a_pushButton.setObjectName(u"a_pushButton")

        self.horizontalLayout_7.addWidget(self.a_pushButton)

        self.horizontalLayout_7.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

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

        self.retranslateUi(TextureMange)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TextureMange)
    # setupUi

    def retranslateUi(self, TextureMange):
        TextureMange.setWindowTitle(QCoreApplication.translate("TextureMange", u"TextureManger_v1.0", None))
        self.show_box.setTitle(QCoreApplication.translate("TextureMange", u"\u9884\u89c8", None))
        self.label_image.setText(QCoreApplication.translate("TextureMange", u"image", None))
        self.pngname_lineEdit.setText(QCoreApplication.translate("TextureMange", u"name", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TextureMange", u"Psd", None))
        self.label.setText(QCoreApplication.translate("TextureMange", u"PSD", None))
        self.psd_Button.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.label_2.setText(QCoreApplication.translate("TextureMange", u"\u6ce8\uff1a\u9ed8\u8ba4PNG\u62c6\u5206\u5230psd\u76ee\u5f55\u4e2d", None))
        self.checkBox_4.setText(QCoreApplication.translate("TextureMange", u"\u6309\u7167\u6807\u7b7e\u62c6\u5206\u9700\u8981\u901a\u9053", None))
        self.checkBox.setText(QCoreApplication.translate("TextureMange", u"\u6807\u7b7e\u81ea\u52a8\u5bfc\u5165", None))
        self.out_Button.setText(QCoreApplication.translate("TextureMange", u"PSD\u5206\u89e3\u8f93\u51fa", None))
        self.groupBox.setTitle(QCoreApplication.translate("TextureMange", u"\u8f93\u51fa\u8bbe\u7f6e", None))
        self.coust_Button.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.checkBox_3.setText(QCoreApplication.translate("TextureMange", u"\u81ea\u5b9a\u4e49\u8def\u5f84\uff08\u5f00\u53d1\u4e2d\uff09", None))
        self.label_4.setText(QCoreApplication.translate("TextureMange", u"\u6ce8\uff1a\u9ed8\u8ba4G\u8d34\u56fe\u901a\u9053\u8def\u5f84", None))
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
        self.RGBA.setTitle(QCoreApplication.translate("TextureMange", u"RGBA", None))
        self.fast_Button.setText(QCoreApplication.translate("TextureMange", u"\u624b\u52a8\u9009\u62e9\u5feb\u901f\u5bfc\u5165(\u5f00\u53d1\u4e2d)", None))
        self.mark_Button.setText(QCoreApplication.translate("TextureMange", u"\u4fdd\u5b58\u6807\u7b7e\u540d\u79f0\u9884\u8bbe", None))
        self.R.setText(QCoreApplication.translate("TextureMange", u"R\uff1a", None))
        self.mark_r.setText(QCoreApplication.translate("TextureMange", u"\u91d1\u5c5e ", None))
        self.r_pushButton.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.G.setText(QCoreApplication.translate("TextureMange", u"G\uff1a", None))
        self.mark_g.setText(QCoreApplication.translate("TextureMange", u"\u5185\u63cf\u8fb9", None))
        self.g_pushButton.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.label_3.setText(QCoreApplication.translate("TextureMange", u"B\uff1a", None))
        self.mark_b.setText(QCoreApplication.translate("TextureMange", u"\u9ad8\u5149", None))
        self.b_pushButton.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.A.setText(QCoreApplication.translate("TextureMange", u"A\uff1a", None))
        self.mark_a.setText(QCoreApplication.translate("TextureMange", u"\u5916\u63cf\u8fb9", None))
        self.a_pushButton.setText(QCoreApplication.translate("TextureMange", u"........", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("TextureMange", u"TextureMerge", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("TextureMange", u"future", None))
    # retranslateUi

