import matplotlib.pyplot as plt
import numpy as np
import glob

archivos = sorted(glob.glob("col_data*_flux.lc"))

for archivo in archivos:
    try:
        
        with open(archivo, 'r') as f:
            lineas = f.readlines()

        # Eliminar encabezado y filtrar solo líneas con 3 columnas válidas
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

        # Verificar si hay datos válidos
        if not datos:
            print(f"Error")
            continue

        datos = np.array(datos)

        tiempo = datos[:, 0]
        flujo = datos[:, 1]
        error = datos[:, 2]

        fig, ax = plt.subplots(figsize=(8, 5))  

        ax.errorbar(tiempo, flujo, yerr=error, fmt='o', markersize=3, capsize=0,
                    ecolor='gray', elinewidth=1, label='Flux')

        ax.set_title(f'Flux vs Time - {archivo}')
        ax.set_xlabel('BJD - 2457000.0 (d)')
        ax.set_ylabel('PDCSAP_FLUX (e⁻/s)')

        ax.legend()
        plt.tight_layout()

        nombre_pdf = archivo.replace(".lc", ".pdf")
        plt.savefig(nombre_pdf)
        plt.close()
        print(f"Gráfico guardado como: {nombre_pdf}")

    except Exception as e:
        print(f"")

