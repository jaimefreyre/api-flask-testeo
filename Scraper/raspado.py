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


tt =''
bio = ''
img2 = ''
videos = []
link= ''
total = dict()
gbio = []
datosf = []

archi=open('serv-todo.js','a', encoding="utf-8-sig")
for (url, archivoNombre) in zip(catehome, csvlista):
	img1.clear()
	lincc.clear()
	matriz.clear()
	lincc.append(url)
	print(lincc)
	#input('este es el lincc')
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

	

	print(lincc)
	#input('Aca arranca el ciclo Art')

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









	print(archivoNombre)
	print(matriz)

	

	vcat = archivoNombre.split('.')
	print(vcat)
	print(vcat[0])
	categ = vcat[0]


	for (direcciones, mini) in zip(matriz, img1):
						# Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
		req = requests.get(direcciones)
		html = BeautifulSoup(req.text, "html.parser")
		mini2 = mini.replace('http://improntamusic.com/', 'img/grandes/')

		nombreartista = ''
		texto3 =  html.find_all(id='texto3')
		for s in texto3:
						for z in s.find_all('b'):
										titulosin = z.get_text()
										print(direcciones)
										titulo = titulosin.replace('Contratar a ', '')
										tip = titulo.replace(' ', '-') 
										tt = ""
										tt = titulo
										link = ""
										link = tip
										print(titulo)
										#data.append(titulo)


		tag =  html.find_all(id='imagengrande')
		for s in tag:
						for z in s.find_all('img'):
										imagensrc = z.get('src')
										#print(imagensrc)

										img2 = ""
										img2 = "http://improntamusic.com/" + imagensrc

		contrato =  'Queres contratar a ' + titulo
		cn2 = 'Contratar a' + titulo
		for s in texto3:
			p1 = s.find_all_next(string=True)
			juntadasbio = " ".join(p1)
			dat = juntadasbio.replace('Seguinos en   \n \n \n \n \n \n \n \n \n \n \n \n Contrata a tu artista preferido   \n\tcompletando el siguiente formulario \n \n \n \n \u00a0 \n \n Nombre: \n \n \n \n \n Email: \n \n \n \n Telefono: \n \n \n \n Artista: \n \n \n \n Mensaje: \n \n \n \n Enviar \n \n \n \n \u00a0 \n  Importamos libreria jQuery y nuestro script para validacion y envio \n \n \n \n   \n \n \n \n \n \n \n \n \n \ninfo@improntamusic.com // 549.1135245577 - 549.1169827881 // Av. Rivadavia 5361 - 6to Piso - Of. O - CABA \n\t\t \n \n \n', ' ') 
			comilla = dat.replace('"', '')
			direwall = comilla.replace('www.improntamusic.com', 'Wallgroup') 
			wallbio = direwall.replace('Impronta Music', 'Wallgroup')
			swd1 = wallbio.replace('Hace click aqui ', '')
			swd2 = swd1.replace('?', '')
			sw2 = swd2.replace('.', '. \n') 
			sw3 = sw2.replace('Queres  contratar a ', '')
			sw = sw3.replace('Contratar a ', '')
			bioengrup = sw.split('.')
			#print(bioengrup)
			gbio.clear()
						
			for a in bioengrup:
				gbio.append(a)
			bio = ""
			#bio = wallbio

		iframe = html.find_all('iframe', attrs={"height": "315"})
		videos.clear()
		for a in iframe:
			direifra = a.get('src')
			#print(direifra)
			videos.append(direifra)
		print(videos)
		#input('videos')

		model = ['titulo', 'Categoria', 'link', 'mini', 'imagen', 'videos', 'gbio']
		info = dict(zip(model,[tt, categ, link, mini, img2, videos, gbio]))
		dsf = json.dumps(info)
		#clave = '"' + tt  + '"' + ':'
		archi.write(dsf)
		archi.write(',')
		datosf.append(info)
		print('Se genero El diccionario', tt) 
		print('final for')

	
archi.close()