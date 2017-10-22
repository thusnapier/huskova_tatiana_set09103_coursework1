# SET09103 - Advanced Web Technologies - Coursework 1 
# Student: 40207956

from flask import Flask, url_for, abort, jsonify, render_template
import json
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
  return "Page not found!", 404

@app.route("/")
def homepage(Name=None, Price=None):
  return render_template('template.html'), 200

@app.route("/<name>")
def location(name):
  data = {}
  with open('flatsdata.json') as infile:
    data = json.load(infile)
    infile.close()
  print data[name]
  return json.dumps(data[name]), 200

@app.route("/arran_house/")
def arran_house():
 # start = '<img src="'
 # url = url_for('static', filename='arran_house.jpg')
 # end = '">',
  data = {}
  with open('flatsdata.json') as infile:
    data = json.load(infile)
    infile.close()
  print data['arran_house']
 # return start+url+end, 200
  return json.dumps(data['arran_house']), 200 

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

