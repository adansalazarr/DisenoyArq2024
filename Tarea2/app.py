from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

def validar_usuario(usuario):
    return usuario[0].isupper()

def validar_contraseña(contraseña):
    return any(char.isalpha() for char in contraseña) and any(char.isdigit() for char in contraseña)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        usuario = request.form['user']
        contraseña = request.form['pass']
        if validar_usuario(usuario) and validar_contraseña(contraseña):
            return render_template('login_success.html')
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
