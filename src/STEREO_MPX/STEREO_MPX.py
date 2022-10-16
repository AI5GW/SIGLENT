#!/usr/bin/env python 3.10.1
# -*- coding: utf-8 -*-


"""
 * Example script to generate waveform data for a valid stereo-FM multiplex (MPX) signal with SIGLENT SDG arbritrary waveform generators
 *
 * Tested on: SIGLENT SGD1032X
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
    
# prevent time-out errors by increasing the timeout to 10 seconds
device.timeout = 10000

# Create an empty array with 16384 points
WAVE = np.arange(0, 0xfffe, 1);

# Sample Rate in S/s
SAMPLE_RATE = 1638400

# Calculate factor for normalized frequency
F_FACTOR = (np.pi/(2*SAMPLE_RATE))

# Fill the waveform array with data
for n in range(len(WAVE)):
    
    # Amplitude (MAX 32767 on SDG1032X)
    Amplitude = 32767

    # Generate waveform data
    WAVE[n] = 0.47*Amplitude*(np.sin(700*F_FACTOR*n)+np.sin(2200*F_FACTOR*n)+0.1*np.sin(19000*F_FACTOR*n)+np.sin(38000*F_FACTOR*n)*(np.sin(700*F_FACTOR*n)-np.sin(2200*F_FACTOR*n)))

    

# Write Waveform to Device
# Note: byte order = little-endian!
device.write_binary_values('C1:WVDT WVNM,STEREO_MPX,FREQ,100.0,TYPE,8,AMPL,1.0,OFST,0.0,PHASE,0.0,WAVEDATA,', WAVE, datatype='i', is_big_endian=False)

device.write("C1:ARWV NAME,STEREO_MPX")

#Enable true Arb functionality
device.write("C1:SRATE MODE,TARB,VALUE,%f,INTER,LINE" % SAMPLE_RATE)
