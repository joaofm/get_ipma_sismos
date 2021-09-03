import requests
import json

try:

    req = requests.get('https://api.ipma.pt/open-data/observation/seismic/7.json')
    
    lista_sismos_nova = json.loads(req.text)['data']
    
    lista_geojson = [{
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [float(sismo['lon']), float(sismo['lat'])]
    },
    "properties": {
        'googlemapref': sismo['googlemapref'],
        'degree': sismo['degree'],
        'sismoId': sismo['sismoId'],
        'dataUpdate': sismo['dataUpdate'],
        'magType': sismo['magType'],
        'obsRegion': sismo['obsRegion'],
        'lon': sismo['lon'],
        'source': sismo['source'],
        'depth': sismo['depth'],
        'tensorRef': sismo['tensorRef'],
        'sensed': sismo['sensed'],
        'shakemapid': sismo['shakemapid'],
        'time': sismo['time'],
        'lat': sismo['lat'],
        'shakemapref': sismo['shakemapref'],
        'local': sismo['local'],
        'magnitud': sismo['magnitud']
        }
    } for sismo in lista_sismos_nova]

    lista_geojson_nova = sorted(lista_geojson, key=lambda k: k["properties"]["time"])
    lista_nova = lista_geojson_nova
    
    try:
        with open('sismos.geojson', 'r') as in_file:
            ficheiro_local = json.load(in_file)
            last_date = ficheiro_local['features'][-1]['properties']['time']
        
            new_sismos = [x for x in lista_geojson if x['properties']['time'] > last_date]

            lista_nova = ficheiro_local['features'] + new_sismos
    except IOError:
        print('ioerror')
    
    with open('sismos.geojson', 'w') as out_file:
        
        geojson = {
            "type": "FeatureCollection",
            "features": lista_nova
            }


        json.dump(geojson, out_file, indent=6)
        print('Atualizado!')

except Exception as err:
    print(err)
