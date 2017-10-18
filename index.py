# SET09103 - Advanced Web Technologies - Coursework 1 
# Student: 40207956

from flask import Flask, url_for, abort, jsonify
import json
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
  return "Page not found!", 404

@app.route("/")
def homepage():
  return """
<!DOCTYPE html>
<heIad>
  <title>Coursework 1 - 40207956</title>
  <link rel="stylesheet" href="./static/style.css">
</head>
<body style="width: auto; margin: auto;">
  <h1>Private accommodation for students in Edinburgh.</h1>
  <h2><a href="localhost:5000/arran_house/">Arran House</a></h2>
  <img src="static/arran_house.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/canal_point/">Canal Point</a></h2>
  <img src="static/canal_point.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/gateaway/">Gateaway Apartments</a></h2>
  <img src="static/gateaway_apartments.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/haddington/>Haddington Place</a></h2>
  <img src="static/haddington_place.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/iqfountain/">iQ Fountainbridge</a></h2>
  <img src="static/iqfountainbridge.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/iqgrove/">iQ Grove</a></h2>
  <img src="static/iqgrove.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/mcdonald/">McDonald Road</a></h2>
  <img src="static/mcdonald.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/millhouse/>Mill House</a></h2>
  <img src="static/mill_house.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/newpark/>New Park</a></h2>
  <img src="static/new_park.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/nido/">Nido Haymarket</a></h2>
  <img src="static/nido.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/potterrow/">Potterrow</a></h2>
  <img src="static/potterrow.jpg" style="width:300px;height:200px;">
  <h2><a href="localhost:5000/elliott/">Pure Elliott House</a></h2>
  <img src="static/pure_elliott.jpg" style="width:300px;heigth:200px;">
  <h2><a href="localhost:5000/studentcastle/">Student Castle</a></h2>
  <img src="static/student_castle.jpg" style="width:300px;height:200px;">
</body>
"""

@app.route("/arran_house/")
def arran_house():
  start = '<img src="'
  url = url_for('static', filename='arran_house.jpg')
  end = '">',
  d = json.load(open("flatsdata.json"))
  print d["Arran House"]
  return start+url+end+d, 200

@app.route("/canal_point/")
def canal_point():
  start = '<img src="'
  url = url_for('static', filename='canal_point.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/gateaway/")
def gateaway():
  start = '<img src="'
  url = url_for('static', filename='gateaway_apartments.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/haddington/")
def haddington():
  start = '<img src="'
  url = url_for('static', filename='haddington_place.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/iqfountain/")
def iqfountain():
  start = '<img src="'
  url = url_for('static', filename='iqfountainbridge.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/iqgrove/")
def iqgrove():
  start = '<img src="'
  url = url_for('static', filename='iqgrove.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/mcdonald/")
def mcdonald():
  start = '<img src="'
  url = url_for('static', filename='mcdonald.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/millhouse/")
def millhouse():
  start = '<img src="'
  url = url_for('static', filename='mill_house.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/newpark/")
def newpark():
  start = '<img src="'
  url = url_for('static', filename='new_park.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/nido/")
def nido():
  start = '<img src="'
  url = url_for('static', filename='nido.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/potterrow/")
def potterrow():
  start = '<img src="'
  url = url_for('static', filename='potterrow.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/elliott/")
def elliott():
  start = '<img src="'
  url = url_for('static', filename='pure_elliott.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/studentcastle/")
def studentcastle():
  start = '<img src="'
  url = url_for('static', filename='student_castle.jpg')
  end = '">'
  return start+url+end, 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

