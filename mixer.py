#! /usr/bin/env python3

import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from gui import MainWindow, VMRibbonWidget, VMWidgetHolder, VMAudioSettingsMenu, buildMenu, buildAudioMenu#, buildDynamicMenu
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

    audio_list = []
    for opt in opts_audio_devices:
        audio_list.append(VMAudioSettingsMenu(opt, opt.getName()))

    menu_audio_out_device_options = buildAudioMenu(audio_list, "Output Devices")
    menu_audio_out.setMenuItemWidget("Set output", menu_audio_out_device_options)

    override_item = menu_audio_out.getMenuItem("Set output")
    override_item.overrideClicked(override_item.overrideClickedOutput)

    menu_audio_out.setMenuItemWidget("Audio options", VMAudioSettingsMenu(AudioDevice("Device"), "Device"))

    audio_list = []
    for opt in opts_audio_progs:
        audio_list.append(VMAudioSettingsMenu(opt, opt.getName()))

    menu_audio_out_program_options = buildAudioMenu(audio_list, "Output Programs")
    menu_audio_out.setMenuItemWidget("Audio Mixer", menu_audio_out_program_options)
    
    override_item = menu_audio_out.getMenuItem("Audio Mixer")
    override_item.overrideClicked(override_item.overrideClickedMixer)

    sys.exit(app.exec())