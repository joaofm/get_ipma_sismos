# get_ipma_sismos
Retrieves earthquake data from IPMA (Portuguese Meteorological Institute).

IPMA has an API for seismic data, however it only goes back around one month.

This script accesses the API and builds a geojson with its data, which can be imported into e.g. QGIS.

If the py file is kept on the same directory as the geojson, every time the script is run all new earthquakes are appended to the existing file.
