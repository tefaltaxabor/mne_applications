import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig, axs = plt.subplots(1, 2, figsize=(12, 4))
titles = ['Ideal filter', 'Real filter']

# Ideal filter: flat line with one red spike at the source location
x_ideal = np.linspace(-10, 10, 1000)
y_ideal = np.zeros_like(x_ideal)
source_pos = 0
source_index = np.argmin(np.abs(x_ideal - source_pos))
y_ideal[source_index] = 1.0  # spike at the source

# Real filter: broader, wavy curve
x_real = np.linspace(-10, 10, 1000)
y_real = 0.8 * np.exp(-0.5 * ((x_real)/2.5)**2)
y_real += 0.3 * np.sin(2.5 * x_real) * np.exp(-0.1 * x_real**2)

# Plot Ideal filter
axs[0].plot(x_ideal, y_ideal, color='darkred', linewidth=2)
axs[0].plot(x_ideal[source_index], 0, 'o', color='black', markersize=8)  # point on x-axis
axs[0].axhline(0, color='black', linewidth=0.8)
axs[0].set_title(titles[0], fontsize=14)
axs[0].set_xticks([])
axs[0].set_yticks([])
axs[0].set_xlim([-10, 10])
axs[0].set_ylim([-0.2, 1.2])
axs[0].grid(True, which='both', linestyle='--', alpha=0.3)
axs[0].text(0, -0.1, 'Source', ha='center', va='center', fontsize=12)

# Plot Real filter
axs[1].plot(x_real, y_real, color='darkred', linewidth=2)
axs[1].plot(-2.5, 0, 'o', color='black', markersize=8)  # source point
axs[1].plot(3.5, 0, 'o', color='black', markersize=8)   # interference point
axs[1].axhline(0, color='black', linewidth=0.8)
axs[1].set_title(titles[1], fontsize=14)
axs[1].set_xticks([])
axs[1].set_yticks([])
axs[1].set_xlim([-10, 10])
axs[1].set_ylim([-0.2, 1.2])
axs[1].grid(True, which='both', linestyle='--', alpha=0.3)
axs[1].text(-2.5, -0.1, 'Source', ha='center', va='center', fontsize=12)
axs[1].text(3.5, -0.1, 'Interference', ha='center', va='center', fontsize=12)

plt.tight_layout()
plt.show()