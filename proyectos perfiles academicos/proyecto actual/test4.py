import json,os
import pandas as pd

def convertir_json_a_csv(json_filename, csv1_filename, csv2_filename, csv3_filename):
    # Leer el archivo JSON
    with open(json_filename, "r") as json_file:
        json_data = json.load(json_file)

    # Obtener el nombre del archivo JSON sin la extensión
    json_name = os.path.splitext(os.path.basename(json_filename))[0]    

    # Crear listas para almacenar los datos
    data_csv1 = []
    data_csv2 = []
    data_csv3 = []

    # Iterar sobre cada objeto en el JSON
    for obj in json_data:
        # Obtener los campos del objeto principal
        organization = obj.get("organization")
        scholar_id = obj.get("scholar_id")
        affiliation = obj.get("affiliation")
        email_domain = obj.get("email_domain")
        citedby = obj.get("citedby")
        interests = obj.get("interests")
        interests_sin_corchetes = ", ".join(interests).strip("[]")
        name = obj.get("name")
        id_institucion = json_name
        
        # Agregar los datos al primer archivo CSV
        data_csv1.append([organization, scholar_id, affiliation, id_institucion, email_domain, citedby, interests_sin_corchetes])
       
        # Obtener el diccionario interno "publications"
        publications = obj.get("publications", [])
        
        # Iterar sobre las publicaciones
        for publication in publications:
            # Obtener los campos de la publicación
            bib = publication.get("bib", {})
            title = bib.get("title")
            num_citations = publication.get("num_citations")
            pub_year = bib.get("pub_year")
    
            # Agregar los datos al segundo archivo CSV
            data_csv2.append([scholar_id, name, affiliation, email_domain, interests_sin_corchetes, title, num_citations, pub_year])
            
        coauthors = obj.get("coauthors",[])    

        for coauthor in coauthors:

            scholar_id_coauthor = coauthor.get("scholar_id")
            name_coauthor = coauthor.get("name")
            affiliation_coauthor = coauthor.get("affiliation")

            data_csv3.append([scholar_id, scholar_id_coauthor, name_coauthor, affiliation_coauthor])
    
    # Escribir los datos en los archivos CSV
    df_csv1 = pd.DataFrame(data_csv1, columns=["organization", "scholar_id", "affiliation","id_institucion","email_domain", "citedby", "interests"])
    df_csv1['organization'] = df_csv1['organization'].fillna(0).apply(int)
    df_csv1['citedby'] = df_csv1['citedby'].fillna(0).astype(int)
    df_csv1.to_csv(csv1_filename, index=False)

    df_csv2 = pd.DataFrame(data_csv2, columns=["scholar_id", "name", "affiliation", "email_domain", "interests", "title", "num_citations", "pub_year"])
    df_csv2.to_csv(csv2_filename, index=False)
    
    df_csv3 = pd.DataFrame(data_csv3, columns=["scholar_id_autor_gs", "scholar_id_gs_coauthor", "nombre_coauthor", "cargo"])
    df_csv3.to_csv(csv3_filename, index=False)
    

