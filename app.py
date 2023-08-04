from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Nskr@5411',
            database='my'
        )
        cursor = cnx.cursor()

        # Insert the user data into the database
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(query, values)

        cnx.commit()
        cursor.close()
        cnx.close()

        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Nskr@5411',
            database='my'
        )
        cursor = cnx.cursor()

        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            # Store the user ID in the session
            session['user_id'] = user[0]
            return redirect('/welcome')
        else:
            return render_template('login.html', error='Invalid credentials')

        cursor.close()
        cnx.close()

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'user_id' in session:
        return render_template('welcome.html')
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(port=8080, debug=True)
