import numpy as np


def create_mesh(nx, ny):
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
X, Y = np.meshgrid(x, y)
return X, Y
