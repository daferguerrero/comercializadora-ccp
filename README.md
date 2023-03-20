# Arquitecturas-g3-qrm


**Instrucciones para la ejecución de los diferentes servicios**

***
**1. Experimento Disponibilidad**
****

- **Microservicio Recibir Orden Venta**

1. Ubicarse en el directorio **Arquitecturas-g3-qrm\MicroServicios\MSRecibirOrdenVenta**
2. Crear directorio virtual **python3 -m venv venv**
3. Activar Ambiente Virtual(Windows) **.\venv\Scripts\activate**
4. Ejecutar el comando **pip3 install -r requirements.txt**
5. Ejecutar **cd flaskr**
6. Ejecutar **flask run -p 5001**
7. Endpoint API http://127.0.0.1:5001/orden/recibir
8. Request: {
     "tipoid":"CC",
     "identificacion":"123456",
     "nombre":"Cliente 1",
     "direccion":"Clle 89",
     "telefono":"3102589635"
    }
 9. Response: {
        "cod_error": "0",
        "descripcion": "OK",
        "numero_orden": 1
    }

- **Microservicio Generar Orden Venta**

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

- **API Gateway**

1. Ubicarse en el directorio **Arquitecturas-g3-qrm\ApiGateway**
2. Crear directorio virtual **python3 -m venv venv**
3 Activar Ambiente Virtual(Windows) **.\venv\Scripts\activate**
4. Ejecutar el comando **pip3 install -r requirements.txt**
5. Ejecutar **cd flaskr**
6. Ejecutar **flask run -p 5002**
7. Endpoint API http://127.0.0.1:5002/orden/generar
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


***
**2. Experimento Seguridad**
****

- **Componente Autorizador**


1. Ubicarse en el directorio **Arquitecturas-g3-qrm\Autorizador**
2. Crear directorio virtual **python3 -m venv venv**
3. Activar Ambiente Virtual(Windows) **.\venv\Scripts\activate**
4. Ejecutar el comando **pip3 install -r requirements.txt**
5. Ejecutar **flask run -p 5001**
6. Endpoint POST API Generar Token http://127.0.0.1:5001/token/generar
7. Request: {}
8. En el encabezado colocar las siguientes llaves **apiKey** :IPE56EOqtwRFeo7TCh6AQyimpqcPY0DIRxZFoni4OIPQ5DklmpCh4R3ocf1GP4hz **user** : cpp_reparto
9. Response: {"msg": "Generación de token exitosa","token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3ODc3MTM0MiwianRpIjoiZDQ2YjM3NTQtMzlkYi00NWJjLTliM2YtMGI4ZWI3ODlhNDU0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNwcF9yZXBhcnRvIiwibmJmIjoxNjc4NzcxMzQyLCJleHAiOjE2Nzg3NzE0MDJ9.kF59lsYsfaQVOFGeLGC8hrRQwrGCEwb2Dos6pJ3USbA" }
10. Endpoint POST API Validar Token http://127.0.0.1:5001/token/validar
11. Request: {}
12. En el encabezado enviar el token así: **Authorization** : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3ODc3MTM0MiwianRpIjoiZDQ2YjM3NTQtMzlkYi00NWJjLTliM2YtMGI4ZWI3ODlhNDU0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImNwcF9yZXBhcnRvIiwibmJmIjoxNjc4NzcxMzQyLCJleHAiOjE2Nzg3NzE0MDJ9.kF59lsYsfaQVOFGeLGC8hrRQwrGCEwb2Dos6pJ3USbA
13. Response: {"msg": "OK"}

- **Archivo Jmeter**
 
**Prueba al Microservicio Modificar Orden Reparto**
 
1. Extraer el archivo **ModificarOrden.jmx** del siguiente .zip [ModificarOrden.zip](https://github.com/neztoring/Arquitecturas-g3-qrm/files/11013194/ModificarOrden.zip)
y colocarlo en la ruta **apache-jmeter-5.5\bin**   
2. Ejecutar Jmeter
3. Abrir archivo **ModificarOrden.jmx**
