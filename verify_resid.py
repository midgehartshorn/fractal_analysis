## inspect fit and verify residuals
# Inspect the shift file to verify pointing residuals
from astropy.table import Table
from astropy.io import fits, ascii
from ccdproc import ImageFileCollection
import glob
shift_table=Table.read('shift660_flc.txt', format='ascii.no_header',
                       names=['file', 'dx', 'dy', 'rot', 'scale', 'xrms', 'yrms'])
formats = ['.2f', '.2f', '.3f', '.5f', '.2f', '.2f']
for i, col in enumerate(shift_table.colnames[1:]):
  shift_table[col].format = formats[i]
print(shift_table)

# identifies dominant and secondary guide stars
collect_spt = ImageFileCollection('./', glob_include="*_spt.fits", ext=0,
                                  keywords=["asn_id", "config", "dgestar", "sgestar"])
table_spt = collect_spt.summary
print(table_spt)



