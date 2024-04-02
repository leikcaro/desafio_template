from string import Template
import requests
import json
from string import Template 

url = "https://aves.ninjas.cl/api/birds"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
# Convertimos la respuesta de texto a JSON
datos_aves = json.loads(response.text)
# Plantilla para el HTML de cada ave
plantilla_ave = Template("""
<div class="col-md-4">
    <div class="card" style="width: 18rem;">
        <img src="$url_imagen" class="card-img-top" alt="$nombre_espanol" height="300px">
        <div class="card-body">
            <h4 class="card-title">$nombre_espanol</h4>
            <p class="card-title">$nombre_ingles</p>
        </div>
    </div>
</div>
""")

# Inicio de la estructura HTML
html_inicio = """
<!DOCTYPE html>
<html lang='es'>
<head>
<h1>Aves de Chile</h1>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<!-- Autor -->
<meta name="author" content="Leik Caro">
<meta name="keywords" content="Viajes, excursion, aves">
<link rel="icon" href="assets/img/viajes.svg" type="image/x-icon">
</head>
<header>
    <title>Aves de Chile</title>
</header>
<body>
    <section class="container col-12 text-center d-none d-sm-block" id="pajarracos">
"""

# Fin de la estructura HTML
html_final = "</section></body>\n</html>"

# Generando el contenido de cada ave
contenido_aves = ''
for ave in datos_aves:  # Aquí, 'datos_aves' debe ser una lista de diccionarios.
    contenido_aves += plantilla_ave.substitute(
        nombre_espanol=ave['name']['spanish'],
        nombre_ingles=ave['name']['english'],
        url_imagen=ave['images']['full']
    )

# Combinando todo para formar el HTML completo
html_completo = html_inicio + contenido_aves + html_final

# Escribiendo `html_completo` a un archivo:
nombre_archivo = 'aves_de_chile.html'
with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
    archivo.write(html_completo)













