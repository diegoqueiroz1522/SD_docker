from flask import Flask, jsonify
import psycopg2
import pymysql

app = Flask(__name__)

pg_connection = {
    'host': 'postgres',
    'port': 5432, 
    'database': 'mydb',
    'user': 'myuser',
    'password': 'mypassword',
}

mysql_connection = {
    'host': 'mysql',
    'port': 3306, 
    'database': 'mydb',
    'user': 'myuser',
    'password': 'mypassword',
}

@app.route('/')
def test():
    return 'test'


@app.route('/comidas', methods=['GET'])
def listar_comidas():
    conn = psycopg2.connect(**pg_connection)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comidas')
    comidas = cursor.fetchall()
    conn.close()
    return jsonify(comidas)

@app.route('/filmes', methods=['GET'])
def listar_filmes():
    conn = pymysql.connect(**mysql_connection)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM filmes')
    filmes = cursor.fetchall()
    conn.close()
    return jsonify(filmes)

if __name__ == '__main__':
    app.run(debug=True)
