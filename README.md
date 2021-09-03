# get_ipma_sismos
Retrieves earthquake data from IPMA (Portuguese Meteorological Institute).

IPMA has an API for seismic data, however it only goes back around one month.

This script accesses the API and builds a geojson with its data, which can be imported into e.g. QGIS.

If the py file is kept on the same directory as the geojson, every time the script is run all new earthquakes are appended to the existing file.


IMPORTANT
I have no affiliation with IPMA, this is just a useful script I built for myself.
If you use this script, please make sure to read and follow the IPMA API Terms of Service.