import numpy as np
#from PIL import Image
import matplotlib.pyplot as plt

data=np.zeros(shape=(2490,3510))

for x in range(len(data)):
	for y in range(len(data[0])):
		theta=np.arcsin((x-len(data)/2)/np.sqrt((x-len(data)/2)**2+(y-len(data[0])/2)**2))
		if abs(theta%0.0157)>=0 and abs(theta%0.0157)<0.00785:
			data[x,y]+=255
			
#img=Image.fromarray(data)
plt.imshow(data)
plt.show()
