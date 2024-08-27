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
                return redirect('/')
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


@app.route('/argentina_players')
def argentina_players():
    cur = db.connection.cursor()
    cur.execute(
        "SELECT fullname, age, height, nationality, position, foot, goal, asis, yellow_card, red_card, image FROM arg_players")
    jugadores = cur.fetchall()
    cur.close()
    jugadores_dict = [
        {
            'fullname': row[0] if row[0] is not None else '',
            'age': row[1] if row[1] is not None else '',
            'height': row[2] if row[2] is not None else '',
            'nationality': row[3] if row[3] is not None else '',
            'position': row[4] if row[4] is not None else '',
            'foot': row[5] if row[5] is not None else '',
            'goal': row[6] if row[6] is not None else '',
            'asis': row[7] if row[7] is not None else '',
            'yellow_card': row[8] if row[8] is not None else '',
            'red_card': row[9] if row[9] is not None else '',
            'image': row[10] if row[10] is not None else 'default_image.jpg'
        }
        for row in jugadores
    ]

    return render_template('argentina_players.html', jugadores=jugadores_dict)


@app.route('/brasil_players')
def brasil_players():
    cur = db.connection.cursor()
    cur.execute(
        "SELECT fullname, age, height, nationality, position, foot, goal, asis, yellow_card, red_card, image FROM bra_players")
    jugadores = cur.fetchall()
    cur.close()
    jugadores_dict = [
        {
            'fullname': row[0] if row[0] is not None else '',
            'age': row[1] if row[1] is not None else '',
            'height': row[2] if row[2] is not None else '',
            'nationality': row[3] if row[3] is not None else '',
            'position': row[4] if row[4] is not None else '',
            'foot': row[5] if row[5] is not None else '',
            'goal': row[6] if row[6] is not None else '',
            'asis': row[7] if row[7] is not None else '',
            'yellow_card': row[8] if row[8] is not None else '',
            'red_card': row[9] if row[9] is not None else '',
            'image': row[10] if row[10] is not None else 'default_image.jpg'
        }
        for row in jugadores
    ]

    return render_template('brasil_players.html', jugadores=jugadores_dict)


@app.route('/uruguay_players')
def uruguay_players():
    cur = db.connection.cursor()
    cur.execute(
        "SELECT fullname, age, height, nationality, position, foot, goal, asis, yellow_card, red_card, image FROM uru_players")
    jugadores = cur.fetchall()
    cur.close()
    jugadores_dict = [
        {
            'fullname': row[0] if row[0] is not None else '',
            'age': row[1] if row[1] is not None else '',
            'height': row[2] if row[2] is not None else '',
            'nationality': row[3] if row[3] is not None else '',
            'position': row[4] if row[4] is not None else '',
            'foot': row[5] if row[5] is not None else '',
            'goal': row[6] if row[6] is not None else '',
            'asis': row[7] if row[7] is not None else '',
            'yellow_card': row[8] if row[8] is not None else '',
            'red_card': row[9] if row[9] is not None else '',
            'image': row[10] if row[10] is not None else 'default_image.jpg'
        }
        for row in jugadores
    ]

    return render_template('uruguay_players.html', jugadores=jugadores_dict)


@app.route('/mexico_players')
def mexico_players():
    cur = db.connection.cursor()
    cur.execute(
        "SELECT fullname, age, height, nationality, position, foot, goal, asis, yellow_card, red_card, image FROM mex_players")
    jugadores = cur.fetchall()
    cur.close()
    jugadores_dict = [
        {
            'fullname': row[0] if row[0] is not None else '',
            'age': row[1] if row[1] is not None else '',
            'height': row[2] if row[2] is not None else '',
            'nationality': row[3] if row[3] is not None else '',
            'position': row[4] if row[4] is not None else '',
            'foot': row[5] if row[5] is not None else '',
            'goal': row[6] if row[6] is not None else '',
            'asis': row[7] if row[7] is not None else '',
            'yellow_card': row[8] if row[8] is not None else '',
            'red_card': row[9] if row[9] is not None else '',
            'image': row[10] if row[10] is not None else 'default_image.jpg'
        }
        for row in jugadores
    ]

    return render_template('mexico_players.html', jugadores=jugadores_dict)


@app.route('/canada_players')
def canada_players():
    cur = db.connection.cursor()
    cur.execute(
        "SELECT fullname, age, height, nationality, position, foot, goal, asis, yellow_card, red_card, image FROM can_players")
    jugadores = cur.fetchall()
    cur.close()
    jugadores_dict = [
        {
            'fullname': row[0] if row[0] is not None else '',
            'age': row[1] if row[1] is not None else '',
            'height': row[2] if row[2] is not None else '',
            'nationality': row[3] if row[3] is not None else '',
            'position': row[4] if row[4] is not None else '',
            'foot': row[5] if row[5] is not None else '',
            'goal': row[6] if row[6] is not None else '',
            'asis': row[7] if row[7] is not None else '',
            'yellow_card': row[8] if row[8] is not None else '',
            'red_card': row[9] if row[9] is not None else '',
            'image': row[10] if row[10] is not None else 'default_image.jpg'
        }
        for row in jugadores
    ]

    return render_template('canada_players.html', jugadores=jugadores_dict)


@app.route('/usa_players')
def usa_players():
    cur = db.connection.cursor()
    cur.execute(
        "SELECT fullname, age, height, nationality, position, foot, goal, asis, yellow_card, red_card, image FROM usa_players")
    jugadores = cur.fetchall()
    cur.close()
    jugadores_dict = [
        {
            'fullname': row[0] if row[0] is not None else '',
            'age': row[1] if row[1] is not None else '',
            'height': row[2] if row[2] is not None else '',
            'nationality': row[3] if row[3] is not None else '',
            'position': row[4] if row[4] is not None else '',
            'foot': row[5] if row[5] is not None else '',
            'goal': row[6] if row[6] is not None else '',
            'asis': row[7] if row[7] is not None else '',
            'yellow_card': row[8] if row[8] is not None else '',
            'red_card': row[9] if row[9] is not None else '',
            'image': row[10] if row[10] is not None else 'default_image.jpg'
        }
        for row in jugadores
    ]

    return render_template('usa_players.html', jugadores=jugadores_dict)


@app.route('/argentina_stats')
def obtener_estadisticas_arg():
    cur = db.connection.cursor()
    cur.execute("SELECT nombre, partidos_jugados, ganados, perdidos, empatados, goles_favor, goles_contra FROM estadisticas_copa_america WHERE nombre = 'Argentina'")
    estadisticas = cur.fetchone()
    cur.close()

    return render_template('argentina_stats.html', estadisticas=estadisticas)


@app.route('/brasil_stats')
def obtener_estadisticas_bra():
    cur = db.connection.cursor()
    cur.execute("SELECT nombre, partidos_jugados, ganados, perdidos, empatados, goles_favor, goles_contra FROM estadisticas_copa_america WHERE nombre = 'Brasil'")
    estadisticas = cur.fetchone()
    cur.close()

    return render_template('brasil_stats.html', estadisticas=estadisticas)


@app.route('/uruguay_stats')
def obtener_estadisticas_uru():
    cur = db.connection.cursor()
    cur.execute("SELECT nombre, partidos_jugados, ganados, perdidos, empatados, goles_favor, goles_contra FROM estadisticas_copa_america WHERE nombre = 'Uruguay'")
    estadisticas = cur.fetchone()
    cur.close()

    return render_template('uruguay_stats.html', estadisticas=estadisticas)


@app.route('/mexico_stats')
def obtener_estadisticas_mex():
    cur = db.connection.cursor()
    cur.execute("SELECT nombre, partidos_jugados, ganados, perdidos, empatados, goles_favor, goles_contra FROM estadisticas_copa_america WHERE nombre = 'Mexico'")
    estadisticas = cur.fetchone()
    cur.close()

    return render_template('mexico_stats.html', estadisticas=estadisticas)


@app.route('/usa_stats')
def obtener_estadisticas_usa():
    cur = db.connection.cursor()
    cur.execute("SELECT nombre, partidos_jugados, ganados, perdidos, empatados, goles_favor, goles_contra FROM estadisticas_copa_america WHERE nombre = 'Estados_Unidos'")
    estadisticas = cur.fetchone()
    cur.close()

    return render_template('usa_stats.html', estadisticas=estadisticas)


@app.route('/canada_stats')
def obtener_estadisticas_can():
    cur = db.connection.cursor()
    cur.execute("SELECT nombre, partidos_jugados, ganados, perdidos, empatados, goles_favor, goles_contra FROM estadisticas_copa_america WHERE nombre = 'Canada'")
    estadisticas = cur.fetchone()
    cur.close()

    return render_template('canada_stats.html', estadisticas=estadisticas)


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
