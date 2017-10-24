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
        'tenancy':'Long-term',
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
        'address':'69 Grove Street, EH3 8FD',
        'rooms':'Double, Studio',
        'bathroom':'En-suite',
        'occupnacy':'Single',
        'catering':'Self',
        'tenancy':'Long-term (43 weeks)',
        'extras':'Gym, Games room, TV'
             },{
        'name':'McDonald Road Studios',
        'price':'129',
        'address':'6 McDonald Road, EH7 4GT',
        'rooms':'Double',
        'bathroom':'En-suite',
        'occupancy':'Single',
        'catering':'Self',
        'tenancy':'Long-term (42 weeks)',
        'extras':'Games room, TV'
             },{
        'name':'The Mill House',
        'price':'142',
        'address':'392 Gorgie Road, EH11 2RN',
        'rooms':'Double, Studio',
        'bathroom':'En-suite',
        'occupancy':'Single, Couples Studio only',
        'catering':'Self',
        'tenancy':'Long-term',
        'extras':'Gym, Study room, TV'
             },{
        'name':'New Park',
        'price':'131',
        'address':'Bothwell Street, EH7 5PX',
        'rooms':'Double, Studio',
        'bathroom':'En-suite',
        'occupancy':'Single',
        'catering':'Self',
        'tenancy':'Long-term',
        'extras':'Games room, TV'
             },{
        'name':'Nido Haymarket',
        'price':'139',
        'address':'5 West Park, EH11 2EE',
        'rooms':'Single, Double, Studio',
        'bathroom':'En-suite',
        'occupancy':'Sinlge',
        'catering':'Self',
        'tenancy':'Long-term',
        'extras':'Housekeeping, Games room, TV'
             },{
        'name':'Potterrow',
        'price':'154',
        'address':'16-20 Potterrow, EH8 9PL',
        'rooms':'Double',
        'bathroom':'Shared',
        'occupancy':'Single',
        'catering':'Self',
        'tenancy':'Long-term (51 weeks)',
        'extras':'Housekeeping'
             },{
        'name':'Pure Elliott House',
        'price':'160',
        'address':'8-10 Hillside Crescent, EH7 5EA',
        'rooms':'Studio',
        'bathroom':'En-suite',
        'occupancy':'Single, Couples',
        'catering':'Self',
        'tenancy':'Long-term',
        'extras':'TV'
             },{
        'name':'Student Castle Edinburgh',
        'price':'189',
        'address':'199 Causewayside, EH9 1PH',
        'rooms':'Studio',
        'bathroom':'En-suite',
        'occupancy':'Single',
        'catering':'Self',
        'tenancy':'Long-term',
        'extras':'Gym'
        }]
  return render_template('template.html', info=data), 200

#To avoid hardcoding routes for every single house, we use a general path.
#This path generates data from JSON according to the name of house.
@app.route("/<name>/")
def location(name):
  data = {}
  print(name)
  with open('flatsdata.json') as infile:
  #Load data from JSON
    data = json.load(infile)
    infile.close()
    details = None
    #Format name of hall so that URL looks nice
    for o in data:
      formattedName = o['name']
      formattedName = formattedName.replace(' ', '_')
      formattedName = formattedName.lower()
      #Read data according to house selected
      if formattedName == name:
        details = o
  return render_template('details.html', details = details), 200

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

