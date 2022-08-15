## This script runs tweakreg
# align F657N frames
# this will also be our reference frame, since F657N is our primary filter of interest

from drizzlepac import tweakreg
tweakreg.TweakReg('*_flc.fits',
                  refimage='f657n_improved_drc_sci.fits',
                  #expand_refcat=True,
                  enforce_user_order=False,
                  imagefindcfg={'threshold':200, 'conv_width':3.5, 'dqbits': ~4096},
                  shiftfile=True,
                  outshifts='shift660_flc.txt', #update this filename
                  searchrad=5.0,
                  ylimit=0.6,
                  updatehdr=True,
                  wcsname='UVIS_FLC',
                  reusename=True,
                  interactive=False)
