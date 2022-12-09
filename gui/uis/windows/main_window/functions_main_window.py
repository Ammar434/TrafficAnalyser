
from asyncio import sleep
import sys
import time
from services.integer_convert import binary_to_hex, hex_to_ascii, message_for_row
from PySide6 import QtCore, QtGui, QtWidgets, QtPrintSupport

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
from utils.constants import combo_box_initial_ip_dst, combo_box_initial_ip_src, combo_box_initial_protocol

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# FUNCTIONS


class MainFunctions():
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # SET MAIN WINDOW PAGES
    # ///////////////////////////////////////////////////////////////
    def set_page(self, page):
        self.ui.load_pages.pages.setCurrentWidget(page)

    # SET LEFT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_left_column_menu(
        self,
        menu,
        title,
        icon_path
    ):
        self.ui.left_column.menus.menus.setCurrentWidget(menu)
        self.ui.left_column.title_label.setText(title)
        self.ui.left_column.icon.set_icon(icon_path)

    # RETURN IF LEFT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def left_column_is_visible(self):
        width = self.ui.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # RETURN IF RIGHT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def right_column_is_visible(self):
        width = self.ui.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # SET RIGHT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_right_column_menu(self, menu):
        self.ui.right_column.menus.setCurrentWidget(menu)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_title_bar_btn(self, object_name):
        return self.ui.title_bar_frame.findChild(QPushButton, object_name)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_left_menu_btn(self, object_name):
        return self.ui.left_menu.findChild(QPushButton, object_name)

    # LEDT AND RIGHT COLUMNS / SHOW / HIDE
    # ///////////////////////////////////////////////////////////////
    def toggle_left_column(self):
        # GET ACTUAL CLUMNS SIZE
        width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(
            self, width, right_column_width, "left")

    def toggle_right_column(self):
        # GET ACTUAL CLUMNS SIZE
        left_column_width = self.ui.left_column_frame.width()
        width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(
            self, left_column_width, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0
        time_animation = self.ui.settings["time_animation"]
        minimum_left = self.ui.settings["left_column_size"]["minimum"]
        maximum_left = self.ui.settings["left_column_size"]["maximum"]
        minimum_right = self.ui.settings["right_column_size"]["minimum"]
        maximum_right = self.ui.settings["right_column_size"]["maximum"]

        # Check Left Values
        if left_box_width == minimum_left and direction == "left":
            left_width = maximum_left
        else:
            left_width = minimum_left

        # Check Right values
        if right_box_width == minimum_right and direction == "right":
            right_width = maximum_right
        else:
            right_width = minimum_right

        # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(
            self.ui.left_column_frame, b"minimumWidth")
        self.left_box.setDuration(time_animation)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(
            self.ui.right_column_frame, b"minimumWidth")
        self.right_box.setDuration(time_animation)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.stop()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    def reset_combo_box(self):
        self.ui.load_pages.comboBox.clear()
        self.ui.load_pages.comboBox_2.clear()
        self.ui.load_pages.comboBox_3.clear()
        listeIp = (self.printerMethod.listeIp)
        listeProtocol = (self.printerMethod.listeProtocol)

        self.ui.load_pages.comboBox.addItem(combo_box_initial_protocol)
        self.ui.load_pages.comboBox_2.addItem(combo_box_initial_ip_dst)
        self.ui.load_pages.comboBox_3.addItem(combo_box_initial_ip_src)

        self.ui.load_pages.comboBox.addItems(listeProtocol)
        self.ui.load_pages.comboBox_2.addItems(listeIp)
        self.ui.load_pages.comboBox_3.addItems(listeIp)

    def display_loading(self, ):

        self.circular_progress_1 = PyCircularProgress(
            value=0,
            progress_color=self.themes["app_color"]["context_color"],
            text_color=self.themes["app_color"]["text_title"],
            font_size=14,
            bg_color=self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_1.setFixedSize(200, 200)

        self.ui.load_pages.row_for_tab.addWidget(
            self.circular_progress_1)
        self.ui.load_pages.row_for_tab.setAlignment(Qt.AlignHCenter)

    def clear_screen(self):
        count = self.ui.load_pages.row_for_tab.count()
        if count == 0:
            return
        item = self.ui.load_pages.row_for_tab.itemAt(count - 1)
        widget = item.widget()
        widget.deleteLater()

    def update_table(self, listeDecodedTrame, filePath):
        # print("len avant creation table  "+str(len(listeDecodedTrame)))

        self.table_widget = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(1)
        self.table_widget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)

        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setShowGrid(False)

        tmp = QTableWidgetItem()
        tmp.setTextAlignment(Qt.AlignCenter)
        tmp.setText("Visualisation de la trame:  " + filePath)
        self.table_widget.setHorizontalHeaderItem(0, tmp)
        self.table_widget.setColumnWidth(0, 1000)

        for count, trame in enumerate(listeDecodedTrame):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number)

            messageToInsert_1, color = message_for_row(trame)

            # Insert row
            self.table_widget.setItem(
                row_number, 0, QTableWidgetItem(messageToInsert_1))
            self.table_widget.item(
                row_number, 0).setTextAlignment(Qt.AlignCenter)

            self.table_widget.item(
                row_number, 0).setForeground(QBrush(color))

            self.table_widget.setRowHeight(row_number, 100)

        self.ui.load_pages.row_for_tab.addWidget(self.table_widget)

    def export_to_pdf(self):
        w = self.table_widget

        filename = "table.pdf"
        model = w.model()

        printer = QtPrintSupport.QPrinter(
            QtPrintSupport.QPrinter.PrinterResolution)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setPageSize(QPageSize.PageSizeId.A4)
        printer.setPageOrientation(QPageLayout.Orientation.Landscape)
        printer.setOutputFileName(filename)

        doc = QtGui.QTextDocument()
        doc.setDefaultStyleSheet(f'''
          background-color:blue;color: lightgray; border: 1px solid black; border-radius:10px;font: bold
        ''')
        html = """<html>
        <head>
        <style>
        table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        }
        </style>
        </head>"""
        html += "<table><thead>"
        html += "<tr>"
        for c in range(model.columnCount()):
            html += "<th>{}</th>".format(model.headerData(c,
                                         QtCore.Qt.Horizontal))

        html += "</tr></thead>"
        html += "<tbody>"
        for r in range(model.rowCount()):
            html += "<tr>"
            for c in range(model.columnCount()):
                html += "<td>{}</td>".format(model.index(r, c).data() or "")
            html += "</tr>"
        html += "</tbody></table>"
        doc.setHtml(html)

        # doc.setPageSize(QtCore.QSizeF(printer.pageRect().size()))
        doc.print_(printer)
