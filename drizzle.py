# drizzle all frames to mosaic 
from drizzlepac import astrodrizzle
import numpy as np
import shutil
import os
import matplotlib.pyplot as plt
from astropy.io import fits
astrodrizzle.AstroDrizzle('*flc.fits',
                          output='f660n_improved', #update filename
                          preserve=False,
                          clean=True, #set to true on final run
                          build=False,
                          context=False,
                          resetbits=4096,
                          skymethod='match',
                          combine_type='minmed',
                          final_bits='64,16',
                          final_wcs=True,
                          final_scale=0.04,
                          )

# display combined images
# science image
sci = fits.getdata('f660n_improved_drc_sci.fits')
fig = plt.figure(figsize=(14,14))
plt.imshow(sci, vmin=0, vmax=1, cmap='Greys_r', origin='lower')

# weighted image
wht = fits.getdata('f660n_improved_drc_wht.fits')
fig = plt.figure(figsize=(14,14))
plt.imshow(wht, vmin=0, vmax=10000, cmap='Greys_r', origin='lower')
