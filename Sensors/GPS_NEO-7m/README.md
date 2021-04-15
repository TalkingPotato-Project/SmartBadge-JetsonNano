# My GPS Control


## Install gpsd and Init settings

```bash
sudo apt-get install gpsd gpsd-clients python-gps 
sudo nano /ect/default/gpsd     # change GPSD_OPTIONS = "/dev/ttyTHS1" 
sudo systemctl stop gpsd.socket 
sudo systemctl disable gpsd.socket'
```

```bash
nano /lib/systemd/system/gpsd.socket // config gpsd # If you want change gpsd Network
sudo killall gpsd 
```

## Allow Jetson Nano to access Serial

```bash
systemctl stop nvgetty
systemctl disable nvgetty
sudo udevadm trigger
```

```bash
sudo reboot
```

## Check Data Stream
```bash
sudo cat /dev/ttyTHS1
```
## Run gpsd
```bash
sudo gpsd /dev/ttyTHS1 -F /var/run/gpsd.sock
gpsmon
```


## Reference Website

https://brisbaneroboticsclub.id.au/install-ublox-m8n-gps-on-raspberry-pi-nvidia-nano/ <br>
https://forums.developer.nvidia.com/t/jetson-nano-python3-gps-problem/144304

**circuitpython - GPS** 
https://learn.adafruit.com/circuitpython-libraries-on-linux-and-the-nvidia-jetson-nano/uart-serial
