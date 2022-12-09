
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
from models.protocol import Protocol
from models.printer_method import PrinterMethod
from utils.dynamic_value import listeIp

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *
from services.decode_trame import DecodeTrame
from services.integer_convert import binary_to_ip_dotted
from services.trame_reader import TrameReader
from utils.constants import SUCCESS
from utils.pdf_maker import PDF, print_to_pdf



# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP PROTOCOL
        # Load protocol from "models\data"
        # ///////////////////////////////////////////////////////////////
        res = Protocol.loadAllProtocol()
        if res != SUCCESS:
            print("All protocol not load correctly")
            return

        self.trameReader = TrameReader()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP PDF
        # ///////////////////////////////////////////////////////////////

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        self.printerMethod = PrinterMethod()
        self.path = ""
        self.src = str(combo_box_initial_ip_src)
        self.dst = str(combo_box_initial_ip_dst)
        self.pro = str(combo_box_initial_protocol)

    # SHOW MAIN WINDOW
    # ///////////////////////////////////////////////////////////////
        self.show()
    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////

    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # WIDGETS BTN
        if btn.objectName() == "btn_open_file":
            self.path = QFileDialog.getOpenFileNames()[0][0]
            if self.path != "":
                self.printerMethod.clearAll()
                MainFunctions.clear_screen(self)
                MainFunctions.display_loading(self)



                listeTrame = self.trameReader.createTramesList(self.path)
                self.printerMethod.listeDecodedTrame = DecodeTrame().decodeAllTrame(listeTrame)
                self.printerMethod.displayThroughCriteria(
                    self.src, self.dst, self.pro)

                for trame in self.printerMethod.listeDecodedTrame:
                    if trame != None and trame.all_protocol_inside[3] != None:
                        for field in trame.all_protocol_inside[3].fields:
                            if field.id == "srcIpAddress" or field.id == "dstIpAddress":
                                newIp = binary_to_ip_dotted(field.content)
                                if newIp not in self.printerMethod.listeIp:
                                    self.printerMethod.listeIp.append(
                                        binary_to_ip_dotted(field.content))

                for trame in self.printerMethod.listeDecodedTrame:
                    if trame != None:
                        np = None
                        for key, val in trame.all_protocol_inside.items():
                            if val != None:
                                np = val
                        if np.name not in self.printerMethod.listeProtocol:
                            self.printerMethod.listeProtocol.append(
                                np.name)

                MainFunctions.reset_combo_box(self)
                MainFunctions.clear_screen(self)
                MainFunctions.update_table(
                    self, self.printerMethod.displayList, self.path)
        # print(listeIp)
        # LOAD USER PAGE
        if btn.objectName() == "btn_save":
            print_to_pdf(self.printerMethod.displayList, self.path)

        if btn.objectName() == "btn_info":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="Information",
                    icon_path=Functions.set_svg_icon("icon_info.svg")
                )

        # SETTINGS LEFT
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////

        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn
            top_settings = MainFunctions.get_left_menu_btn(
                self, "btn_settings")
            top_settings.set_active_tab(False)

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    def activated_1(self, index):
        # MainFunctions.clear_screen(self)
        print("Activated index:", index)

    def text_changed_1(self, s):
        self.pro = s
        MainFunctions.clear_screen(self)
        self.printerMethod.displayThroughCriteria(
            self.src, self.dst, self.pro)
        MainFunctions.update_table(
            self, self.printerMethod.displayList, self.path)

    def index_changed_1(self, index):
        pass

    def activated_2(self, index):
        pass

    def text_changed_2(self, s):
        self.dst = s
        MainFunctions.clear_screen(self)
        self.printerMethod.displayThroughCriteria(
            self.src, self.dst, self.pro)
        MainFunctions.update_table(
            self, self.printerMethod.displayList, self.path)

    def index_changed_2(self, index):
        pass

    def activated_3(self, index):

        pass

    def text_changed_3(self, s):
        # print("Text changed:", self.src)
        self.src = s
        MainFunctions.clear_screen(self)
        self.printerMethod.displayThroughCriteria(
            self.src, self.dst, self.pro)
        MainFunctions.update_table(
            self, self.printerMethod.displayList, self.path)

    def index_changed_3(self, index):

        pass

        # RESIZE EVENT
        # ///////////////////////////////////////////////////////////////

    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()


# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())
