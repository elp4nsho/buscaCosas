
from lxml import html
import requests

import csv


from csv import writer
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:

        #Create a writer object from csv module
        csv_writer = writer(write_obj)
# Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


details = ["price__fraction","main-title"]
elementos = 10

with open('listadoObjetos.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for listado in csv_reader:
        append_list_as_row("Resultados_mercadoLibre.csv",['Nombre buscado','Nombre comercial', 'Precio','Link'])
        for nombre in listado:
            print(nombre)
            pagina = requests.get(f'https://listado.mercadolibre.cl/{nombre}')
            arbol = html.fromstring(pagina.content)
            detallesACSV = []

            precios = arbol.xpath("//span[@class='%s']/text()" % "price__fraction")
            nombres = arbol.xpath("//span[@class='%s']/text()" % "main-title")
            links = arbol.xpath("//a[@class='figure item-image item__js-link']")

            print(f'Resultados: {elementos}')
            for i in range(elementos):
                    #l = links[i].get("href")   #imprimir vendidos
                    #a = html.fromstring(requests.get(l).content) #imprimir vendidos
                    #print("".join(a.xpath("//div[@class='item-conditions']/text()")).strip()) #imprimir vendidos
                    append_list_as_row("Resultados_mercadoLibre.csv",[nombre,nombres[i], precios[i],links[i].get("href")])
            #append_list_as_row("employee_file.csv",['Nombre buscado','Nombre comercial', 'Precio'])

                #employee_writer.writerow(['Nombre buscado','Nombre comercial', 'Precio'])
                #employee_writer.writerow(detallesACSV)
                #for i in range(len(precios)):
                    #employee_writer.writerow([nombre,nombres[i], precios[i]])





