import numpy as np
import TEMimagemanipulation

#.getSubImage() input is a 2D numpy array
#it returns an array with: 
#array[0] = numpy array, the subimage
#array[1] = tuple, start click position
#array[2] = tuple, end release position

data = np.genfromtxt("lattice.dat")
subImageArray = TEMimagemanipulation.getSubImage(data)
subImage = subImageArray[0]
position1 = subImageArray[1]
position2 = subImageArray[2]
