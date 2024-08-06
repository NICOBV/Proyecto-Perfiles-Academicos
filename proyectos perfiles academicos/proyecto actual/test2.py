from test4 import *
import os

archivos_json = ["uadolfoi.json","autonoma.json","pucv.json","santotomas.json","uach.json","uahurtado.json","uandes.json",
                 "uantof.json","ubiobio.json","uc.json","uchile.json","ucm.json","ucn.json","ucsc.json","uct.json","udd.json",
                 "udec.json","udp.json","ufrontera.json","ulagos.json","umag.json","unab.json","unap.json","upla.json","usach.json",
                 "userena.json","usm.json","uss.json","uta.json","utalca.json","uv.json"]

for json_filename in archivos_json:

    csv1_filename = f"CSV_AUTOR_{os.path.splitext(json_filename)[0]}.csv"
    csv2_filename = f"CSV_ARTICULO_{os.path.splitext(json_filename)[0]}.csv"
    csv3_filename = f"CSV_COAUTOR_{os.path.splitext(json_filename)[0]}.csv"
    
    convertir_json_a_csv(json_filename, csv1_filename, csv2_filename, csv3_filename)