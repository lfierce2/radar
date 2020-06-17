#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:33:31 2020

@author: fiercenator
"""
import os
import numpy as np
import netCDF4

def get_disdrometer_moments(ncfiles,moment_names):
    num_drops, particle_size, class_size_width = get_data(ncfiles)
    dims = np.shape(num_drops)
    observed_moments = np.zeros([dims[0],len(moment_names)])
    observed_rainrate = np.zeros(dims[0])
    
    dia_vals = np.logspace(np.log10(0.1),np.log10(9),1000)
    
    these = np.nonzero((particle_size<=dia_vals.max())&(particle_size>=dia_vals.min()))
    for kk in range(len(moment_names)):
        phi_k_vals = get_kernel(particle_size,moment_names[kk])
        for tt in range(dims[0]):
            sum_this = num_drops[tt][these]*phi_R(particle_size[these])*class_size_width[these]
            rainrate[tt] = sum(sum_this[~np.isnan(sum_this)])
            sum_this = phi_k_vals[these]*num_drops[tt][these]*class_size_width[these]
            moments[tt,kk] = sum(sum_this[~np.isnan(sum_this)])
                
    return moments, rainrate

def get_kernel(particle_size,moment_name):
    read_dir = '../kernel_funs/'
    radius_axisratio = np.loadtxt(read_dir+'radiusmm_axis_ratio.txt')
    if moment_name.startswith('Ahh'):
        phi_k_vals = np.interp(particle_size,radius_axisratio[:,0]*2,np.loadtxt(read_dir+'amp_AH.txt'))
    elif moment_name.startswith('Kdp'):
        phi_k_vals = np.interp(particle_size,radius_axisratio[:,0]*2,np.loadtxt(read_dir+'amp_KDP.txt'))
    elif moment_name.startswith('Zdr'):
        phi_k_vals = np.interp(particle_size,radius_axisratio[:,0]*2,np.loadtxt(read_dir+'amp_ZH.txt') - np.loadtxt(read_dir+'amp_ZV.txt'))
    elif moment_name.startswith('Z'):
        phi_k_vals = np.interp(particle_size,radius_axisratio[:,0]*2,np.loadtxt(read_dir+'amp_ZH.txt'))
    return phi_k_vals

def phi_R(d):
    Vterm_fun = lambda d: (3.78*d**(0.67)); 
    rainrate_kern = (6*np.pi*10**(-4)*d**3*Vterm_fun(d));
    return rainrate_kern

def get_R(d,num_per_bin):
    return sum(num_per_bin*phi_R(d))


def get_ncfiles(data_dir):
    ncfiles = []
    cwd = os.getcwd()
    os.chdir(data_dir)
    ncfiles.extend([data_dir + x for x in os.listdir() if x.endswith('.cdf')])
    os.chdir(cwd)
    return ncfiles

def read_disdometer_data(ncfiles):
    for ncfile in ncfiles:
        f = netCDF4.Dataset(ncfile)
        if 'GoAmazon' in ncfile:
            particle_size = f.variables['particle_size'][:]
            class_size_width = f.variables['class_size_width'][:]            
            number_density_drops = np.transpose(f.variables['ND'][:])
        elif 'SGP' in ncfile:
            particle_size = f.groups['parameter']['particle_size'][:]
            class_size_width = f.groups['parameter']['class_size_width'][:]
            number_density_drops = f.groups['parameter']['Nd'][:]
        num_detected = np.zeros(np.shape(number_density_drops[:,0]))           
        for tt in range(number_density_drops.shape[0]):
            num_detected[tt] = sum(np.transpose(number_density_drops[tt,:]*class_size_width))            

        tt = 0
        dtt = 12
        
        num_drops = np.zeros([0,len(class_size_width)])
        while tt < (number_density_drops.shape[0]-dtt):
            if sum(phi_R(particle_size)*class_size_width*sum(number_density_drops[range(tt,tt+dtt)][:]))>0.1:
                num_drops = np.vstack([num_drops,class_size_width*sum(
                        number_density_drops[range(tt,tt+dtt)][:])])
            tt = tt + dtt
    return num_drops, particle_size, class_size_width