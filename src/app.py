from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

db = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = db.connection.cursor()
        query = 'SELECT * FROM users WHERE username = %s AND password = %s'
        cur.execute(query, (username, password))
        user = cur.fetchone()
        cur.close()

        try:
            if user:
                # Ingresar flash
                return redirect('Bienvenido')
            else:
                # Ingresar flash
                return redirect('Error')
        except Exception as e:
            flash(f'el usuario {e} no se encontro')
    return render_template('login.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
