.. _examples:

Examples
========

Gaussian
--------
The following code scatters a Gaussian source.

First, we generate our source model as a 2D numpy array.

.. code-block:: python

    import matplotlib.pyplot as plt 
    import numpy as np

    # construct gaussian source
    nx,ny = 220,256
    yy,xx = np.meshgrid(np.arange(ny)-ny/2,np.arange(nx)-nx/2,indexing='ij')
    isrc = np.exp(-0.5*(xx**2 + yy**2) / (0.07*np.min([nx,ny]))**2)

Next we generate the screen which will be written to the file gaussian_screen.bin.
This permits us to run many simulations using the same screen.

.. code-block:: python

    # generate screen
    generate_screen(screenfile='gaussian_screen.bin')

    # scatter source
    iss = run_slimscat(isrc,1.,screenfile='gaussian_screen.bin')

Our gaussian source appears to have been scrambled by our simulated screen.

.. image:: http://i172.photobucket.com/albums/w36/krosenf/gaussian_zpsdelzel97.png 

Gargantua
---------

In this example we will have a bit of fun and use an image rendered to look
like the supermassive black hole from the movie 
`Interstellar <http://www.interstellarmovie.net/>`_.  

.. figure:: http://i172.photobucket.com/albums/w36/krosenf/gargantua_zpsdjotmjwm.jpg 

    Image by `BlackRainbow <http://blenderartists.org/forum/showthread.php?355402-Interstellar-Black-Hole/page2>`_

We'll generate the 
screen for observations at a slightly smaller wavelength and higher
resolution.

.. code-block:: python

    # generate scattering file
    generate_screen(wavelength=0.87e-6,dx=0.2,ips=4,screenfile='gargantua_screen.bin')

And we'll run the simulation over each RGB channel disregarding the important 
dependence on wavelength.

.. code-block:: python

    # load RGB image with rough scale appropriate for Sgr A*
    model = misc.imread('gargantua.jpg')
    dx = 50./350    # photon ring diameter is about 50 microarcseconds
    nx,ny,nchan = model.shape

    # scatter each rgb channel separately (using same screen)
    r = run_slimscat(model[:,:,0],dx,screenfile='gargantua_screen.bin')
    g = run_slimscat(model[:,:,1],dx,screenfile='gargantua_screen.bin')
    b = run_slimscat(model[:,:,1],dx,screenfile='gargantua_screen.bin')

And Gargantua appears scattered:

.. image:: http://i172.photobucket.com/albums/w36/krosenf/scattered_gargantua_zpszg45omwc.jpg 
.. .. image:: ../_static/examples/scattered_gargantua.jpg
