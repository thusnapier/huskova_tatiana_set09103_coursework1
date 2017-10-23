# SET09103 - Advanced Web Technologies - Coursework 1 
# Student: 40207956

from flask import Flask, url_for, abort, jsonify, render_template
import json
app = Flask(__name__)

#Setup error handler route
@app.errorhandler(404)
def page_not_found(error):
  return "Page not found!", 404

#Setup homepage route localhost:5000
@app.route("/")
def homepage():
  #Details of each hall in a string
  data =[{
        'name':'Arran House', 
        'price':'146-270',
        'address':'5 Drysdale Road, EH3 9QJ',
        'rooms':'Double, Studio',
        'bathroom':'En-suite',
        'occupancy':'Single, Couples Studio only',
        'catering':'Self',
        'tenancy':'Long-term',
        'extras':'Free breakfast'
             },{
        'name':'Canal Point', 
        'price':'146-260',
        'address':'22 West Tollcross, EH3 9QW',
        'rooms':'Single, Double, Studio',
        'bathroom':'En-suite',
        'occupancy':'Single, Couples Studio only',
        'catering':'Self',
        'tenancy':'Long-term',
        'extras':'Free breakfast, TV'
             },{
        'name':'Gateaway Apartments',
        'price':'155',
        'address': '31 Montgomery Street, EH7 5JA',
        'rooms':'Double, Studios',
        'bathroom':'En-suite',
        'occupancy':'Single, Couples',
        'catering':'Self',
        'tenancy':'Long-term (51 weeks)',
        'extras':'Gym, Cinema, Study space'
             },{
        'name':'Haddington Place',
        'price':'160',
        'address':'Haddington Place, EH7 4AG',
        'rooms':'Double, Studio',
        'bathroom':'En-suite',
        'occupancy':'Single',
        'catering':'Self',
        'tenancy':'Long-term''
        'extras':'Gym, Study space, TV'
             },{
        'name':'iQ Fountainbridge',
        'price':'133',
        'address':'114 Dundee Street, EH3 8AA',
        'rooms':'Double, Studio',
        'bathroom':'En-suite',
        'occupancy':'Single, Couples',
        'catering':'Self',
        'tenancy':'Long-term (50 weeks)',
        'extras':'Gym, Games room, TV'
             },{
        'name':'iQ Grove',
        'price':'145',
        'address':'69 Grove Street, EH3 8FD'
             },{
        'name':'McDonald Road Studios',
        'price':'129',
        'address':'6 McDonald Road, EH7 4GT'
             },{
        'name':'The Mill House',
        'price':'142',
        'address':'392 Gorgie Road, EH11 2RN'
             },{
        'name':'New Park',
        'price':'131',
        'address':'Bothwell Street, EH7 5PX'
             },{
        'name':'Nido Haymarket',
        'price':'139',
        'address':'5 West Park, EH11 2EE'
             },{
        'name':'Potterrow',
        'price':'154',
        'address':'16-20 Potterrow, EH8 9PL'
             },{
        'name':'Pure Elliott House',
        'price':'160',
        'address':'8-10 Hillside Crescent, EH7 5EA'
             },{
        'name':'Student Castle Edinburgh',
        'price':'189',
        'address':'199 Causewayside, EH9 1PH'
        }]
  return render_template('template.html', info=data), 200

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
  start = '<img src="'
  url = url_for('static', filename='arran_house.jpg')
  end = '">'
  return start+url+end, 200

@app.route("/canal_point/")
def canal_point():
  start ='<img src="'
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

