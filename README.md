# Finite Difference Methods for Solving PDEs

This repository contains implementations of numerical methods for solving partial differential equations (PDEs) using the **Finite Difference Method (FDM)**. The focus is on three classical schemes:

1. **Explicit Scheme**
2. **Implicit Scheme**
3. **Crank-Nicolson Scheme**

---

## 📘 File Overview

### 1. `Explicit_Implicit_FDM(F).ipynb`

This notebook demonstrates the **Explicit** and **Implicit** schemes for solving time-dependent PDEs (like the heat equation). It covers:

- **Explicit Scheme**:
  - Uses the forward time and central space (FTCS) discretization.
  - Condition for stability is discussed (`dt <= dx² / (2*ν)`).
  - Simple to implement but conditionally stable.

- **Implicit Scheme**:
  - Uses backward time and central space discretization.
  - Requires solving a linear system at each time step.
  - Unconditionally stable but computationally more intensive.

Both methods are demonstrated with code, numerical results, and basic plots to visualize the evolution of the solution over time.

---

### 2. `Cranck Nicholson.ipynb`

This notebook implements the **Crank-Nicolson Scheme**, a combination of Explicit and Implicit methods that offers:

- **Second-order accuracy** in both time and space.
- **Unconditional stability**, like the implicit method.
- Involves solving a tridiagonal system using the Thomas Algorithm.

This method provides better accuracy than either explicit or implicit schemes alone, making it ideal for problems requiring precision and stability.

---

## 🛠️ Requirements

You can run the notebooks with the following Python libraries:

- `numpy`
- `matplotlib`
- `scipy` (optional, if used for solving linear systems)
- `jupyter` or any notebook-compatible interface

To install the requirements:
```bash
pip install numpy matplotlib scipy notebook
