# CFD Simulation 
A Python-based 2D Computational Fluid Dynamics (CFD) simulation project.  
This project models airflow over simple geometries, visualizes velocity and pressure fields, and demonstrates basic CFD principles using streamlines and obstacles. It’s ideal for students, hobbyists, or anyone learning CFD and Python-based simulations.

---

## Features

- Simple 2D CFD solver for velocity and pressure fields  
- Handles basic obstacles in the flow  
- Streamline visualization with velocity magnitude coloring  
- Modular Python code for easy customization and extension  
- Suitable for learning CFD concepts, numerical methods, and visualization techniques  

---

## Folder Structure

The project is organized as follow 
CFD-simulation/
│
├─ main.py # Main script to run the simulation
├─ cfd_solver.py # Core CFD solver functions
├─ visualization.py # Functions for plotting and animating results
├─ utils.py # Helper functions (mesh generation, geometry)
├─ assets/ # Input data, obstacle shapes, and example images
├─ results/ # Output data and simulation results (images, arrays)
├─ requirements.txt # Python dependencies
├─ README.md # Project overview and instructions
└─ LICENSE # License file (MIT)


---

## ⚡ Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/CFD-simulation.git
cd CFD-simulation

# 2. Install dependencies
pip install -r requirements.txt
