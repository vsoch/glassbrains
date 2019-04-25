#!/usr/bin/python

from glob import glob
filey = open("gallery.html","wb")
images = glob("*.png")

for i in range(0,len(images)):
  image = images[i]
  filey.writelines('<div id="image-%s" class="masonry-thumb"><a style="background:url(%s) width=200px" title="%s" href="%s"><img class="grayscale" src="%s" alt="%s"></a></div>\n' %(i,image,image,image,image,image))

filey.close()

