![](/preview.jpg)

This project was born out of a desire to print large areas of satellite photos of Portland, OR that are only available via smaller 256x256px tiles.  It allows you to fetch and merge tiles from [Portland's ArcGIS server](https://www.portlandmaps.com/arcgis/rest/services/Public).  Though I've only tested in with Portland's ArcGIS server, it _might_ work with other tile servers with a few updates.

Tested on OSX 10.11.6 with Python 3.5.2. First install the requirements.

```
script/bootstrap
```

Open up the server to pull up a debug grid view.  Each grid contains its signature as z,x,y.  

```
script/server
open http://localhost:8000/html/select.html
```

Now download tiles at zoom level 19 starting at the grid point `[83513, 187554]` and going to `[83566, 187555]`.  Tiles are stored and cached in the `tiles` directory in the z/x/y.jpg format.  You can run `script/fetch --help` for more info, but quickly:

* `--layer` - You can find a list of available on the ArcGIS server, but I've only tested with the satellite photo layers.
* `--route` - Generally this is the layer name found in the MapServer URL.  For instance, the route name for [this url](https://www.portlandmaps.com/arcgis/rest/services/Public/Aerial_Photos_Summer_1998/MapServer) is "Aerial_Photos_Summer_1998."

```
./script/fetch -z 19 \
  -x0 83513 \
  -y0 187554 \
  -x1 83566 \
  -y1 187555 \
  --route Aerial_Photos_Summer_1996 \
  --layer Public_Aerial_Photos_Summer_2015
```

Now we can merge the set of tiles we just downloaded into one large image.  You can find more info by running `script/merge --help`, but quickly:

* `-o` - The directory to store the output images.
* `-d` - One or more input directories to read from.  Sometimes it's useful to merge a bunch of layers in one go.

```
./script/merge -o ./out \
  -z 19 \
  -x0 83513 \
  -y0 187554 \
  -x1 83566 \
  -y1 187555 \
  -d tiles/Aerial_Photos_Summer_2015
```
