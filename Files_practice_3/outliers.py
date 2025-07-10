import matplotlib.pyplot as plt
import numpy as np
import glob

archivos = sorted(glob.glob("col_data*_flux.lc"))

for archivo in archivos:
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()

        datos = []
        for linea in lineas[1:]:
            partes = linea.strip().split()
            if len(partes) == 3:
                try:
                    tiempo = float(partes[0])
                    flujo = float(partes[1])
                    error = float(partes[2])
                    datos.append([tiempo, flujo, error])
                except ValueError:
                    continue 

        if not datos:
            print(f"Error")
            continue

        datos = np.array(datos)

        tiempo = datos[:, 0]
        flujo = datos[:, 1]
        error = datos[:, 2]

        # Detección de outliers
        mediana_flujo = np.median(flujo)
        sigma = np.std(flujo)
        outliers = np.abs(flujo - mediana_flujo) > 4 * sigma

        plt.figure(figsize=(8, 5))

        plt.errorbar(tiempo[~outliers], flujo[~outliers], yerr=error[~outliers],
                     fmt='o', markersize=3, capsize=0,
                     ecolor='gray', elinewidth=1, color='blue', label='Flux')

        plt.errorbar(tiempo[outliers], flujo[outliers], yerr=error[outliers],
                     fmt='o', markersize=4, capsize=0,
                     ecolor='red', elinewidth=1, color='red', label='Outliers')

        plt.title(f'Flux vs Time - {archivo}')
        plt.xlabel('BJD - 2457000.0 (d)')
        plt.ylabel('PDCSAP_FLUX (e⁻/s)')
        plt.legend()
        plt.tight_layout()

        nombre_pdf = archivo.replace(".lc", ".pdf")
        plt.savefig(nombre_pdf)
        plt.close()

        print(f"Gráfico guardado como: {nombre_pdf}")

    except Exception as e:
        print(f"")
