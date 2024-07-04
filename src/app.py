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
                return redirect('/teams')
            else:
                # Ingresar flash
                return redirect('Error')
        except Exception as e:
            flash(f'el usuario {e} no se encontro')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        try:
            cur = db.connection.cursor()
            query = (
                'INSERT INTO users (username, password, email) VALUES (%s, %s, %s)')
            cur.execute(query, (username, password, email))
            db.connection.commit()
            cur.close()
            flash('Registro exitoso', 'succes')
        except Exception as e:
            flash(f'Error al registrar el usuario {e}')
            db.connection.rollback()
    return render_template('register.html')


@app.route('/teams')
def teams():
    return render_template('prueba_seleccion.html')


@app.route('/argentina_players')
def argentina_players():
    cur = db.connection.cursor()
    cur.execute(
        "SELECT name, position, age, height, weight, nationality FROM players")
    jugadores = cur.fetchall()
    cur.close()

    return render_template('/argentina_players.html', jugadores=jugadores)

@app.route('/argentina_home')
def argentina_home():
    return render_template('argentina_home.html')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
