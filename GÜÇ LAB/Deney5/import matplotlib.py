import matplotlib.pyplot as plt
import numpy as np

# 1. Simulation Datasets (Extracted from LTspice steps)
V_AK_sim = np.array([1.867, 1.889, 1.908, 1.927, 1.944])  # Voltage (V)
I_k_sim = np.array([0.4, 0.8, 1.2, 1.6, 2.0])             # Current (A)

# 2. Experimental Datasets (From your handwritten Table 3)
V_AK_exp = np.array([0.795, 0.826, 0.845, 0.860, 0.880])  # Voltage (V)
I_k_exp = np.array([0.4, 0.8, 1.2, 1.6, 2.0])             # Current (A)

# Setup the figure area
plt.figure(figsize=(10, 6), dpi=100)

# Plot Simulation Curve (Blue)
plt.plot(V_AK_sim, I_k_sim, color='#1f77b4', linestyle='--', marker='o', 
         linewidth=2, markersize=8, label='Simulation Curve (LTspice Macro-Model)')

# Plot Experimental Curve (Orange)
plt.plot(V_AK_exp, I_k_exp, color='#ff7f0e', linestyle='-', marker='s', 
         linewidth=2, markersize=8, label='Experimental Curve (Physical Bench Test)')

# Format Annotations for the Data Points
for i in range(len(I_k_exp)):
    # Lab labels
    plt.annotate(f'{I_k_exp[i]}A\n({V_AK_exp[i]}V)', (V_AK_exp[i], I_k_exp[i]), 
                 textcoords="offset points", xytext=(-15, 10), ha='center', fontsize=8)
    # Sim labels
    plt.annotate(f'{I_k_sim[i]}A\n({V_AK_sim[i]}V)', (V_AK_sim[i], I_k_sim[i]), 
                 textcoords="offset points", xytext=(15, -15), ha='center', fontsize=8)

# Title and Axis Labels
plt.title('Thyristor Forward Conduction: Simulation vs. Experimental I-V Characteristics', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Thyristor Forward Voltage Drop, V_AK [V]', fontsize=11, fontweight='semibold')
plt.ylabel('Thyristor Load Current, I_k [A]', fontsize=11, fontweight='semibold')

# Add Grid and Legend
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower right', fontsize=10, frameon=True, shadow=True)

# Adjust axes window bounds to comfortably fit both curves side-by-side
plt.xlim(0.6, 2.2)
plt.ylim(0.1, 2.4)

plt.tight_layout()
plt.show()