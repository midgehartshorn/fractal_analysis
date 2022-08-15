## this script reviews the downloaded data
# F657N exposures were dithered in sets of 3
from ccdproc import ImageFileCollection
collect_uvis = ImageFileCollection('./', glob_include="*flc.fits", ext=0,
                                   keywords=["asn_id", 
                                       "detector", 
                                       "filter", 
                                       "exptime", 
                                       "postarg1", 
                                       "postarg2"])
uvis_table = collect_uvis.summary
uvis_table['exptime'].format = '7.1f'
uvis_table['postarg1'].format = '7.2f'
uvis_table['postarg2'].format = '7.2f'
uvis_table



