from flask import Flask, render_template, request, json, url_for, redirect
from flaskext.mysql import MySQL
import plotly
#plotly.tools.set_credentials_file(username='ganeshcodes', api_key='9QIJefjnbz6Y0arQD7ww')
#import plotly.plotly as py
from plotly.offline import plot
import plotly.graph_objs as go
#py.sign_in('ganeshcodes', '9QIJefjnbz6Y0arQD7ww')

#kmeans imports
import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pylab as pl

app = Flask(__name__, static_url_path='')

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ganesh'
app.config['MYSQL_DATABASE_DB'] = 'clouddb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)


@app.route('/listcoursesform')
def listcoursesform():
    return render_template('listcourses.html', data=[])

@app.route('/listcourses', methods=['POST'])
def listcourses():
    # Get inputs from form
    day =  request.form['day']
    q = "select course from csefall where "+room+"='Y'"
    print(q)
    # execute and get results
    cursor = mysql.connect().cursor()
    cursor.execute(q)
    results = cursor.fetchall()
    resp = []
    for i in range(len(results)):
        resp.append(results[i][0])
    print(resp)
    return render_template('listcourses.html', data=resp)