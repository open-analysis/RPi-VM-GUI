# Requirements
Set up the RPi with whatever's the default image

Update/Upgrade the Pi & make sure that Python3 is installed

Setting up RPi GUI
https://learn.adafruit.com/adafruit-pitft-3-dot-5-touch-screen-for-raspberry-pi/easy-install-2

Edit `/etc/dhcpcd.conf`
Add the lines:
```
interface eth0
static ip_address=192.168.1.142/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```

`python3 -m pip install flask`

Git clone this repo to a directory of your choosing but make note of it
` git clone https://github.com/open-analysis/RPi-VM-GUI.git `

# Set GUI & Server to start automatically

## Autostart 
` chmod 777 start.sh ` 
Edit ` /etc/xdg/lxsession/LXDE-pi/autostart `
Add line at the end:
`@./path/to/repo/RPi-VM-GUI/start.sh`

# Run
If auostart doesn't work, just run `start.sh` in the directory of `RPi-VM-GUI`
