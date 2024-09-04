from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index ():

    if 'color' in request.cookies:
        return render_template('index.html', cor=request.cookies['color'])
    return render_template('index.html', cor='white')

@app.route('/color')
def color():
    cor = request.args.get('color')

    if 'color' in request.cookies:
        if cor != request.cookies['color']:
            template = render_template('color.html', cor=cor)
            response = make_response(template)
            response.delete_cookie('color')
            response.set_cookie('color', value=cor)
            return response
        else:
            return render_template('color.html', cor=request.cookies['color'])
    else:
        template = render_template('color.html', cor=cor)
        response = make_response(template)
        response.delete_cookie('color')
        response.set_cookie('color', cor=cor)
        return response

    return render_template('color.html', request.cookie['color'])