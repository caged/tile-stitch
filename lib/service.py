from owslib.wmts import WebMapTileService

zooms = {
    19: [[187224, 82784], [188035, 83985]]
}

wmts = WebMapTileService("https://www.portlandmaps.com/arcgis/rest/services/Public/Aerial_Photos_Summer_2015/MapServer/WMTS/1.0.0/WMTSCapabilities.xml")

zoom = 19
start_x, start_y = [187530, 83520] #zooms[zoom][0]
end_x, end_y = [start_x + 30, start_y + 30] #zooms[zoom][1]
i = 0
for x in range(start_x, end_x):
    for y in range(start_y, end_y):
        tile_file = "tiles/%s/%s-%s.jpg" % (zoom, x, y)
        print(tile_file)
        try:
            tile = wmts.gettile(
                layer='Public_Aerial_Photos_Summer_2015',
                tilematrixset='GoogleMapsCompatible',
                tilematrix=str(zoom),
                row=str(x),
                column=str(y),
                crs="EPSG:3857")

            with open(tile_file, "wb") as f:
                f.write(tile.read())
            sleep(1)
        except Exception:
            pass
