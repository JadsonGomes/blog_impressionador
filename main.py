from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta

app = Flask(__name__)

lista_usuarios = ['lira', 'joão', 'alon', 'Alesssandra', 'Amanda']

app.config['SECRET_KEY'] = '5b163219fce201b07ccc48e39db2da5d'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contatos")
def contato():
    return render_template('contatos.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login')
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', form_login=FormLogin, form_criarconta=FormCriarConta)


if __name__ == '__main__':
    # (debag = True // Faz o site atualizar altomaticamente.
    app.run(debug=True)
