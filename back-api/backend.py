from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'mysql-service'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

@app.route("/test", methods=['POST'])
def test():
    data = request.get_json()
    cur = mysql.connection.cursor()
    query = "INSERT INTO users (Id, name, email) VALUES (%s, %s, %s)"
    cur.execute(query, (data['Id'], data['nm'], data['nm1']))
    mysql.connection.commit()
    cur.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
