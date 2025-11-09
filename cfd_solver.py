import numpy as np


def simulate_flow(nx, ny, steps, obstacle=None):
u = np.zeros((nx, ny))
v = np.zeros((nx, ny))
p = np.zeros((nx, ny))


for t in range(steps):
u[1:-1, 1:-1] += 0.1 * (u[1:-1, 2:] - u[1:-1, :-2] + u[2:, 1:-1] - u[:-2, 1:-1])
v[1:-1, 1:-1] += 0.1 * (v[1:-1, 2:] - v[1:-1, :-2] + v[2:, 1:-1] - v[:-2, 1:-1])


if obstacle:
x, y = obstacle
u[x-1:x+2, y-1:y+2] = 0
v[x-1:x+2, y-1:y+2] = 0


p = u + v


return (u, v), p
