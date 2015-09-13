from slimscat import run_slimscat, generate_screen
import os
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# generate scattering file
if not os.path.isfile('gargantua_screen.bin'):
  generate_screen(wavelength=0.87e-6,dx=0.2,ips=4,screenfile='gargantua_screen.bin')

# load RGB image with rough scale appropriate for Sgr A*
model = misc.imread('gargantua.jpg'); dx = 50./350
nx,ny,nchan = model.shape

# scatter each rgb channel separately (using same screen)
r = run_slimscat(model[:,:,0],dx,screenfile='gargantua_screen.bin')
g = run_slimscat(model[:,:,1],dx,screenfile='gargantua_screen.bin')
b = run_slimscat(model[:,:,1],dx,screenfile='gargantua_screen.bin')

# construct rgb image
rgb = np.dstack((r,g,b))
rgb[rgb < 0] = 0
rgb = (255 / rgb.max()* rgb).astype(np.uint8)
img = Image.fromarray(rgb)
img.save('scattered_gargantua.jpg')
