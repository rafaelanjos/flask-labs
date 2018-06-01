from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length, Email

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = '0ba168f0e6a1487f91ee3dc2c2715ee6'

class ContatoForm(Form):
    message_length = 'O campo deve ter entre %(min)d à %(max)d caracteres.'
    name = StringField('Nome', validators=[Required('Informe o seu nome'), Length(3, 100, message_length)])
    email = StringField('Email', validators=[Required('Informe o seu email'),Email('Email inválido'), Length(5, 100,message_length)])
    assunto = StringField('Assunto', validators=[Required('Informe o assunto'), Length(5, 100,message_length)])
    mensagem = StringField('Mensagem', validators=[Required('Informe o mensagem'), Length(3, 5000,message_length)])
    submit = SubmitField('Enviar')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = ContatoForm()
    print('Valid form ',form.validate_on_submit())
    #  if form.validate_on_submit():
    #     name = form.name.data
    #     form.name.data = ''

    return render_template('index.html',form=form,)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 

# apecnascimento/Happy-Flasker
# https://github.com/apecnascimento/Happy-Flasker

# WTForms Documentation
# https://wtforms.readthedocs.io/en/stable/validators.html#built-in-validators

# flask-mail — Flask-Mail 0.9.1 documentation
# https://pythonhosted.org/Flask-Mail/

# Shutdown telemetria windows
#https://gist.github.com/jumarag/738fd121c8f3a37cc6240993853a6977