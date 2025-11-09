import matplotlib.pyplot as plt
import numpy as np


def plot_streamlines(velocity_field, pressure_field):
u, v = velocity_field
nx, ny = u.shape
x = np.linspace(0, nx-1, nx)
y = np.linspace(0, ny-1, ny)
X, Y = np.meshgrid(x, y)


plt.figure(figsize=(8,6))
plt.streamplot(X, Y, u.T, v.T, color=np.sqrt(u.T**2 + v.T**2), cmap='viridis')
plt.colorbar(label='Velocity magnitude')
plt.title('Streamlines')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
