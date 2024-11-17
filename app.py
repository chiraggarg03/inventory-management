import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

db_config = {
    'host': 'localhost',
    'user': 'guest',
    'password': 'password',
    'database': 'inventory_management'
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            quantity INT NOT NULL DEFAULT 0,
            price DECIMAL(10, 2) NOT NULL,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()


@app.route('/products', methods=['GET'])
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(products)


@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO products (name, description, quantity, price) VALUES (%s, %s, %s, %s)',
            (data['name'], data.get('description', ''),
             data['quantity'], data['price'])
        )
        conn.commit()
        product_id = cursor.lastrowid

        return jsonify({
            'id': product_id,
            'message': 'Product added successfully'
        }), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()


@app.route('/products/<int:product_id>/update-quantity', methods=['POST'])
def update_quantity(product_id):
    data = request.json
    quantity_change = data['quantity_change']

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            'SELECT quantity FROM products WHERE id = %s', (product_id,))
        current_quantity = cursor.fetchone()[0]
        new_quantity = current_quantity + quantity_change

        if new_quantity < 0:
            return jsonify({'error': 'Insufficient inventory'}), 400

        cursor.execute(
            'UPDATE products SET quantity = %s WHERE id = %s',
            (new_quantity, product_id)
        )

        conn.commit()
        return jsonify({
            'message': 'Quantity updated successfully',
            'new_quantity': new_quantity
        })
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
