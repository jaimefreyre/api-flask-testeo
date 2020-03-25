import os
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, render_template, request

# instancia del objeto Flask
app = Flask(__name__)

# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './Archivos PDF'

@app.route('/')
def inicio():
	return jsonify({"mensaje": "Api rest hecha en Python Flask : Direcciones: /subir, /items, /item/<id>"})

@app.route("/subir")
def upload_file():
 # renderiamos la plantilla "forma1.html"
 return render_template('forma1.html')

@app.route("/upload", methods=['POST'])
def uploader():
 if request.method == 'POST':
  # obtenemos el archivo del input "archivo"
  f = request.files['archivo']
  filename = secure_filename(f.filename)
  # Guardamos el archivo en el directorio "Archivos PDF"
  f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  # Retornamos una respuesta satisfactoria
  return "<h1>Archivo subido exitosamente</h1>"

@app.route('/items')
def items():
  #returns the id
  return 'Items de una base de datos no conectada'

@app.route('/item/<id>')
def show_item(id):
  #returns the id
  return 'Id del Item es: %s' % id

if __name__ == '__main__':
	app.run(debug=True, port=8080)
