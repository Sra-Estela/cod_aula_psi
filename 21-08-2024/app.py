from flask import Flask, url_for, \
    request, render_template, flash, redirect
import sqlite3

app = Flask(__name__)

def get_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    users = []
    conn = get_connection()
    users = conn.execute('SELECT id, email FROM users').fetchall()
    return render_template('pages/index.html', users=users)

@app.route('/creat', methods=['GET', 'POST'])
def create():

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']
        if not email:
            flash ('Email é obrigatório')
        
        else:
            conn = get_connection()
            conn.execute("INSERT INTO users (email, senha) VALUES(?,?)", (email, senha))
            conn.commit()
            conn.close()
            return redirect(url_for('index.html'))

    return render_template('pages/create.html')

@app.route('/<int:id>/edit')
def edit(id):
    return str(id)