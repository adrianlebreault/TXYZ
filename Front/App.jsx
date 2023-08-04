import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [clientes, setClientes] = useState([]);
  const [nombre, setNombre] = useState('');
  const [correo, setCorreo] = useState('');
  const [telefono, setTelefono] = useState('');
  const [direccion, setDireccion] = useState('');

  const obtenerClientes = async () => {
    try {
      const response = await axios.get('http://localhost:5000/clientes');
      setClientes(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    obtenerClientes();
  }, []);

  const crearCliente = async () => {
    try {
      const response = await axios.post('http://localhost:5000/clientes', {
        nombre,
        correo,
        telefono,
        direccion,
      });
      console.log(response.data.message);
      obtenerClientes();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Clientes</h2>
      <div>
        <h3>Crear Cliente</h3>
        <input type="text" value={nombre} onChange={(e) => setNombre(e.target.value)} placeholder="Nombre" />
        <input type="email" value={correo} onChange={(e) => setCorreo(e.target.value)} placeholder="Correo" />
        <input type="tel" value={telefono} onChange={(e) => setTelefono(e.target.value)} placeholder="Teléfono" />
        <input type="text" value={direccion} onChange={(e) => setDireccion(e.target.value)} placeholder="Dirección" />
        <button onClick={crearCliente}>Guardar</button>
      </div>
      <div>
        <h3>Listado de Clientes</h3>
        {clientes.map((cliente) => (
          <div key={cliente.id}>
            <p>Nombre: {cliente.nombre}</p>
            <p>Correo: {cliente.correo}</p>
            <p>Teléfono: {cliente.telefono}</p>
            <p>Dirección: {cliente.direccion}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;