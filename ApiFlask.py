from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
	return jsonify({"mensaje": "Api rest hecha en Python Flask : Direcciones: /pingo, /items, /item/<id>"})

@app.route('/pingo')
def pingo():
	return jsonify({"mensaje": "Api rest hecha en Python PINGO, desplegada para tester rapidos"})

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
