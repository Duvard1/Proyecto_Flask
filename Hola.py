#Importamos Flask
from flask import Flask, render_template

#Creamos aplicacion Flask 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Home')
def Home():
    return 'Pagina Home'