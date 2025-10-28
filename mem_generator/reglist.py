import adafruit_ov5640
# from manta import Manta
import time
import sys

# PART 1
# simulate writes to camera, according to adafruit library (with modifications by kiran)
# NB: MAKE EDITS HERE IN ORDER TO PUT THE CAMERA INTO NEW MODES!
# reference the modified adafruit_ov5640.py file for all available options.

# size: different modes will give you different camera resolutions
cam = adafruit_ov5640.OV5640(size=adafruit_ov5640.OV5640_SIZE_HD)

# Colorspace: OV5640_COLOR_RGB makes the camera spit out RGB565 (familiar format for 6.205)
# other options can be used to get YUV, or only Y channels
# changing the data format may require you to update your pixel_reconstruct module!

cam.colorspace = adafruit_ov5640.OV5640_COLOR_RGB

# flip horizontal/vertical feed
cam.flip_y = False
cam.flip_x = True

# cam.white_balance = adafruit_ov5640.OV5640_WHITE_BALANCE_AUTO

cam.test_pattern = False

# PLL configuration: I wouldn't recommend messing with this

# cam._set_pll(False, 20, 1, 1, False, 1, True,4)
# cam._set_pll(False,32,1,2,False,1,True,2)
# cam._write_addr_reg(0x3816,320,40)


# No need to make edits below here. This will print out the list of register-setting commands you need.

byte_list = [ ((regval[0]<<8) + regval[1]) for regval in cam._writes ]

while (len(byte_list) < 256):
    byte_list.append(0)


# PART 2    
# write the register sequence in the mode specified
modes = ["rom","manta","arduino"]
if ( len(sys.argv) < 2 or not sys.argv[1] in modes ):
    print("usage: python3 reglist.py ["+"|".join(modes)+"]")
else:
    mode = sys.argv[1]
    if mode == "rom":
        ### ROM Mode
        print("\n".join([format(regval,'06x') for regval in byte_list]))
    elif mode == "manta":
        #### Manta Mode
        print("manta mode doesn't currently work, needs to update for current version of manta")
        # m = Manta('../manta/camprobe.yaml')
        # m = Manta.from_config("../manta/camprobe.yaml")
        # addrs_a = list(range(0,len(byte_list)*2,2))
        # addrs_b = list(range(1,len(byte_list)*2,2))

        # m.cores.register_sequence.write(addrs_a, [ val&0xFFFF for val in byte_list ])
        # m.cores.register_sequence.write(addrs_b, [ val>>16 for val in byte_list ])
        
        # manta_list = m.cores.register_sequence.read( list(range(0,len(byte_list)*2)) )

        # m.cores.register_sequence.write( list(range(len(byte_list))), byte_list )

        # time.sleep(2)

        # manta_list = m.cores.register_sequence.read( list(range(256)) )
        
        # print("manta contents")
        # print([format(regval,'04x') for regval in manta_list])
    elif mode == "arduino":
        ### Arduino Mode
        print("reg_data settings_exp[] = {")
        print(",\n".join( ["{{{}, {}}}".format(hex(regval[0]),hex(regval[1])) for regval in cam._writes]))
        print("};")
        print("int length_exp = sizeof(settings_exp) / sizeof(reg_data);")

