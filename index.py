# SET09103 - Advanced Web Technologies - Coursework 1 
# Student: 40207956

from flask import Flask
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
  return "Page not found!", 404
  
if __name__ == "__main__"
  app.run(host='0.0.0.0', debug=True)

