# app.py
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'localhost',
    'database': 'sys',
    'user': 'root',
    'password': '987654321',
}


def insert_memorial_data(name, phone, relation, image, tribute, condolence):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "INSERT INTO memorials (name, phone, relation, image, tribute, condolence) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, phone, relation, image, tribute, condolence)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()
    except Error as e:
        print("Error while connecting to MySQL:", e)


@app.route('/', methods=['GET', 'POST'])
def memorial_form():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        relation = request.form['relation']
        image = request.files['image'].read()
        tribute = request.form['tribute']
        condolence = request.form['condolence']

        # Save memorial data to MySQL database
        insert_memorial_data(name, phone, relation, image, tribute, condolence)

        return redirect(url_for('thank_you'))

    return render_template('index.html')


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

# app.py

# ... (previous imports and configurations)

@app.route('/obituary')
def obituary_page():
    return render_template('obituary.html')

@app.route('/service')
def service_page():
    return render_template('service.html')

@app.route('/gallery')
def gallery_page():
    return render_template('gallery.html')

@app.route('/zelly_foundation')
def zelly_foundation_page():
    return render_template('zelly_foundation.html')

@app.route('/buy_flowers')
def buy_flowers_page():
    return render_template('buy_flowers.html')

# ... (existing routes and app.run() statement)


if __name__ == '__main__':
    app.run(debug=True)
