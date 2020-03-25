import os
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, render_template, request, session
import verifi 
from flask_login import login_required

##############################################################
# instancia del objeto Flask
app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './ArchivosPDF'
# Sesion
app.secret_key = 'app secret key'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return 'Ingresos registrados en sesion: '+str(session['counter'])
	# return jsonify({"mensaje": "Api rest hecha en Python Flask : Direcciones: /subir, /items, /item/<id>"})

@app.route('/items')
def items():
  #returns the id
  return 'Items de una base de datos no conectada'

@app.route('/item/<id>')
def show_item(id):
  #returns the id
  return 'Id del Item es: %s' % id


###########################################################
#Carga de Archivos
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

################################################################
#Login
#libreria de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
    
    # Se construye a traves de validacion cliente un objeto LoginForm
    # form = LoginForm()
    # if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        # login_user(user)

        # flask.flash('Logged in successfully.')

        # next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        # if not is_safe_url(next):
            # return flask.abort(400)

        # return flask.redirect(next or flask.url_for('index'))
    # return flask.render_template('login.html', form=form)


@app.route("/settings")
# @login_required
def settings():
	pass







if __name__ == '__main__':
	app.run(debug=True, port=8080)
