from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn

@app.route('/boxers', methods=['GET'])
def get_boxers():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM boxers;')
    boxers = cur.fetchall()
    cur.close()
    conn.close()
    
    return jsonify(boxers)

@app.route('/flask', methods=['GET'])
def flask_endpoint():
    return "Вечер в хату, Алексей Сергеевич!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)