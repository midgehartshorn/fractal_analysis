#!/bin/bash
set -e
#read -p "On-band:" ON
#read -p "Off-band:" OFF
#ON="f657n_globalmin_drc_sci.aligned.fits"
#OFF="f625_improved_drc_sci.aligned.fits"
ON=$1
OFF=$2
REG="/tmp/tempregions.reg"

grep "color=blue" regions.reg > $REG
BACK=`phot $REG $ON | awk '{x=x+$4; y=y+$6}END{print x/y}'`
NARROW="/tmp/narrow_unback.fits"

# background subtracted images
/diy/Tools/imarith $ON - $BACK $NARROW # subtract background coeff and assign to unback.fits
OFFBACK="/tmp/wide_unback.fits"
BACK=`phot $REG $OFF | awk '{x=x+$4; y=y+$6}END{print x/y}'`
/diy/Tools/imarith $OFF - $BACK $OFFBACK  # subtract background coeff and assign to unback.fits

grep -v "color=blue" regions.reg > $REG
contOff=`phot $REG $OFFBACK | awk '{x=x+$4}END{print x}'`
contOn=`phot $REG $NARROW | awk '{x=x+$4}END{print x}'`

CONTSUM=$(echo $contOn / $contOff |bc -l)
CONT="/tmp/cont.fits"
/diy/Tools/imarith $OFFBACK "*" $CONTSUM $CONT #subtracted continuum ratio cont.fits
/diy/Tools/imarith $ON - $CONT outputimage.fits

ds9 -zscale $ON $OFF outputimage.fits &

