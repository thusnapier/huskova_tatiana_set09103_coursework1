# SET09103 - Advanced Web Technologies - Coursework 1 
# Student: 40207956

from flask import Flask, url_for, abort
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
  return "Page not found!", 404

@app.route("/")
def homepage():
  return """
<!DOCTYPE html>
<head>
  <title>Coursework 1</title>
  <link rel="stylesheet" href="./css/style.css">
</head>
<body style="width: auto; margin: auto;">
  <h1>Private accommodation for students in Edinburgh.</h1>
  <h2>Arran House</h2>
  <img src="https://github.com/thusnapier/huskova_tatiana_set09103_coursework1/blob/master/static/arran_house.jpg">
</body>
"""

@app.route('/arran_house/')
def arran_house():
  start = '<img src="'
  url = url_for('static', filename='arran_house.jpg')
  end = '">'
  return start+url+end, 200
  
if __name__ == "__main__"
  app.run(host='0.0.0.0', debug=True)

