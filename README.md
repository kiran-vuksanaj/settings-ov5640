### Configuration File generator for OV5640
Used in MIT's 6.205, Digital Systems Laboratory

### Usage
```
cd mem_generator
python3 reglist.py rom > rom.mem
```

This will fill rom.mem with a 24-bit wide, 256-bit deep `.mem` file that can be used for configuring the OV5640 camera on startup.

**TO MAKE ALTERNATIVE CONFIGURATIONS**: modify the settings set in the reglist.py `PART 1` section, to whichever modes you desire. Look through the `adafruit_ov5640.py` file to see what options are available.

For use in the 6.205 framework, these files will work as a drop-in replacement for the default `rom.mem` files we provide you to configure the camera.

The files are formatted such that the first 16 bits (4 hex digits) of each line specify a camera register to set, and the last 8 bits (2 hex digits) specify the value it should take.

### What's going on here?

At startup, the OV5640 needs a sequence of registers to be set over its I2C (SCCB, technically--see datasheet) bus; the drivers implemented in various microcontroller systems specify a sequence that works to get the camera running. This repo has a modified version of a few different drivers mushed together that seems to give good results for getting the camera running nicely in the architecture we've been using in 6.205. Instead of actually configuring the camera, it just prints out each command it would have sent in a good format to stick into a BRAM initialization file (see above for format) so we can go use

The base code provided for lab in weeks 05-07 expect a `rom.mem` formatted the way that this script produces them. You can also use the data from these files to set up alternate ways of configuring the camera, if you happen to need to dynamically reconfigure the camera or anything like that.


**NOTE**: by default this generates a ROM file that is 256 entries deep; you might need to make that longer depending on what camera settings you set. Mess with `reglist.py` as appropriate to make that happen.

### References

If just making plain changes to these files isn't enough to get your alternative modes working, definitely look to these sources.
* [OV5640 Datasheet](https://cdn.sparkfun.com/datasheets/Sensors/LightImaging/OV5640_datasheet.pdf)
* [Adafruit Driver for OV5640 in CircuitPython](https://github.com/adafruit/Adafruit_CircuitPython_OV5640/tree/main/adafruit_ov5640)
* [STM Driver for OV5640](https://github.com/STMicroelectronics/stm32-ov5640)
* [Drivers for cameras on ESP32, including OV5640](https://github.com/espressif/esp32-camera)


Kiran is generally happy to answer questions in office hours or over email ([firstname] [last initial] at [mit.edu]) !
