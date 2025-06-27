import pandas as pd
import os

input_directory = "C:/Users/Usuario/Desktop/PROGRAMAS/CONVERTIR XLS A XLSX/ARCHIVOS"
output_directory = "C:/Users/Usuario/Desktop/PROGRAMAS/CONVERTIR XLS A XLSX/ARCHIVOS_CONVERTIDOS"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_directory, filename)
        try:
            # Intenta leer el archivo como HTML
            dfs = pd.read_csv(file_path)
            if dfs:
                # Guarda el primer DataFrame en un archivo .xlsx
                output_file_path = os.path.join(output_directory, filename.replace(".csv", ".xlsx"))
                dfs[0].to_excel(output_file_path, index=False)
                print(f"Archivo {filename} convertido exitosamente.")
            else:
                print(f"No se pudo leer el archivo {filename} como HTML.")
        except Exception as e:
            print(f"Error al convertir {filename}: {e}")
