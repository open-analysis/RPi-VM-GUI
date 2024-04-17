from math import floor, sqrt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QSlider
from menu_options import opts_audio_devices, opts_audio_progs

class MainWindow(QWidget):
    m_layout = QVBoxLayout()

    def __init__(self, title: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle(title)

        # self.setGeometry(0,0, 700, 440)
        self.setFixedWidth(700)
        self.setFixedHeight(450)

        self.setLayout(self.m_layout)

        # show the window
        self.show()

class VMWidget(QWidget):
    m_layout = None
    m_name = ""

    def __init__(self, name="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.m_name = name

    def setVMLayout(self, layout):
        self.m_layout = layout
        self.setLayout(self.m_layout)

    def addVMWidget(self, widget):
        self.m_layout.addWidget(widget)

    def removeVMWidget(self, widget):
        self.m_layout.removeWidget(widget)

    def deleteSelf(self):
        self.parentWidget().deleteChildWidget(self)

    def deleteChildWidget(self, child_widget):
        self.removeVMWidget(child_widget)
        child_widget.deleteLater()

class VMRibbonWidget(VMWidget):
    m_label_title = None

    def __init__(self, *args, **kwargs):
        super().__init__("Ribbon", *args, **kwargs)

        self.m_layout = QHBoxLayout()
        self.setLayout(self.m_layout)

        button_back = QPushButton("Back", clicked=self.clicked_back)
        button_home = QPushButton("Home", clicked=self.clicked_home)
        self.m_label_title = QLabel("NA")

        self.m_layout.addWidget(button_back)
        self.m_layout.addStretch()
        self.m_layout.addWidget(self.m_label_title)
        self.m_layout.addStretch()
        self.m_layout.addWidget(button_home)

    def setRibbonTitle(self, title:str):
        self.m_label_title.setText(title)

    def clicked_back(self):
        self.parentWidget().popWidget()

    def clicked_home(self):
        self.parentWidget().returnHome()

class VMWidgetHolder(VMWidget):
    m_prev_widgets = []
    m_ribbon_widget = None
    m_home_widget = None
    m_current_widget = None

    def __init__(self, ribbon_widget, name="", *args, **kwargs) -> None:
        super().__init__("Widget Holder", *args, **kwargs)
        self.m_ribbon_widget = ribbon_widget

        self.setVMLayout(QVBoxLayout())

        self.m_layout.addWidget(self.m_ribbon_widget)

    def setRibbon(self, ribbon_widget) -> None:
        self.m_ribbon_widget = ribbon_widget

    def setHome(self, home_widget) -> None:
        self.m_home_widget = home_widget
        self.setCurrentWidget(home_widget)

    def appendPrevWidget(self, widget) -> None:
        self.m_prev_widgets.append(widget)

    def setCurrentWidget(self, widget, newWidget=True) -> None:
        self.m_current_widget = widget
        self.m_ribbon_widget.setRibbonTitle(widget.m_name)
        if newWidget:
            self.addVMWidget(widget)
        else:
            widget.show()

    def returnHome(self) -> None:
        if not self.m_home_widget or self.m_current_widget == self.m_home_widget:
            return

        self.m_current_widget.hide()
        self.removeVMWidget(self.m_current_widget)
        self.setCurrentWidget(self.m_home_widget, newWidget=False)
        # self.m_current_widget = self.m_home_widget
        # self.m_home_widget.show()
    
    def popWidget(self) -> None:
        widget = None
        try:
            widget = self.m_prev_widgets.pop()
        except Exception as err:
            print("List of previous widgets is empty")
            return

        self.m_current_widget.hide()
        self.removeVMWidget(self.m_current_widget)
        # self.m_current_widget.deleteSelf()
        self.setCurrentWidget(widget, newWidget=False)
        # self.m_current_widget = widget
        # widget.show()

class VMButtonWidget(VMWidget):
    m_button = None

    def __init__(self, name="", *args, **kwargs):
        super().__init__(name, *args, **kwargs)

class VMMenu(VMWidget):
    m_menu_items = []

    def __init__(self, name="", *args, **kwargs):
        super().__init__(name, *args, **kwargs)

        self.setVMLayout(QGridLayout())

    def addMenuItemWidget(self, widget, row: int, col: int):
        self.appendMenuWidget(widget, row, col)

    def appendMenuWidget(self, widget:VMWidget, row: int, col: int):
        self.m_layout.addWidget(widget, row, col, Qt.AlignmentFlag.AlignRight)
        self.m_menu_items.append(widget)

    def getMenuItem(self, name:str) -> VMWidget:
        for item in self.m_menu_items:
            if name == item.m_name:
                return item

        return None

    def setMenuItemWidget(self, name:str, widget:VMWidget) -> None:
        item = self.getMenuItem(name)
        item.setNextWidget(widget)

class VMMenuItem(VMButtonWidget):
    m_next_widget = None

    def __init__(self, name="Item", *args, **kwargs):
        super().__init__(name, *args, **kwargs)

        self.m_layout = QHBoxLayout()
        self.setLayout(self.m_layout)

        self.m_name = name
        self.m_button = QPushButton(name, clicked=self.menuItemClicked)
        self.m_layout.addWidget(self.m_button)

    def setButtonText(self, title:str):
        self.m_button.setText(title)

    def setNextWidget(self, widget):
        self.m_next_widget = widget

    def getButtonText(self) -> str:
        return self.m_button.text()

    def menuItemClicked(self):
        parent = self.parentWidget()
        if self.m_next_widget is None:
            return
        parent.parentWidget().appendPrevWidget(parent)
        parent.parentWidget().setCurrentWidget(self.m_next_widget)
        self.m_next_widget.show()

        parent.hide()

    def overrideClicked(self, func):
        self.m_button.clicked.connect(func)
        
    def overrideClickedOutput(self):        
        parent = self.parentWidget()
        
        audio_devices = []
        for opt in opts_audio_devices:
            with open("out.txt", "a") as w:
                w.write(f"Override output {opt.getName()}\n")    
            audio_devices.append(VMAudioSettingsMenu(opt, opt.getName()))
        with open("out.txt", "a") as w:
            w.write(f"\n")    
        self.m_next_widget = buildAudioMenu(audio_devices, "Output Devices")
        
        parent.parentWidget().appendPrevWidget(parent)
        parent.parentWidget().setCurrentWidget(self.m_next_widget)
        self.m_next_widget.show()

        parent.hide()

    def overrideClickedMixer(self):
        parent = self.parentWidget()

        audio_programs = []
        for opt in opts_audio_progs:
            audio_programs.append(VMAudioSettingsMenu(opt, opt.getName()))
        self.m_next_widget = buildAudioMenu(audio_programs, "Output Programs")

        parent.parentWidget().appendPrevWidget(parent)
        parent.parentWidget().setCurrentWidget(self.m_next_widget)
        self.m_next_widget.show()

        parent.hide()
    
class VMAudioSettingsMenu(VMMenu):
    from data import Audio 
    m_audio_program = None

    m_opts_audio_output_settings = ["Volume",
                                    "Mute"]

    def __init__(self, audio_program, name, *args, **kwargs):
        super().__init__(name, *args, **kwargs)

        self.m_audio_program = audio_program
        
        # Set Volume slider option
        menu_item = VMMenuItem(self.m_opts_audio_output_settings[0])
        menu_item.setButtonText(self.m_opts_audio_output_settings[0])
        menu_item.setNextWidget(VMVolumeSlider(self.m_audio_program, self.m_opts_audio_output_settings[0]))
        self.addMenuItemWidget(menu_item, 0, 0)
        
        # Set Toggle mute option
        menu_item = VMMenuItem(self.m_opts_audio_output_settings[1])
        menu_item.setButtonText(self.m_opts_audio_output_settings[1])
        menu_item.m_button.setCheckable(True)
        menu_item.m_button.setChecked(self.m_audio_program.getMute())
        menu_item.m_button.clicked.connect(self.m_audio_program.setMute)
        self.addMenuItemWidget(menu_item, 0, 1)

    def updateAudioSettingsName(self, name:str):
        self.m_name = f"Audio Settings | {name}"
        return self
    
    def setAudioSettingsName(self, name:str):
        self.m_name = f"Audio Settings | {name}"

    def setAudioProgram(self, audio_program):
        self.m_audio_program = audio_program

class VMVolumeSlider(VMWidget):
    m_audio_program = None
    m_slider = None
    m_label = None

    def __init__(self, audio_prog, name, *args, **kwargs):
        super().__init__(f"Volumer Slider | {name}", *args, **kwargs)
        self.m_audio_program = audio_prog
        self.m_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.m_slider.setRange(0, 100)
        self.m_slider.setSingleStep(2)
        self.m_slider.setValue(self.m_audio_program.getVolume())
        
        self.m_label = QLabel(f"Volume: {self.m_slider.value()}")
        
        self.m_slider.valueChanged.connect(self.update)

        self.setVMLayout(QVBoxLayout())

        self.m_layout.addWidget(self.m_slider)
        self.m_layout.addWidget(self.m_label)

    def update(self, value):
        self.m_audio_program.setVolume(value)
        self.m_label.setText(f"Volume: {value}")

    def setVolumerSliderName(self, name:str):
        self.m_name = f"Volumer Slider | {name}"

    def setVolumeSliderValue(self):
        pass

def buildMenu(menu_items:list, name:str):
    max_col = 3
    
    if len(menu_items) > 20:
        max_col = floor(sqrt(len(menu_items)))

    menu = VMMenu(name)
    row = 0
    col = 0

    for item in menu_items:
        menu_item = VMMenuItem(item)
        menu_item.setButtonText(item)

        menu.addMenuItemWidget(menu_item, row, col)
        
        col += 1
        if col > max_col:
            col = 0
            row += 1

    return menu

def buildAudioMenu(menu_items:list, name:str):
    max_col = 3

    if len(menu_items) > 10:
        max_col = floor(sqrt(len(menu_items)))

    menu = VMMenu(name)
    row = 0
    col = 0

    for item in menu_items:
        with open("out.txt", "a") as w:
            w.write(f"Item {item.m_name}\n")    
        menu_item = VMMenuItem(item.m_name) 
        menu_item.setButtonText(item.m_name)
        menu_item.setNextWidget(item)

        menu.addMenuItemWidget(menu_item, row, col)
        
        col += 1
        if col > max_col:
            col = 0
            row += 1

    return menu
