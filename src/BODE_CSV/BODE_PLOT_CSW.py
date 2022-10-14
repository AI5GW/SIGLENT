#!/usr/bin/env python 3.10.1
# -*- coding: utf-8 -*-

"""
 * Example script that imports .CSV-Exportet data from the Bode Plot function of a SDS2000 HD and Displays the data using pandas
 *
 * Copyright (C) 2022 Sebastian (AI5GW) <sebastian@baltic-lab.com>
 * Web (EN): https://baltic-lab.com
 * Web (DE): https://baltic-labor.de/
 * YouTube (EN): https://www.youtube.com/c/BalticLab
 *
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv', skiprows=27)

#print(data)
#sprint(data.columns)

Freq = data['Frequency(Hz)']
CH1_Amp = data['CH1 Amplitude(dB)']
CH1_Phase = data['CH1 Phase(Deg)']
CH2_Amp = data['CH2 Amplitude(dB)']
CH2_Phase = data['CH2 Phase(Deg)']
fig, ax = plt.subplots(2,1)



#ax[0].set_title('Amplitude')

ax[0].set_xlabel('Frequency')
ax[0].set_ylabel('Amplitude')
ax[0].plot(Freq, CH2_Amp, label="Amplitude (CH 2)")
ax[0].plot(Freq, CH1_Amp, label="Amplitude (CH 1)")
ax[0].set_xscale('log')
ax[0].legend()

#ax[1].set_xlabel('Frequency')
ax[1].set_ylabel('Phase')
ax[1].set_title('Phase')
ax[1].plot(Freq, CH1_Phase, label="Phase (CH 1)")
ax[1].plot(Freq, CH2_Phase, label="Phase (CH 2)")
ax[1].set_xscale('log')
ax[1].legend()


plt.show()
