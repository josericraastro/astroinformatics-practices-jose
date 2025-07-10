import numpy as np
import glob
import pandas as pd

files = sorted(glob.glob("col_data*_flux.lc"))

results = []

for file in files:
    try:
        with open(file, 'r') as f:
            lines = f.readlines()

        flux_values = []
        for line in lines[1:]:
            parts = line.strip().split()
            if len(parts) == 3:
                try:
                    flux = float(parts[1])
                    flux_values.append(flux)
                except ValueError:
                    continue  

        if not flux_values:
            print(f"")
            continue

        flux_values = np.array(flux_values)

        # Compute statistics
        minimum = np.min(flux_values)
        maximum = np.max(flux_values)
        mean = np.mean(flux_values)
        median = np.median(flux_values)
        std_dev = np.std(flux_values)
        amplitude = maximum - minimum

        results.append({
            'File': file,
            'Min': minimum,
            'Max': maximum,
            'Amplitude': amplitude,
            'Mean': mean,
            'Median': median,
            'Std_Dev': std_dev
        })

    except Exception as e:
        print(f"")

summary_table = pd.DataFrame(results)

print(summary_table)

summary_table.to_csv("flux_statistics_summary.csv", index=False)
print("\n[OK] Summary table saved as 'flux_statistics_summary.csv'")
