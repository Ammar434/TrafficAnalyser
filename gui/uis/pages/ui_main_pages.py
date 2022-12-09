# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_pagesTKySkt.ui'
##
# Created by: Qt User Interface Compiler version 6.4.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                               QLabel, QLayout, QScrollArea, QSizePolicy,
                               QStackedWidget, QVBoxLayout, QWidget)


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt;")
        self.verticalLayout_2 = QVBoxLayout(self.page_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background: transparent;")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.contents_2 = QWidget()
        self.contents_2.setObjectName(u"contents_2")
        self.contents_2.setGeometry(QRect(0, 0, 840, 580))
        self.contents_2.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.contents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title_label_2 = QLabel(self.contents_2)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label_2.setFont(font)
        self.title_label_2.setStyleSheet(u"font-size: 16pt")
        self.title_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.title_label_2)

        self.description_label_2 = QLabel(self.contents_2)
        self.description_label_2.setObjectName(u"description_label_2")
        self.description_label_2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.description_label_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.description_label_2)

        self.row_for_tab = QVBoxLayout()
        self.row_for_tab.setObjectName(u"row_for_tab")

        self.verticalLayout_4.addLayout(self.row_for_tab)
        self.horizontalLayout_ForComboBox = QHBoxLayout()
        self.horizontalLayout_ForComboBox.setObjectName(
            u"horizontalLayout_ForComboBox")
        self.comboBox_3 = QComboBox(self.contents_2)
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"QComboBox{\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "	border-radius: 20px;\n"
                                      "	border: 2px solid rgb(52, 59, 72);\n"
                                      "	padding: 5px;\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox::drop-down {\n"
                                      "	subcontrol-origin: padding;\n"
                                      "	subcontrol-position: top right;\n"
                                      "	width: 25px; \n"
                                      "	border-left-width: 3px;\n"
                                      "	border-left-color: rgba(39, 44, 54, 150);\n"
                                      "	border-left-style: solid;\n"
                                      "	border-top-right-radius: 3px;\n"
                                      "	border-bottom-right-radius: 3px;	\n"
                                      "	background-image: url(:\gui\images\svg_icons\arrow_down.ico);\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-reperat;\n"
                                      " }\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "	color: rgb(255, 121, 198);	\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	padding: 10px;\n"
                                      "	selection-background-color: rgb(39, 44, 54);\n"
                                      "}")

        self.horizontalLayout_ForComboBox.addWidget(self.comboBox_3)

        self.comboBox_2 = QComboBox(self.contents_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
                                      "	background-color: rgb(52, 59, 72);\n"
                                      "	border-radius: 20px;\n"
                                      "	border: 2px solid rgb(52, 59, 72);\n"
                                      "	padding: 5px;\n"
                                      "	padding-left: 10px;\n"
                                      "}\n"
                                      "QComboBox:hover{\n"
                                      "	border: 2px solid rgb(64, 71, 88);\n"
                                      "}\n"
                                      "QComboBox::drop-down {\n"
                                      "	subcontrol-origin: padding;\n"
                                      "	subcontrol-position: top right;\n"
                                      "	width: 25px; \n"
                                      "	border-left-width: 3px;\n"
                                      "	border-left-color: rgba(39, 44, 54, 150);\n"
                                      "	border-left-style: solid;\n"
                                      "	border-top-right-radius: 3px;\n"
                                      "	border-bottom-right-radius: 3px;	\n"
                                      "	background-image: url(:\gui\images\svg_icons\arrow_down.ico);\n"
                                      "	background-position: center;\n"
                                      "	background-repeat: no-reperat;\n"
                                      " }\n"
                                      "QComboBox QAbstractItemView {\n"
                                      "	color: rgb(255, 121, 198);	\n"
                                      "	background-color: rgb(33, 37, 43);\n"
                                      "	padding: 10px;\n"
                                      "	selection-background-color: rgb(39, 44, 54);\n"
                                      "}")

        self.horizontalLayout_ForComboBox.addWidget(self.comboBox_2)

        self.comboBox = QComboBox(self.contents_2)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox{\n"
                                    "	background-color: rgb(52, 59, 72);\n"
                                    "	border-radius: 20px;\n"
                                    "	border: 2px solid rgb(52, 59, 72);\n"
                                    "	padding: 5px;\n"
                                    "	padding-left: 10px;\n"
                                    "}\n"
                                    "QComboBox:hover{\n"
                                    "	border: 2px solid rgb(64, 71, 88);\n"
                                    "}\n"
                                    "QComboBox::drop-down {\n"
                                    "	subcontrol-origin: padding;\n"
                                    "	subcontrol-position: top right;\n"
                                    "	width: 25px; \n"
                                    "	border-left-width: 3px;\n"
                                    "	border-left-color: rgba(39, 44, 54, 150);\n"
                                    "	border-left-style: solid;\n"
                                    "	border-top-right-radius: 3px;\n"
                                    "	border-bottom-right-radius: 3px;	\n"
                                    "	background-image: url(:\gui\images\svg_icons\arrow_down.ico);\n"
                                    "	background-position: center;\n"
                                    "	background-repeat: no-reperat;\n"
                                    " }\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "	color: rgb(255, 121, 198);	\n"
                                    "	background-color: rgb(33, 37, 43);\n"
                                    "	padding: 10px;\n"
                                    "	selection-background-color: rgb(39, 44, 54);\n"
                                    "}")

        self.horizontalLayout_ForComboBox.addWidget(self.comboBox)

        self.verticalLayout_4.addLayout(self.horizontalLayout_ForComboBox)

        self.scrollArea.setWidget(self.contents_2)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 215, 266))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
                                  "	font-size: 16pt;\n"
                                  "}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        self.empty_page_label.setFont(font)
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)

        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(
            QCoreApplication.translate("MainPages", u"Form", None))
        self.title_label_2.setText(QCoreApplication.translate(
            "MainPages", u"Visualisateur de traffic r\u00e9seau", None))
        self.description_label_2.setText(QCoreApplication.translate("MainPages", u"Ici, appara\u00eetra le trafic r\u00e9seau correspondant \u00e0 une trame.\n"
                                                                    "Pour commencer \u00e0 analyser une trame, il faut la s\u00e9lectionner dans le menu \u00e0 votre gauche.\n"
                                                                    "Si besoin, vous pouvez filtrer la trame affich\u00e9e selon quelques crit\u00e8res.\n"
                                                                    "\n"
                                                                    "", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate(
            "MainPages", u"Display all source IP", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate(
            "MainPages", u"Display all dest IP", None))

        self.comboBox.setItemText(0, QCoreApplication.translate(
            "MainPages", u"Display all protocol", None))

        self.title_label.setText(QCoreApplication.translate(
            "MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
                                                                  "I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        self.empty_page_label.setText(
            QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi
