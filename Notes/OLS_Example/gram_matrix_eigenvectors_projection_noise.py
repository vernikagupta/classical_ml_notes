# Gram Matrix, Eigenvectors, Projection & Noise
# Intuition-first notebook (no PCA)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------
# 1. Create a tiny dataset
# -------------------------------
# Two features, correlated data
X = np.array([
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4]
])

# Center the data (important for variance interpretation)
X_centered = X - X.mean(axis=0)

print("Design Matrix X:\n", X_centered)

# -------------------------------
# 2. Plot data in feature space
# -------------------------------
plt.figure()
plt.scatter(X_centered[:, 0], X_centered[:, 1])
plt.axhline(0)
plt.axvline(0)
plt.xlabel("Feature X1")
plt.ylabel("Feature X2")
plt.title("Data in Feature Space")
plt.show()

# -------------------------------
# 3. Compute Gram matrix
# -------------------------------
G = X_centered.T @ X_centered
print("Gram Matrix X^T X:\n", G)

# -------------------------------
# 4. Eigen-decomposition of Gram matrix
# -------------------------------
eigenvalues, eigenvectors = np.linalg.eigh(G)

print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors (columns):\n", eigenvectors)

# -------------------------------
# 5. Plot eigenvectors on data
# -------------------------------
plt.figure()
plt.scatter(X_centered[:, 0], X_centered[:, 1], label="Data")

origin = np.zeros(2)
for i in range(2):
    v = eigenvectors[:, i]
    plt.arrow(origin[0], origin[1], v[0]*3, v[1]*3,
              head_width=0.1, length_includes_head=True,
              label=f"Eigenvector {i+1}")

plt.axhline(0)
plt.axvline(0)
plt.xlabel("X1")
plt.ylabel("X2")
plt.legend()
plt.title("Eigenvectors as Directions in Feature Space")
plt.show()

# -------------------------------
# 6. Projection of data onto eigenvectors
# -------------------------------
# Normalize eigenvectors
V = eigenvectors / np.linalg.norm(eigenvectors, axis=0)

projections = X_centered @ V
print("Projections of data onto eigenvectors:\n", projections)

# -------------------------------
# 7. Variance along each direction
# -------------------------------
variances = np.var(projections, axis=0)
print("Variance after projection (per eigenvector):\n", variances)

# -------------------------------
# 8. Visualizing projection spread
# -------------------------------
plt.figure()
plt.scatter(projections[:, 0], np.zeros_like(projections[:, 0]), label="EV1")
plt.scatter(projections[:, 1], np.zeros_like(projections[:, 1]), label="EV2")
plt.xlabel("Projection value")
plt.title("Projection Spread Along Eigenvector Directions")
plt.legend()
plt.show()

# -------------------------------
# 9. Add noise and observe effect
# -------------------------------
noise = np.random.normal(0, 0.2, X_centered.shape)
X_noisy = X_centered + noise

# Recompute projections
proj_noisy = X_noisy @ V

plt.figure()
plt.scatter(proj_noisy[:, 0], np.zeros_like(proj_noisy[:, 0]), label="EV1 noisy")
plt.scatter(proj_noisy[:, 1], np.zeros_like(proj_noisy[:, 1]), label="EV2 noisy")
plt.title("Noise Appears in All Directions")
plt.legend()
plt.show()

# -------------------------------
# 10. Noise amplification with small eigenvalues
# -------------------------------
# Simulate scaling by inverse sqrt eigenvalues
scaled = proj_noisy / np.sqrt(eigenvalues + 1e-6)

plt.figure()
plt.scatter(scaled[:, 0], np.zeros_like(scaled[:, 0]), label="Scaled EV1")
plt.scatter(scaled[:, 1], np.zeros_like(scaled[:, 1]), label="Scaled EV2")
plt.title("Small Eigenvalues Amplify Noise")
plt.legend()
plt.show()

print("Notebook complete: You have seen data, Gram matrix, eigenvectors,\n"
      "projection, variance, and why small eigenvalues amplify noise.")
