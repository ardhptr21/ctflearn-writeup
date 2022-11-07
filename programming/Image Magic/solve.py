from PIL import Image, ImageOps
import numpy as np

ori = Image.open('./out copy.jpg')
width, height = ori.size

pixels = np.array(ori)
pixels = pixels.reshape((304, int(width / 304), 3))

reconfig = Image.fromarray(pixels)
reconfig_flip = ImageOps.mirror(reconfig)
reconfig_flip.save('./flag.jpg')
