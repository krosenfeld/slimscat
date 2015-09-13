from slimscat import generate_screen,run_slimscat
import matplotlib.pyplot as plt
import numpy as np
import os

# gaussian source
nx,ny = 220,256
yy,xx = np.meshgrid(np.arange(ny)-ny/2,np.arange(nx)-nx/2,indexing='ij')
isrc = np.exp(-0.5*(xx**2 + yy**2) / (0.07*np.min([nx,ny]))**2)

# generate screen
if not os.path.isfile('gaussian_screen.bin'):
  generate_screen(screenfile='gaussian_screen.bin')

# scatter source
iss = run_slimscat(isrc,1.,screenfile='gaussian_screen.bin')

# show result
fig,axs = plt.subplots(ncols=2)
axs[0].imshow(isrc,interpolation='nearest',cmap='hot')
axs[0].set_title('source')
axs[1].imshow(iss,interpolation='nearest',cmap='hot')
axs[1].set_title('scattered')
plt.tight_layout()
plt.savefig('gaussian.png')
