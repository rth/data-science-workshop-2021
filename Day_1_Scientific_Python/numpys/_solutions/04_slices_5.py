import matplotlib.pyplot as plt
%matplotlib inline

checkerboard = np.zeros((8, 8))
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
plt.imshow(checkerboard)