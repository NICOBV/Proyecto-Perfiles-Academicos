from scholarly import scholarly 
import time,csv,json

urls = []
nombres = []


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

with open('C:/Users/krist/Desktop/proyecto/proyecto actual/AUTORESPORINSTITUCION/autonoma.csv',encoding='utf8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        urls.append(row['id_autor_gs'])

for ids in urls:
    autorID(ids)
   






    
    