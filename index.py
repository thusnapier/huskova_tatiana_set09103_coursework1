# SET09103 - Advanced Web Technologies - Coursework 1 
# Student: 40207956

from flask import Flask, url_for, abort
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
  return "Page not found!", 404

@app.route("/")
def title():
  return "Private accommodation for students in Edinburgh."

@app.route('/arran_house/')
def arran_house():
  start = '<img src="'
  url = url_for('static', filename='arran_house.jpg')
  end = '">'
  return start+url+end, 200
  
if __name__ == "__main__"
  app.run(host='0.0.0.0', debug=True)

