var CanvasLayer = L.GridLayer.extend({
    createTile: function(point){
        var tile = L.DomUtil.create('div', 'leaflet-tile'),
            canvas = L.DomUtil.create('canvas', 'debug-tile');

        tile.appendChild(canvas)

        var size = this.getTileSize();
        tile.width = canvas.width = size.x;
        tile.height = canvas.height = size.y;

        var ctx = canvas.getContext('2d');
        ctx.rect(0, 0, canvas.width, canvas.height)
        ctx.strokeStyle = 'red'
        ctx.stroke()

        var span = L.DomUtil.create('span', 'debug-tile-info')
        span.innerHTML = point.z + "," + point.x + "," + point.y
        tile.appendChild(span)

        return tile;
    }
});
