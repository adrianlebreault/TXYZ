<<<<<<< HEAD
from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

# Configuración de la conexión a la base de datos MySQL
db_host = 'localhost'
db_user = 'root'
db_password = 'root'
db_name = 'tallerxyzdb'

def get_db_connection():
    return pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        return jsonify(clientes)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()

@app.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.get_json()
    nombre = data['nombre']
    correo = data['correo']
    telefono = data['telefono']
    direccion = data['direccion']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO clientes (nombre, correo, telefono, direccion) VALUES (%s, %s, %s, %s)", (nombre, correo, telefono, direccion))
        connection.commit()
        return jsonify({"message": "Cliente creado correctamente."})
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()

@app.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    data = request.get_json()
    nombre = data['nombre']
    correo = data['correo']
    telefono = data['telefono']
    direccion = data['direccion']

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE clientes SET nombre=%s, correo=%s, telefono=%s, direccion=%s WHERE id=%s", (nombre, correo, telefono, direccion, id))
        connection.commit()
        return jsonify({"message": "Cliente actualizado correctamente."})
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()

@app.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
        connection.commit()
        return jsonify({"message": "Cliente eliminado correctamente."})
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()
    
@app.route('/vehiculos', methods=['POST'])
def crear_vehiculo():
    data = request.get_json()
    cliente_id = data['cliente_id']
    marca = data['marca']
    modelo = data['modelo']
    anio = data['anio']
    placa = data['placa']
    color = data['color']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO vehiculos (cliente_id, marca, modelo, anio, placa, color) VALUES (%s, %s, %s, %s, %s, %s)", (cliente_id, marca, modelo, anio, placa, color))
        connection.commit()
        return jsonify({"message": "Vehículo creado correctamente."})
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()

@app.route('/vehiculos', methods=['GET'])
def obtener_vehiculos():
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM vehiculos")
        vehiculos = cursor.fetchall()
        return jsonify(vehiculos)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()

@app.route('/vehiculos/<int:id>', methods=['PUT'])
def actualizar_vehiculo(id):
    data = request.get_json()
    cliente_id = data['cliente_id']
    marca = data['marca']
    modelo = data['modelo']
    anio = data['anio']
    placa = data['placa']
    color = data['color']

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE vehiculos SET cliente_id=%s, marca=%s, modelo=%s, anio=%s, placa=%s, color=%s WHERE id=%s", (cliente_id, marca, modelo, anio, placa, color, id))
        connection.commit()
        return jsonify({"message": "Vehículo actualizado correctamente."})
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()
@app.route('/vehiculos/<int:id>', methods=['DELETE'])
def eliminar_vehiculo(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM vehiculos WHERE id=%s", (id,))
        connection.commit()
        return jsonify({"message": "Vehículo eliminado correctamente."})
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

# Configuración de la conexión a la base de datos MySQL
db_host = 'localhost'
db_user = 'root'
db_password = 'root'
db_name = 'tallerxyzdb'

def get_db_connection():
    return pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        return jsonify(clientes)
    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()

@app.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.get_json()
    nombre = data['nombre']
    correo = data['correo']
    telefono = data['telefono']
    direccion = data['direccion']
    
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO clientes (nombre, correo, telefono, direccion) VALUES (%s, %s, %s, %s)", (nombre, correo, telefono, direccion))
        connection.commit()
        return jsonify({"message": "Cliente creado correctamente."})
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()

@app.route('/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    data = request.get_json()
    nombre = data['nombre']
    correo = data['correo']
    telefono = data['telefono']
    direccion = data['direccion']

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE clientes SET nombre=%s, correo=%s, telefono=%s, direccion=%s WHERE id=%s", (nombre, correo, telefono, direccion, id))
        connection.commit()
        return jsonify({"message": "Cliente actualizado correctamente."})
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()

@app.route('/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
        connection.commit()
        return jsonify({"message": "Cliente eliminado correctamente."})
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)})
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 6d22dd8eb15667f7ef0cea6cd2495568ad2af54a
