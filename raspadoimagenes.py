# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import itertools
import csv
import numpy as np
import json

a11 =  "http://improntamusic.com/"
# Realizamos la petición a la web
req = requests.get(a11)
# Comprobamos que la petición nos devuelve un Status Code = 200
statusCode = req.status_code
# Links de paginacion
catehome = []

lincc = []
matriz = []
csvlista = []
img1 = []
def jsonDefault(object):
				return object.__dict__




home = BeautifulSoup(req.text, "html.parser")
seccion = home.find_all('a', attrs={"onmouseout": "MM_swapImgRestore()"})

for i in seccion:
				
				sd = i.get('href')
				if sd.startswith('http'):
								continue
				if sd.startswith('contratar'):
								continue
				if sd.startswith('coreografias'):
								direccion = 'http://improntamusic.com/' + sd
								archivo = sd + '.json'
								catehome.append(direccion)
								csvlista.append(archivo)
								listadarchivos = open('diresderaspado.txt','a')
								listadarchivos.write("/".join(csvlista))
								listadarchivos.close()
								break
				else:
								direccion = 'http://improntamusic.com/' + sd
								archivo = sd + '.json'
								catehome.append(direccion)
								csvlista.append(archivo)
								
print(catehome)
print(csvlista)



for (url, archivoNombre) in zip(catehome, csvlista):
	img1.clear()
	lincc.clear()
	matriz.clear()
	print(lincc)
	while url != True:
					# Realizamos la petición a la web
					req = requests.get(url)
					# Comprobamos que la petición nos devuelve un Status Code = 200
					statusCode = req.status_code
					if statusCode == 200:
									# Links de paginacion
									print(url)
									html = BeautifulSoup(req.text, "html.parser")
									articulotodo = html.find_all(id='flechas')
									for i in articulotodo:
													for j in i.find_all('a'):
																	linkpage = j.get('href')
																	dires = 'http://improntamusic.com/' + linkpage
									if lincc.count(dires) == 1:
													break       
									lincc.append(dires)
									url = dires     
					else:
									print(statusCode)
									break


	for art in lincc:
					req = requests.get(art)
					html = BeautifulSoup(req.text, "html.parser")
					tag = html.find_all(id='imagen')
					
					for i in tag:
									for j in i.find_all('a'):
													links = j.get('href')
													dires = 'http://improntamusic.com/' + links
													matriz.append(dires)

					for i in tag:
									for j in i.find_all('img'):
													links = j.get('src')
													im = 'http://improntamusic.com/' + links
													img1.append(im)





	tt =''
	bio = ''
	img2 = ''
	videos = ''
	total = dict()
	datosf = [] 





	print(archivoNombre)
	print(matriz)

	

	archi=open(archivoNombre,'a', encoding="utf-8-sig")
	


	for (direcciones, mini) in zip(matriz, img1):
						# Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
		req = requests.get(direcciones)
		html = BeautifulSoup(req.text, "html.parser")
		#mini2 = mini.replace('http://improntamusic.com/', 'img/grandes/')

		nombreartista = ''
		texto3 =  html.find_all(id='texto3')
		for s in texto3:
						for z in s.find_all('b'):
										titulo = z.get_text()
										print(direcciones)
										tt = ""
										tt = titulo
										print(titulo)
										#data.append(titulo)


		tag =  html.find_all(id='imagengrande')
		for s in tag:
						for z in s.find_all('img'):
										imagensrc = z.get('src')
										#print(imagensrc)

										img2 = ""
										img2 = "http://improntamusic.com/" + imagensrc


		

		model = ['titulo', 'mini', 'imagen']
		info = dict(zip(model,[tt, mini, img2]))
		dsf = json.dumps(info)
		#clave = '"' + tt  + '"' + ':'
		archi.write(dsf)
		archi.write(',')
		datosf.append(info)
		print('Se genero El diccionario', tt) 
		print('final for')

	
	archi.close()