import numpy as np
import pandas as pd
from scipy.optimize import fsolve

# Define the constants
H1 = 3089
q = 280.84
wi = 2.33
wc = 0.9728
a = 450
Eel = 0.00012987
Eth = 0.0000189
t1 = -30

# Generate t2 values from -30 to 40 in steps of 5
t2_values = np.arange(-30, 41, 5)

# Define the equation to solve for H2
def equation(H2, t2):
    term1 = H2 + q * (Eth / Eel) * (t2 - t1)
    term2 = (a**2 * (wi + wc)**2 * q) / (24 * H1**2 * Eel)
    term3 = H1
    rhs = (a**2 * wc**2 * q) / (24 * Eel)
    return H2**2 * (term1 + term2 - term3) - rhs

# Solve for H2 for each t2 value
H2_values = []
for t2 in t2_values:
    # Use fsolve to find the root of the equation
    H2_solution = fsolve(equation, H1, args=(t2))[0]  # Initial guess is H1
    H2_values.append(H2_solution)

# Create a DataFrame for the results
results = pd.DataFrame({
    "t2": t2_values,
    "H2": H2_values
})

# Add "stress" column (H2 / q)
results["stress"] = results["H2"] / q

# Add "sag" column (a^2 * wc / (8 * H2))
results["sag"] = (a**2 * wc) / (8 * results["H2"])

# Save the final results to an Excel file
file_path_final_excel = "H2_Stress_Sag_Results_Final.xlsx"
results.to_excel(file_path_final_excel, index=True, index_label="Index", sheet_name="Results")

# Inform the user of the file creation
file_path_final_excel

