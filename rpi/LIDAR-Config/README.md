# TF-MINI-Plus LIDAR interfacing with RPi 3
## Required components:

1. Raspberry Pi
2. Jumper Wires

## Steps for connection:

1. Connect Red wire of TFMini Lidar with raspberry pi `pin 2 (5v)*`.
2. Connect Black wire of TFMini Lidar with raspberry pi `pin 6 (GND)*`.
3. Connect WHITE wire of TFMini Lidar with raspberry pi `pin 8 (GPIO 14)*`.
4. Connect Green wire of TFMini Lidar with raspberry pi `pin 10 (GPIO 15)*`.

## PIN Layout

|  TFMini Pinout     |   Raspberry Pi Pinout|
|--------------------|----------------------|
|    Red             |        5V(Pin 2)     |
|    Black           |       GND(Pin 6)     | 
|    White           |       GPIO 14(Pin 8) |
|    Green           |       GPIO 15(Pin10) |
   
        
        
## Command line procedure:
1. `sudo nano lidar_tfmini.py`
2. `ls`
3. `sudo python lidar_tfmini.py`
