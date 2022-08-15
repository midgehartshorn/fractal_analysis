## Inspect the fit for each .match file

# inspect the fits
# v02a matches
plt.figure(figsize = (20,7))
data = fits.open('hst_13773_15_wfc3_uvis_f657n_icnk15jz_flc.fits')['SCI', 1].data
zscale = ZScaleInterval()
z1, z2 = zscale.get_limits(data)
plt.imshow(data, cmap='Greys', origin='lower', vmin=z1, vmax=z2)
match_tab = ascii.read('hst_13773_15_wfc3_uvis_f657n_icnk15jz_flc_catalog_fit.match')
x_coord, y_coord = match_tab['col11'], match_tab['col12']
plt.scatter(x_coord, y_coord, s=30, edgecolor='r', facecolor='None')
plt.ylim(0, 1014)
plt.xlim(0, 1014)
plt.title('Match: to (Ref)', fontsize=20)

# vector residuals
Image(filename='vector_hst_13773_15_wfc3_uvis_f657n_icnk15jz_flc.png', width=500, height=300)

# fit residuals
#v02a fit residuals
Image(filename='residuals_hst_13773_15_wfc3_uvis_f657n_icnk15jz_flc.png', width=500, height=300)

