from PIL import Image
import os, math

width = 2000
height = 1000
tilesize = 256
start_x, start_y = [187530, 83520]
end_x, end_y = [start_x + 20, start_y + 20]

lst = os.listdir("tiles/19")
count = len(lst)
grid  = int(math.sqrt(count))

resulwidth = tilesize * grid
resultheight = tilesize * grid


merged = Image.new('RGB', (resulwidth, resultheight))

for x in range(start_x, end_x):
    for y in range(start_y, end_y):
        y_offset = (x - start_x) % grid
        x_offset = (y - start_y) % grid
        img_name = "tiles/19/%s-%s.jpg" % (x, y)
        img = Image.open(img_name)
        print("Writing %s at %s,%s" % (img_name, x_offset * 256, y_offset * 256))

        merged.paste(im=img, box=(x_offset * tilesize, y_offset * tilesize))


merged.save('merged.jpg')
