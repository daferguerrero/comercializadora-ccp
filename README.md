# Arquitecturas-g3-qrm


**Instrucciones para la ejecución de los diferentes servicios**


- Microservicio **Recibir Orden Venta**

1. Ubicarse en el directorio **Arquitecturas-g3-qrm\MicroServicios\MSRecibirOrdenVenta**
2. Crear directorio virtual **python3 -m venv venv**
3. Activar Ambiente Virtual(Windows) **.\venv\Scripts\activate**
4. Ejecutar el comando **pip3 install -r requirements.txt**
5. Ejecutar **cd flaskr**
6. Ejecutar **flask run -p 5001**
7. Endpoint API http://127.0.0.1:5001/orden/recibir
8. Request: 
      {
     "tipoid":"CC",
     "identificacion":"123456",
     "nombre":"Cliente 1",
     "direccion":"Clle 89",
     "telefono":"3102589635"
    }
 9. Response: 
    {
        "cod_error": "0",
        "descripcion": "OK",
        "numero_orden": 1
    }

- Microservicio **Generar Orden Venta**

1. Ubicarse en el directorio **Arquitecturas-g3-qrm\MicroServicios\MSGenerarOrdenVenta**
2. Crear directorio virtual **python3 -m venv venv**
3 Activar Ambiente Virtual(Windows) **.\venv\Scripts\activate**
4. Ejecutar el comando **pip3 install -r requirements.txt**
5. Ejecutar **cd flaskr**
6. Ejecutar **flask run -p 5000**
7. Endpoint API http://127.0.0.1:5000/orden/generar
8. Request: 
     {
 "tipoid":"CC",
     "identificacion":"123456",
     "nombre":"Cliente 1",
     "direccion":"Clle 89",
     "telefono":"3102589635",
     "estado_recibir":"false"

    }
 9. Response: 
    {
        "cod_error": "0",
        "descripcion": "OK",
        "numero_orden": 1
    }
    
    
 - **Archivo Jmeter**
 
 **Prueba al Microservicio Generar Orden Venta**
 
 1. Extraer el archivo **GenerarOrden.jmx** del siguiente .zip [GenerarOrden.zip](https://github.com/neztoring/Arquitecturas-g3-qrm/files/10829024/GenerarOrden.zip) y colocarlo en la ruta **apache-jmeter-5.5\bin**
   
 2. Ejecutar Jmeter
 3. Abrir archivo **GenerarOrden.jmx**
 
 ![image](https://user-images.githubusercontent.com/20029761/221299313-7cbc92f5-bcf6-4c1c-b70b-20ecb3057cdb.png)
![image](https://user-images.githubusercontent.com/20029761/221299460-0e081803-94d3-4f12-9c69-c6419be2c574.png)
![image](https://user-images.githubusercontent.com/20029761/221299533-28c804c6-4a04-4ed3-b3df-fd23d7d39f2b.png)
 
 4. Ejecutar Prueba
 
 ![image](https://user-images.githubusercontent.com/20029761/221299584-0689bf16-f98e-4372-bf14-afde3945857e.png)


 
    
