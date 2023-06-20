from astropy.coordinates import SkyCoord
import healpy as hp
import numpy as np


# -*- coding: utf-8 -*-
"""
Created on Mon May 29 11:34:14 2023

@author: marin
"""
import numpy as np
import h5py  
import bilby 
import corner
from matplotlib import pyplot as plt
import numpy as np
import healpy as hp

from healpy.newvisufunc import projview, newprojplot


result_list = []
path = '/home/supeguest/Documents/LDAS_Codes/GW382641_16cpus/outdir_G382641_16cpus/result/'
node_nb = 16
prefix= 'G382641_16cpus_data0_1267509412-389_analysis_H1L1V1_par'
out = 'SSMC2_FIGURES/'

for i in range(node_nb):
    print(i)
    if (i != 20 ):
        file = prefix + '%i'%i + '_result.hdf5'
        filename = path+file
        result = bilby.core.result.read_in_result(filename=filename, outdir=None, label=None, extension='hdf5')
        result_list.append(result)

result_list = bilby.core.result.ResultList(results=result_list)

merge_results = result_list.combine()

coord = merge_results.posterior
median_ra = merge_results.get_one_dimensional_median_and_error_bar(['ra'])
median_dec = merge_results.get_one_dimensional_median_and_error_bar(['dec'])

ra = []
dec = []
for i in range(len(coord['ra'])):
    ra.append(coord['ra'][i])
    dec.append(coord['dec'][i])

# converting list to array
ra = np.array(ra)
dec = np.array(dec)

def cat2hpx(lon, lat, nside, radec=True):
    """
    Convert a catalogue to a HEALPix map of number counts per resolution
    element.

    Parameters
    ----------
    lon, lat : (ndarray, ndarray)
        Coordinates of the sources in degree. If radec=True, assume input is in the icrs
        coordinate system. Otherwise assume input is glon, glat

    nside : int
        HEALPix nside of the target map

    radec : bool
        Switch between R.A./Dec and glon/glat as input coordinate system.

    Return
    ------
    hpx_map : ndarray
        HEALPix map of the catalogue number counts in Galactic coordinates

    """

    npix = hp.nside2npix(nside)


    # conver to theta, phi
    theta = np.radians(90. - b)
    phi = np.radians(l)

    # convert to HEALPix indices
    indices = hp.ang2pix(nside, theta, phi)

    idx, counts = np.unique(indices, return_counts=True)

    # fill the fullsky map
    hpx_map = np.zeros(npix, dtype=int)
    hpx_map[idx] = counts

    return hpx_map


l = np.rad2deg(ra)
b = np.rad2deg(dec)

hpx_map = cat2hpx(l, b, nside=32, radec=True)

# Hammer projection, Equatorial coordinates
a = projview(
    np.log10(hpx_map+1),
    xsize = 1600,
    coord=["G", "C"],
    norm='symlog',
    graticule=True,
    cmap = "plasma",
    graticule_labels=True,
    unit=r"counts",
    xlabel="latitude",
    ylabel="longitude",
    xtick_label_color = "white",
    cb_orientation="vertical",
    projection_type="mollweide",
    title="Projection of the PDF for the sky location of SSSMC1",
);
