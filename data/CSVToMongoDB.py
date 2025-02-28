import os
import pandas as pd
from pymongo import MongoClient
from config.config import MONGO_URI, DATABASE_NAME
from controller.db_connection import cliente, db

# Configuración de la conexión a MongoDB
# MONGO_URI = "mongodb://localhost:27017/"  # Cambia esto si usas MongoDB Atlas o un puerto diferente
COLLECTION_NAME = "asistencias"
CSV_FOLDER = "data/archivos"  # Nombre de la carpeta con los archivos CSV

# Obtener lista de archivos CSV en la carpeta
archivos_csv = [f for f in os.listdir(CSV_FOLDER) if f.endswith(".csv")]

def conectar_mongo():
   # Establece la conexión con MongoDB y retorna la colección.
   cliente = MongoClient(MONGO_URI)
   db = cliente[DATABASE_NAME]
   return db[COLLECTION_NAME]

def insertar_csv_a_mongo():
   # Lee el CSV e inserta los datos en MongoDB.
   try:
      collection = conectar_mongo()
      
      # Procesar cada archivo CSV
      for archivo in archivos_csv:
         ruta_completa = os.path.join(CSV_FOLDER, archivo)
         print(f"Procesando: {archivo}")

         # Leer el archivo CSV con pandas
         df = pd.read_csv(ruta_completa)

         # Convertir DataFrame a lista de diccionarios para MongoDB
         datos = df.to_dict(orient="records")

         # Insertar los datos en la colección
         if datos:
            collection.insert_many(datos)
            print(f"{len(datos)} registros insertados desde {archivo}")
         else:
            print(f"{archivo} está vacío. No se insertó nada.")
      print("Proceso completado.")

   except Exception as e:
      print(f"Error: {e}")
      
if __name__ == "__main__":
    insertar_csv_a_mongo()
