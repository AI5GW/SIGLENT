#!/usr/bin/env python 3.10.1
# -*- coding: utf-8 -*-

"""
 * Example script to retrieve screenshot from SIGLENT oscilloscope
 * Tested with: SDS2000X HD & SDS 1202X-E
 *
 * Copyright (C) 2022 Sebastian (AI5GW) <sebastian@baltic-lab.com>
 * Web (EN): https://baltic-lab.com
 * Web (DE): https://baltic-labor.de/
 * YouTube (EN): https://www.youtube.com/c/BalticLab
 *
"""

import sys
import pyvisa as visa
import numpy as np

try:
    rm = visa.ResourceManager()

    # Connect to device (Make sure to change the resource locator!)
    device = rm.open_resource('TCPIP::192.168.188.29::INSTR',query_delay=0.25)
except:
    print('Failed to connect to device...')
    sys.exit(0)
    
device.timeout = 30000
device.chunk_size = 20*1024*1024

device.write("SCDP")
IMAGE_DATA = device.read_raw()

f=open("Screenshot.bmp",'wb')
f.write(IMAGE_DATA)
f.flush()
f.close()

