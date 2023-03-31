from typing import List, Dict
from flask import Flask,render_template, redirect, url_for, request
import mysql.connector
import json

app = Flask(__name__)

def test_table() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM test_table')
    results = [{login: mdp} for (login, mdp) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route('/')
def index():
   return render_template('index.html',text=test_table())
# Route for handling the login page logic
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         if test_table("admin","admin").length==0:
#             error = 'Mdp ou login incorrect'
#         else:
#             error='Felicitation'+request.form['username']
#     return render_template('index.html', error=error)
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    go=None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            go = 'Felicitation '+request.form['username'] 
    return render_template('index.html', error=error,go=go)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
