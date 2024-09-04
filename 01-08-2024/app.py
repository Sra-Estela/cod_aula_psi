from flask import Flask, session, request, render_template, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'superdificil'

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/login', methods=['POST','GET'])
def login():
    return 'OI'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else: 
        nome = request.form['nome']
        senha = request.form['senha']

        if nome == request.form['nome']:
            pass