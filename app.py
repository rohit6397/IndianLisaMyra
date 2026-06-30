from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

import sqlite3

app = Flask(__name__)


def init_db():

    conn = sqlite3.connect('users.db')

    cur = conn.cursor()

    cur.execute(

        '''

        CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT,

        phone TEXT,

        username TEXT,

        password TEXT

        )

        '''

    )

    conn.commit()

    conn.close()


init_db()


@app.route('/')

def home():

    return render_template('index.html')


@app.route('/register',

methods=['GET','POST'])

def register():

    if request.method == 'POST':

        name = request.form['name']

        email = request.form['email']

        phone = request.form['phone']

        username = name.lower().replace(" ","")

        password = username + "@#$"

        conn = sqlite3.connect(

            'users.db'

        )

        cur = conn.cursor()

        cur.execute(

            '''

            INSERT INTO users

            (

            name,

            email,

            phone,

            username,

            password

            )

            VALUES

            (?,?,?,?,?)

            ''',

            (

            name,

            email,

            phone,

            username,

            password

            )

        )

        conn.commit()

        conn.close()

        return """

        <h1>

        Registration Successful

        </h1>

        <h2>

        Please Login To Continue

        </h2>

        <br>

        <a href='/login'>

        Login

        </a>

        """

    return render_template(

        'register.html'

    )


@app.route('/login',

methods=['GET','POST'])

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        conn = sqlite3.connect(

            'users.db'

        )

        cur = conn.cursor()

        cur.execute(

            '''

            SELECT *

            FROM users

            WHERE username=?

            AND password=?

            ''',

            (

            username,

            password

            )

        )

        user = cur.fetchone()

        conn.close()

        if user:

            return redirect(

                '/membership'

            )

        else:

            return '''

            <h1>

            Invalid Credentials

            </h1>

            <a href="/login">

            Try Again

            </a>

            '''

    return render_template(

        'login.html'

    )


@app.route('/membership')

def membership():

    return render_template(

        'membership.html'

    )


@app.route('/payment')

def payment():

    return render_template(

        'payment.html'

    )


@app.route('/success')

def success():

    return render_template(

        'success.html'

    )


if __name__ == "__main__":

    app.run(

        host='0.0.0.0',

        port=5000,

        debug=True

    )
