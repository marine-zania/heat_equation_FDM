# -*- coding: utf-8 -*-
"""Explicit_Implicit_FDM(F).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sti8xBOrYWmSHJUsUWhzoj54J5ZOY2nf
"""

# Solve 16∂u/∂t = ∂²u/∂x², 0<=x<=4, t>0
# with boundary condition u(0,t)= 0, u(4,t)= 8
# and initial condition u(x,0)= 1/2x(8-x)

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

L = 4         # Length of the spatial domain
dx = 0.25      # Spatial step size (delta x)
dt = 0.25        # Time step size (delta t)
alpha = 1/16
time_steps = 5

T = time_steps * dt
print(f'Total time T = {T:.4f}')

# Stability condition
r = alpha * dt / dx**2
print ('r=', r)
if r > 0.5:
    print("Warning: The scheme may be unstable (r > 0.5).")

Nx = int(L / dx) + 1
Nt = time_steps + 1
print('Number of discretization on x:', Nx)
print('Number of discretization on t:', Nt)

x = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt)

u = np.zeros((Nt, Nx))

# Initial condition:
u[0, :] = 0.5 * x * (8 - x)   #u(x, 0) = 1/2x(8 - x)

# Boundary conditions
u[:, 0] = 0     # u(0, t) = 0
u[:, -1] = 8    # u(4, t) = 8

"""##Explicit Scheme"""

# Finite difference method (explicit scheme)
for j in range(Nt - 1):
    for i in range(1, Nx - 1):
        u[j + 1, i] = r * u[j, i - 1] + (1 - 2 * r) * u[j, i] + r * u[j, i + 1]

# Function to print a detailed table
def print_table(u, x, t):
    headers = ["x"] + [f"{x_val:.1f}" for x_val in x]
    table = []
    for j, time_step in enumerate(t):
        row = [f"j={j}(t={time_step})"] + [f"{u[j, i]:.4f}" for i in range(len(x))]
        table.append(row)
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

# Display table of results for selected time steps
print_table(u, x, t)

plt.figure()
for j in range(0, Nt, int(Nt/4)):
    plt.plot(x, u[j, :], marker='o', label=f't = {j*dt}')
plt.xlabel('x')
plt.ylabel('u(x, t)')
plt.legend()
plt.title("Heat Distribution Over Time")
plt.grid(True)
plt.show()

"""Implicit Scheme"""

# Set up the tridiagonal matrix A for the implicit scheme
A = np.zeros((Nx - 2, Nx - 2))
b = np.zeros(Nx - 2)

# Filling matrix A using r
for i in range(Nx - 2):
    if i > 0:
        A[i, i - 1] = -r
    A[i, i] = 1 + 2 * r
    if i < Nx - 3:
        A[i, i + 1] = -r

# Time-stepping using the implicit method
for n in range(0, Nt - 1):
    # Right-hand side vector
    b[:] = u[n, 1:-1]
    # Adjust for boundary conditions
    b[0] += r * u[n + 1, 0]  # Left boundary
    b[-1] += r * u[n + 1, -1]  # Right boundary

    # Solve the tridiagonal system A * u_next = b
    u[n + 1, 1:-1] = np.linalg.solve(A, b)

# Function to print a detailed table
def print_table(u, x, t):
    headers = ["x"] + [f"{x_val:.1f}" for x_val in x]
    table = []
    step = max(int(Nt / 10), 1)  # Ensure the step size is at least 1
    for n, time_step in enumerate(t[::step]):  # Display every 10th time step or at least every step 1
        row = [f"t = {time_step:.2f}"] + [f"{u[n * step, j]:.4f}" for j in range(len(x))]
        table.append(row)
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

print_table(u, x, t)

# Plotting the solution with markers
plt.figure()
time_steps_to_plot = [0, int(Nt/4), int(Nt/2), int(3*Nt/4), Nt-1]
for n in time_steps_to_plot:
    plt.plot(x, u[n, :], marker='o', linestyle='-', label=f't = {n * dt:.2f}')
plt.xlabel('x')
plt.ylabel('u(x, t)')
plt.title("Heat Distribution Over Time (Implicit Method)")
plt.legend()
plt.grid(True)
plt.show()

