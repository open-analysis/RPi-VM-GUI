import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from gui import MainWindow, VMRibbonWidget, VMWidgetHolder, VMAudioSettingsMenu, buildMenu, buildAudioMenu
# from button_operations import home_menu_options, test_audio_out_options
from menu_options import *
from data import *

def start():
    app = QApplication(sys.argv)
    app.setStyleSheet(Path("style_sheet.qss").read_text())

    mainWin = MainWindow('Volume Mixer')
    widget_ribbon = VMRibbonWidget()
    widget_holder = VMWidgetHolder(widget_ribbon)

    mainWin.m_layout.addWidget(widget_holder)

    menu_home = buildMenu(opts_home, "Home")
    widget_holder.setHome(menu_home)

    menu_audio_out = buildMenu(opts_audio_out, "Audio Output")
    menu_home.setMenuItemWidget("Audio Out", menu_audio_out)

    menu_audio_out_device_options = buildAudioMenu(opts_audio_devices, "Output Devices")
    menu_audio_out.setMenuItemWidget("Set output", menu_audio_out_device_options)

    menu_audio_out.setMenuItemWidget("Audio options", VMAudioSettingsMenu(AudioDevice("Device"), "Device"))

    opts_audio_output_progs_with_settings = []
    audio_programs = []
    for opt in opts_audio_progs:
        tmp = AudioProgram(name=opt)
        audio_programs.append(tmp)
        opts_audio_output_progs_with_settings.append([opt, VMAudioSettingsMenu(tmp, opt)])
    menu_audio_out_program_options = buildAudioMenu(opts_audio_output_progs_with_settings, "Output Programs")
    menu_audio_out.setMenuItemWidget("Audio Mixer", menu_audio_out_program_options)

    sys.exit(app.exec())

if __name__ == "__main__":
    start()