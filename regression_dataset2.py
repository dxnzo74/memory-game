import numpy as np

# Données du Dataset 2
X_donnees = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
Y_donnees = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 7.26, 7.26, 4.74]

X = np.array(X_donnees)
Y = np.array(Y_donnees)

X_matrix = np.column_stack((np.ones(len(X)), X))

theta = np.linalg.inv(X_matrix.T @ X_matrix) @ X_matrix.T @ Y

b = theta[0]
a = theta[1]

print(f"--- Résultats Dataset 2 ---")
print(f"Pente (a) = {a:.3f}")
print(f"Biais (b) = {b:.3f}")
print(f"Équation : y = {a:.2f}x + {b:.2f}")
