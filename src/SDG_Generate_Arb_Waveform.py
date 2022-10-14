#!/usr/bin/env python 3.10.1
# -*- coding: utf-8 -*-

"""
 * Example script to generate a 100 Hz sine wave in Python for SIGLENT SDG function generators. This code can easily be changed to generate two-tone or double sideband signals. Examples provided below. 
 *
 * Copyright (C) 2022 Sebastian (AI5GW) <sebastian@baltic-lab.com>
 * Web (EN): https://baltic-lab.com
 * Web (DE): https://baltic-labor.de/
 * YouTube (EN): https://www.youtube.com/c/BalticLab
 *
"""

import pyvisa as visa
import numpy as np

rm = visa.ResourceManager()

# Connect to device (Make sure to change the resource locator!)
device = rm.open_resource('TCPIP::192.168.188.29::INSTR',query_delay=0.25)

# prevent time-out errors by increasing the timeout to 10 seconds
device.timeout = 10000

# Create an empty array with 16384 points
WAVE = np.arange(0, 0xfffe, 1);

# Fill the waveform array with data
for n in range(len(WAVE)):

    # Frequency in Hz
    F = 100
    
    # Sample Rate in S/s
    SAMPLE_RATE = 16384
    
    # Amplitude (MAX 32767 on SDG1032X)
    Amplitude = 32767
    
    # Calculate factor for normalized frequency
    F_FACTOR = (0.5*np.pi/SAMPLE_RATE)

    # Generate Sine-Wave
    WAVE[n] = Amplitude*np.sin(F*F_FACTOR*n)

    # Uncomment next line for a double sideband (DSB) signal (Carrier= 1 kHz, AF = 100 Hz)
    #WAVE[n] = Amplitude*np.sin(100*F_FACTOR*n)*np.cos(1000*F_FACTOR*n)

    # Uncommend next line for a dual-tone signal (1209 Hz + 697 Hz = DTMF '1')
    #WAVE[n] = 0.5 * Amplitude*np.sin(1209*F_FACTOR*n) + 0.5 * Amplitude * np.cos(697*F_FACTOR*n)

# Write Waveform to Device
# Note: byte order = little-endian!
device.write_binary_values('C1:WVDT WVNM,Python,FREQ,1.0,TYPE,8,AMPL,1.0,OFST,0.0,PHASE,0.0,WAVEDATA,', WAVE, datatype='i', is_big_endian=False)

device.write("C1:ARWV NAME,Python")

#Enable true Arb functionality
device.write("C1:SRATE MODE,TARB,VALUE,%f,INTER,LINE" % SAMPLE_RATE)



  
    
