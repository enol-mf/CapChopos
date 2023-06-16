from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de usuarios válidos
valid_users = [
    {'username': 'admin', 'password': 'admin',
     'username': 'alex', 'password': 'alex',
     'username': 'jessica', 'password': 'jessica',
     'username': 'juanca', 'password': 'juanca',
     'username': 'enolf', 'password': 'enolf',
     'username': 'cortina', 'password': 'cortina',
     'username': 'david', 'password': 'david',
     'username': 'enolm', 'password': 'enolm',
     'username': 'david', 'password': 'david',
     
     }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form_login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificar las credenciales del usuario
        for user in valid_users:
            if username == user['username'] and password == user['password']:
                # Credenciales válidas, redireccionar a la página de inicio
                return redirect('/home')

        # Credenciales inválidas, mostrar mensaje de error en la misma página de inicio de sesión
        error_message = 'Credenciales inválidas. Inténtalo de nuevo.'
        return render_template('login.html', error=error_message)

    return render_template('login.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()