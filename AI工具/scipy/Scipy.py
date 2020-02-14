import numpy as np
import matplotlib.pyplot as plt
import scipy
import imageio
img = imageio.imread('/Users/chengkun/Desktop/1.jpg')
# img = imread('/Users/chengkun/Desktop/1.jpg')
print(img.shape)
img_tinted = img * [1, 0.95, 0.9,0.8]

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(img)

# Show the tinted image
plt.subplot(1, 2, 2)

# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. To work around this, we
# explicitly cast the image to uint8 before displaying it.
plt.imshow(np.uint8(img_tinted))
plt.show()