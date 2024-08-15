from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def create_db():
    # Replace with your MySQL credentials
    mydb = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )
    mycursor = mydb.cursor()
    mycursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        username VARCHAR(255) UNIQUE,
                        password VARCHAR(255)
                    )''')
    mydb.commit()
    mydb.close()

create_db()

@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']

    mydb = mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_database"
    )
    mycursor = mydb.cursor()

    try:
        mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mydb.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except mysql.connector.errors.IntegrityError:
        return jsonify({'message': 'Username already exists'}), 400
    finally:
        mydb.close()

if __name__ == '__main__':
    app.run(debug=True)