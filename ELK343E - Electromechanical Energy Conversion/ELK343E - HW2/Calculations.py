import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constants
a = 89.98
S_max = 400 * 1e3  # 400 kVA converted to VA
phi_values = {
    "0.75 Inductive": np.arccos(0.75),
    "1.0 Unity": np.arccos(1.0),
    "0.75 Capacitive": np.arccos(-0.75)
}

# Function to calculate parameters with debugging
def calculate_parameters(S_values, phi_values):
    results = {
        "Case": [],
        "S (kVA)": [],
        "I1ph (A)": [],
        "E1 (V)": [],
        "I0 (A)": [],
        "I0_reel (A)": [],
        "I2ph (A)": [],
        "V2p-p (V)": [],
        "Pcu (W)": [],
        "Pfe (W)": [],
        "Efficiency (%)": []
    }
    
    for phi_name, phi in phi_values.items():
        for S in S_values:
            # Step 1: Calculate Input Line Current
            I1ph = (S / 62353.829) 
            
            # Step 2: Calculate Induced Voltage
            E1 = 20780 - I1ph * (20 + 32j)
            
            # Step 3: Calculate Iron Loss Current
            I0 = E1 / (3496.4339 + 41706.8855j)
            
            # Step 4: Calculate Secondary Phase Current
            I2ph = I1ph - I0
            
            # Step 5: Calculate Phase-to-Phase Voltage
            V2p_p = np.sqrt(3) * (E1 - (13.7599 + 29.1395j) * I2ph) / a
            
            # Step 6: Copper and Iron Losses
            Pcu = 3 * ((abs(I1ph) ** 2) * 20 + (abs(I2ph) ** 2) * 13.76)
            Pfe = 3 * (I0.real ** 2) * 501000
            
            # Step 7: Output Power and Efficiency
            P_in = abs(S * np.cos(phi))
            P_out = P_in - (Pcu + Pfe)
            efficiency = (P_out / P_in) * 100
            
            # Append to Results
            results["Case"].append(phi_name)
            results["S (kVA)"].append(S / 1e3)  # Convert back to kVA for display
            results["I1ph (A)"].append(abs(I1ph))
            results["E1 (V)"].append(abs(E1))
            results["I0 (A)"].append(abs(I0))
            results["I0_reel (A)"].append(I0.real)  # Real part of I0
            results["I2ph (A)"].append(abs(I2ph))
            results["V2p-p (V)"].append(abs(V2p_p))
            results["Pcu (W)"].append(Pcu)
            results["Pfe (W)"].append(Pfe)
            results["Efficiency (%)"].append(efficiency)
    
    return pd.DataFrame(results)

# S values as a percentage of S_max (10% to 100% in 1% increments)
percentages = np.arange(10, 101, 1)  # Percentages from 10% to 100%
S_values = (percentages / 100) * S_max

# Calculate results
results_df = calculate_parameters(S_values, phi_values)

# Function to plot individual results
def plot_individual_results(results_df):
    cases = results_df["Case"].unique()
    for case in cases:
        df_case = results_df[results_df["Case"] == case]
        print(f"Plotting graphs for {case}...")
        
        # Plot I1ph vs S
        plt.figure(figsize=(8, 6))
        plt.plot(df_case["S (kVA)"], df_case["I1ph (A)"], label="I1ph")
        plt.xlabel("S (kVA)")
        plt.ylabel("I1ph (A)")
        plt.grid(True)
        plt.legend()
        plt.show()

        # Plot E1 vs S
        plt.figure(figsize=(8, 6))
        plt.plot(df_case["S (kVA)"], df_case["E1 (V)"], label="E1")
        plt.xlabel("S (kVA)")
        plt.ylabel("E1 (V)")
        plt.grid(True)
        plt.legend()
        plt.show()

        # Plot V2p-p vs S
        plt.figure(figsize=(8, 6))
        plt.plot(df_case["S (kVA)"], df_case["V2p-p (V)"], label="V2p-p")
        plt.xlabel("S (kVA)")
        plt.ylabel("V2p-p (V)")
        plt.grid(True)
        plt.legend()
        plt.show()

        # Plot Pcu vs S
        plt.figure(figsize=(8, 6))
        plt.plot(df_case["S (kVA)"], df_case["Pcu (W)"], label="Pcu")
        plt.xlabel("S (kVA)")
        plt.ylabel("Pcu (W)")
        plt.grid(True)
        plt.legend()
        plt.show()

        # Plot Pfe vs S
        plt.figure(figsize=(8, 6))
        plt.plot(df_case["S (kVA)"], df_case["Pfe (W)"], label="Pfe")
        plt.xlabel("S (kVA)")
        plt.ylabel("Pfe (W)")
        plt.grid(True)
        plt.legend()
        plt.show()

        # Plot Efficiency vs S
        plt.figure(figsize=(8, 6))
        plt.plot(df_case["S (kVA)"], df_case["Efficiency (%)"], label="Efficiency")
        plt.xlabel("S (kVA)")
        plt.ylabel("Efficiency (%)")
        plt.grid(True)
        plt.legend()
        plt.show()

# Plot results individually for each case
plot_individual_results(results_df)

# Save to Excel
file_path = 'Calculations.xlsx'
results_df.to_excel(file_path, index=False)

print(f"Results saved to: {file_path}")
