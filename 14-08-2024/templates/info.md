# Aula - 14/08/2024 (PSI);
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/dash')
def dash():
	return render_template('dash.html')
```

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Templates</title>
    <style>
	* {
		box-sizing: border-box;
	}
	h1 {
		padding: 20px;
		text-align: center;
		background-color: blue;
		color: white;
	}
    </style>
</head>
<body>
	{% block titulo_pagina %}
	<h1> Templates </h1>
	{% endblock %}

	{% block conteudo %}
	<div>
		Conteúdo
	</div>
	{% endblock %}

	{% block conteudo %}

	<p>{{ nome }}</p>

	<ul>
		<ul>
			<li>Livro 1</li>
			<li>Livro 2</li>
			<li>Livro 3</li>
		</ul>
	</ul>
	{% endblock %}
</body>
</html>
```