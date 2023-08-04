import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [clientes, setClientes] = useState([]);
  const [vehiculos, setVehiculos] = useState([]);
  const [nombreCliente, setNombreCliente] = useState('');
  const [correoCliente, setCorreoCliente] = useState('');
  const [telefonoCliente, setTelefonoCliente] = useState('');
  const [direccionCliente, setDireccionCliente] = useState('');

  const [marcaVehiculo, setMarcaVehiculo] = useState('');
  const [modeloVehiculo, setModeloVehiculo] = useState('');
  const [anioVehiculo, setAnioVehiculo] = useState('');
  const [placaVehiculo, setPlacaVehiculo] = useState('');
  const [colorVehiculo, setColorVehiculo] = useState('');

  const obtenerClientes = async () => {
    try {
      const response = await axios.get('http://localhost:5000/clientes');
      setClientes(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const obtenerVehiculos = async () => {
    try {
      const response = await axios.get('http://localhost:5000/vehiculos');
      setVehiculos(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    obtenerClientes();
    obtenerVehiculos();
  }, []);

  const crearCliente = async () => {
    try {
      const response = await axios.post('http://localhost:5000/clientes', {
        nombre: nombreCliente,
        correo: correoCliente,
        telefono: telefonoCliente,
        direccion: direccionCliente,
      });
      console.log(response.data.message);
      obtenerClientes();
    } catch (error) {
      console.error(error);
    }
  };

  const crearVehiculo = async () => {
    try {
      const response = await axios.post('http://localhost:5000/vehiculos', {
        cliente_id: parseInt(document.getElementById('cliente_id').value),
        marca: marcaVehiculo,
        modelo: modeloVehiculo,
        anio: anioVehiculo,
        placa: placaVehiculo,
        color: colorVehiculo,
      });
      console.log(response.data.message);
      obtenerVehiculos();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Clientes</h2>
      <div>
        <h3>Crear Cliente</h3>
        <input type="text" value={nombreCliente} onChange={(e) => setNombreCliente(e.target.value)} placeholder="Nombre" />
        <input type="email" value={correoCliente} onChange={(e) => setCorreoCliente(e.target.value)} placeholder="Correo" />
        <input type="tel" value={telefonoCliente} onChange={(e) => setTelefonoCliente(e.target.value)} placeholder="Teléfono" />
        <input type="text" value={direccionCliente} onChange={(e) => setDireccionCliente(e.target.value)} placeholder="Dirección" />
        <button onClick={crearCliente}>Guardar Cliente</button>
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
      <h2>Vehículos</h2>
      <div>
        <h3>Crear Vehículo</h3>
        <select id="cliente_id">
          {clientes.map((cliente) => (
            <option key={cliente.id} value={cliente.id}>
              {cliente.nombre}
            </option>
          ))}
        </select>
        <input type="text" value={marcaVehiculo} onChange={(e) => setMarcaVehiculo(e.target.value)} placeholder="Marca" />
        <input type="text" value={modeloVehiculo} onChange={(e) => setModeloVehiculo(e.target.value)} placeholder="Modelo" />
        <input type="text" value={anioVehiculo} onChange={(e) => setAnioVehiculo(e.target.value)} placeholder="Año" />
        <input type="text" value={placaVehiculo} onChange={(e) => setPlacaVehiculo(e.target.value)} placeholder="Placa" />
        <input type="text" value={colorVehiculo} onChange={(e) => setColorVehiculo(e.target.value)} placeholder="Color" />
        <button onClick={crearVehiculo}>Guardar Vehículo</button>
      </div>
      <div>
        <h3>Listado de Vehículos</h3>
        {vehiculos.map((vehiculo) => (
          <div key={vehiculo.id}>
            <p>Cliente: {vehiculo.cliente_id}</p>
            <p>Marca: {vehiculo.marca}</p>
            <p>Modelo: {vehiculo.modelo}</p>
            <p>Año: {vehiculo.anio}</p>
            <p>Placa: {vehiculo.placa}</p>
            <p>Color: {vehiculo.color}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;