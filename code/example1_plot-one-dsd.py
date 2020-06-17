#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:41:54 2020

@author: fiercenator
"""
from radar_helper import *
import matplotlib.pyplot as plt


data_dir = '../DSDs_from_GoAmazon/'

ncfiles = get_ncfiles(data_dir)
num_drops, particle_size, class_size_width = read_disdometer_data(ncfiles)

ii = 0
plt.plot(particle_size,num_drops[ii,:]/class_size_width); 
plt.xlim([0,8])
plt.xlabel('droplet diameter, D [um]')
plt.ylabel(r'size distribution, dN/dD [m$^{-3}$um$^{-1}$]')
