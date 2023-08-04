# TXYZ
A sample webapp for Taller xyz 
## Backend
- En esta solución tenemos una API rest en python (Flask) que se ejecutará por defecto en el puerto 5000 tras colocar python app.py
- la conexión de la base de datos está en mysql y por esto se importa la librería `pymysql` en caso de querer usar Microsoft SQL server tendrá que reemplazar la librería por `pyodbc`
- En caso de que brinde algún error en las consultas solo se debe de reemplazar los comodines `%s` por el estándar de SQL server `?` y recortar los argumentos en el `cursor.execute`
- Estructura base de datos tallerxyzdb:
- Tabla: clientes
id (clave primaria)
nombre
correo
telefono
dirección
...
-Tabla: vehiculos
id (clave primaria)
cliente_id (clave foránea hacia la tabla clientes)
marca
modelo
año
placa
color
chasis (No implementado en este caso)

## Frontend 

El frontend está en react sin ningún detalle estético para consumior la api se hace uso de `axios` 

Para correr el frontend bastará con intalar lo requerido con hacer un `npm install` y `npm start` 



