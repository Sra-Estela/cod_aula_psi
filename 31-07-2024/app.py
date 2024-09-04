from flask import Flask, session, render_template, request, make_response

app = Flask(__name__)

# banco de dados
mensagens = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensagem')
def mensagem():
    return render_template('mensagem.html')

@app.route('/mural', methods=['GET', 'POST'])
def mural():

    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        if name in mensagens:
            mensagens[name].append(message)
        else:
            mensagens[name] = [message]
    
        if 'nome' in request.cookies and request.cookies['nome'] == name:
            return render_template('mural.html', lista=mensagens[name])
        else:
            template = render_template('mural.html', lista=mensagens[name])
            response = make_response(template)
            response.set_cookie(key='nome', value=name)
            return response

        return render_template('mural.html', lista=mensagens[name])
    return 'OI!'