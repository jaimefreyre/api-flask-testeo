import os
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, render_template, request
from verifi import login_manager

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


#libreria de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)




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
