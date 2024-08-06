import csv, os, time, csv, json
from scholarly import scholarly 

urls = []

def autorID(id_autor):
    time.sleep(2)
    try:

        search_query = scholarly.search_author_id(id_autor)
        autor = scholarly.fill(search_query,sections=[])
        autores = []
    
        for llave in autor:
            autores.append(autor[llave])
        print(autores)

        with open('test.json', 'a') as f:
            f.write(json.dumps(autor, indent=4, sort_keys=True))

    except Exception as e:
        print('Error',e)


# Directorio donde se encuentran los archivos CSV
directorio = 'C:/Users/krist/Desktop/proyecto/proyecto actual/AUTORESPORINSTITUCION'

# Obtener una lista de archivos en el directorio
archivos_csv = [archivo for archivo in os.listdir(directorio) if archivo.endswith('.csv')]

# Iterar sobre los archivos CSV
for archivo_csv in archivos_csv:
    ruta_completa = os.path.join(directorio, archivo_csv)
    print("Abriendo:", ruta_completa)
    try:
        with open(ruta_completa, newline='', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            # Iterar sobre las filas del archivo CSV
            for fila in lector_csv:
                urls.append(fila[1])
            #for fila in lector_csv:
                # Realizar las operaciones que necesites con cada fila
                #print(urls)

        for ids in urls:
            autorID(ids)
    
    except FileNotFoundError:
        print("El archivo CSV especificado no se encontró.")
    except Exception as e:
        print("Se produjo un error al abrir el archivo CSV:", e)
    


        

