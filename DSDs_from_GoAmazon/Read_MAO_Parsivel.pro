;*************************************************************
; IDL script for reading MAO Processed Parsivel .cdf file
;*************************************************************

PRO READ_MAO_PARSIVEL, Filename,year, month,day, hour, minute, second,$
                       fall_vel, ND, dsd, ZS , ZW, Z, mean_Doppler_W, $
                       mean_Doppler_S, precip , rain_rate, particle_size,$
                       class_size_width, lambda , N0, W , D0,Dm,M1, M2,$
                       M3,M4,M5,M6,Nw,drop_total     

ncid = NCDF_OPEN(Filename)            ; Open The NetCDF file

NCDF_VARGET, ncid,  0, year      ; Read in variable 'year'
NCDF_VARGET, ncid,  1, month      ; Read in variable 'month'
NCDF_VARGET, ncid,  2, day      ; Read in variable 'day'
NCDF_VARGET, ncid,  3, hour      ; Read in variable 'hour'
NCDF_VARGET, ncid,  4, minute      ; Read in variable 'minute'
NCDF_VARGET, ncid,  5, second      ; Read in variable 'second'
NCDF_VARGET, ncid,  6, fall_vel      ; Read in variable 'fall_vel'
NCDF_VARGET, ncid,  7, ND      ; Read in variable 'ND'
NCDF_VARGET, ncid,  8, dsd      ; Read in variable 'dsd'
NCDF_VARGET, ncid,  9, ZS      ; Read in variable 'ZS'
NCDF_VARGET, ncid,  10, ZW      ; Read in variable 'ZW'
NCDF_VARGET, ncid,  11, Z      ; Read in variable 'Z'
NCDF_VARGET, ncid,  12, mean_Doppler_W      ; Read in variable 'mean_Doppler_W'
NCDF_VARGET, ncid,  13, mean_Doppler_S      ; Read in variable 'mean_Doppler_S'
NCDF_VARGET, ncid,  14, precip      ; Read in variable 'precip'
NCDF_VARGET, ncid,  15, rain_rate      ; Read in variable 'rain_rate'
NCDF_VARGET, ncid,  16, particle_size      ; Read in variable 'particle_size'
NCDF_VARGET, ncid,  17, class_size_width      ; Read in variable 'class_size_width'
NCDF_VARGET, ncid,  18, lambda      ; Read in variable 'lambda'
NCDF_VARGET, ncid,  19, N0      ; Read in variable 'N0'
NCDF_VARGET, ncid,  20, W      ; Read in variable 'W'
NCDF_VARGET, ncid,  21, D0      ; Read in variable 'D0'
NCDF_VARGET, ncid,  22, Dm      ; Read in variable 'Dm'
NCDF_VARGET, ncid,  23, M1      ; Read in variable 'M1'
NCDF_VARGET, ncid,  24, M2      ; Read in variable 'M2'
NCDF_VARGET, ncid,  25, M3      ; Read in variable 'M3'
NCDF_VARGET, ncid,  26, M4      ; Read in variable 'M4'
NCDF_VARGET, ncid,  27, M5      ; Read in variable 'M5'
NCDF_VARGET, ncid,  28, M6      ; Read in variable 'M6'
NCDF_VARGET, ncid,  29, Nw      ; Read in variable 'Nw'
NCDF_VARGET, ncid,  30, drop_total      ; Read in variable 'drop_total'

; Read in the Global Attributes.

NCDF_CLOSE, ncid      ; Close the NetCDF file

abort:
END