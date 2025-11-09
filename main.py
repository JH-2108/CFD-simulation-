from cfd_solver import simulate_flow
from visualization import plot_streamlines

nx, ny = 50, 50 
steps = 100 
obstacle = (25, 25) 

velocity_field, pressure_field = simulate_flow(nx, ny, steps, obstacle)

plot_streamlines(velocity_field, pressure_field)
