=========My GPS========
===install gpsd init settings===
sudo apt-get install gpsd gpsd-clients python-gps
sudo nano /ect/default/gpsd // change GPSD_OPTIONS = "/dev/ttyTHS1"
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket

nano /lib/systemd/system/gpsd.socket // config gpsd
sudo killall gpsd
================================

===Allow Nvidia Nano to access Serial===
systemctl stop nvgetty
systemctl disable nvgetty
sudo udevadm trigger
========================================
sudo reboot
========================================

sudo cat /dev/ttyTHS1

========================================

===visualize===

sudo gpsd /dev/ttyTHS1 -F /var/run/gpsd.sock
gpsmon

========================================

===help===

linked
https://forums.developer.nvidia.com/t/jetson-nano-python3-gps-problem/144304/3

python get gps data
https://brisbaneroboticsclub.id.au/install-ublox-m8n-gps-on-raspberry-pi-nvidia-nano/




=========end==============



sudo apt-get install gpsd gpsd-clients python-gps
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket


nano /lib/systemd/system/gpsd.socket

sudo killall gpsd




sudo gpsd /dev/ttyTHS1 -F /var/run/gpsd.sock ???


sudo nano /ect/default/gpsd
GPSD_OPTIONS = "/dev/ttyTHS1"



===========================================================


===Allow Nvidia Nano to access Serial===
systemctl stop nvgetty
systemctl disable nvgetty
sudo udevadm trigger
========================================

sudo reboot

========================================

sudo cat /dev/ttyTHS1

========================================

===visualize===

sudo gpsd /dev/ttyTHS1 -F /var/run/gpsd.sock
gpsmon

========================================

linked
https://forums.developer.nvidia.com/t/jetson-nano-python3-gps-problem/144304/3

python get gps data
https://brisbaneroboticsclub.id.au/install-ublox-m8n-gps-on-raspberry-pi-nvidia-nano/

===========================================================

serial port
https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-nvidia-jetson-nano/uart-serial


last test
http://throosea.com/wordpress/index.php/2015/12/22/raspberrypi-gps-install/
