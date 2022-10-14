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

import pyvisa as visa
import numpy as np
import matplotlib.pyplot as plotter

rm = visa.ResourceManager()
device = rm.open_resource('TCPIP::192.168.188.28::INSTR',query_delay=0.25)
device.timeout = 30000
device.chunk_size = 20*1024*1024

device.write("SCDP")
IMAGE_DATA = device.read_raw()

f=open("Screenshot.bmp",'wb')
f.write(IMAGE_DATA)
f.flush()
f.close()

