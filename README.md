# Requirements
Set up the RPi with whatever's the default image

Update/Upgrade the Pi & make sure that Python3 is installed

## Setting up RPi GUI
https://learn.adafruit.com/adafruit-pitft-3-dot-5-touch-screen-for-raspberry-pi/easy-install-2

## Network config
Edit `/etc/dhcpcd.conf`  
Add the lines:
```
interface eth0
static ip_address=192.168.1.142/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```

## Python modules install
Edit `~/.bashrc` to include:
```
export PATH=$PATH:/usr/bin/qmake
```

Update the Pi and install the necessary modules for the scripts
(Still testing this [SO question/answer](https://stackoverflow.com/questions/75509805/installing-pyqt6-on-raspberry-pi))
```
sudo apt update
sudo apt upgrade -y
sudo apt full-upgrade -y
sudo apt auto-remove -y
# Unsure if this v is necessary
apt install ninja-build libfontconfig1-dev libdbus-1-dev libfreetype6-dev libicu-dev libinput-dev libxkbcommon-dev libsqlite3-dev libssl-dev libpng-dev libjpeg-dev libglib2.0-dev libgles2-mesa-dev libgbm-dev libdrm-dev libx11-dev libxcb1-dev libxext-dev libxi-dev libxcomposite-dev libxcursor-dev libxtst-dev libxrandr-dev libx11-xcb-dev libxext-dev libxfixes-dev libxi-dev libxrender-dev libxcb1-dev libxcb-glx0-dev libxcb-keysyms1-dev libxcb-image0-dev libxcb-shm0-dev libxcb-icccm4-dev libxcb-sync-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-randr0-dev libxcb-render-util0-dev libxcb-util0-dev libxcb-xinerama0-dev libxcb-xkb-dev libxkbcommon-dev libxkbcommon-x11-dev libxcb-xinput-dev
python3 -m pip install flask PyQt6
sudo reboot
```

## This project
Git clone this repo to a directory of your choosing but make note of it  
` git clone https://github.com/open-analysis/RPi-VM-GUI.git `

# Remove "Screen blanking"
NOT REQUIRED
Basically turn off the screen going dark
```bash
sudo raspi-config
```
Go to `Display Options` then `Screen Blanking`. Select `No`, save and exit `raspi-config`  
`sudo reboot`

You can also try, but I'm unsure if this will work
```bash
sudo xset -dpms
```

# Set GUI & server to start automatically

## Autostart 
` chmod 777 start.sh `  
Edit ` /etc/xdg/lxsession/LXDE-pi/autostart `  
Add line at the end:  
`@./path/to/repo/RPi-VM-GUI/start.sh`

# To run
If auostart doesn't work, just run `start.sh` in the directory of `RPi-VM-GUI`
