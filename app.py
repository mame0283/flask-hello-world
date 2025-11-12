from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Maxwell in 3308'

@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://lab_10_db_hfq4_user:YLAQC2BuNFp7SOY4pxJucdC9DTsYPupe@dpg-d49t02q4d50c739lkfb0-a/lab_10_db_hfq4")
    conn.close()
    return "Database Connection Succesful"
