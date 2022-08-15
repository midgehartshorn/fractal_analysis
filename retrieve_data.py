## This script contains code for importing and collecting MAST datasets

# imports
from astroquery.mast import Observations
from ccdproc import ImageFileCollection
from astropy.table import Table
from astropy.io import fits, ascii
from astropy.visualization import ZScaleInterval
from IPython.display import Image
import glob
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
from drizzlepac import tweakreg, astrodrizzle

# obtain the UVIS/F656N calibrated FLC and SPT data products
science_list = Observations.query_criteria(objectname='NGC1313',
                                           obs_collection='HST',
                                           filters=[
                                                #'F657N', 
                                                'F660N', 
                                                #'F656N', 
                                                #'F645N', 
                                                #'F621M', 
                                                #'F689M'
                                                    ])
Observations.download_products(science_list['obsid'], 
        mrp_only=False, download_dir='./science',
        productSubGroupDescription=['FLC', 'SPT'])
science_files = glob.glob(os.path.join(os.curdir, 
                                        'science', 
                                        'mastDownload', 
                                        'HST', '*', 
                                        '*fits'))
for im in science_files:
  root = im.split('/')[-1]
  os.rename(im, './' + root)
shutil.rmtree('science/')
