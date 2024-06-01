Proyecto Grocery Store

Liga a video: https://drive.google.com/file/d/1KJV1QltBjGppY71yD3iH8k1uhlORJlgZ/view?usp=share_link

Este proyecto es una aplicación web construida con Python y Flask que permite gestionar un inventario de artículos.
## Funcionalidades

- Cargar datos desde un archivo CSV a una base de datos PostgreSQL.
- API REST para operaciones CRUD (Crear, Leer, Actualizar, Eliminar) de artículos.
- Conversión de precios de artículos a diferentes monedas utilizando una API externa.
    https://exchangeratesapi.io/documentation/
- Vista HTML para agregar, editar y eliminar artículos.

# Prácticas SOLID

-Responsabilidad Única: Cada clase y módulo tiene una responsabilidad específica.
-Abierto/Cerrado: La clase 'CurrencyConverter' está abierta para extensión y cerrada para modificación.
-Sustitución de Liskov: La clase 'GroceryRepository' podría ser sustituida por una implementación alternativa.
-Segregación de Interfaces: Las clases tienen interfaces específicas y coherentes.
-Inversión de Dependencias: Las clases de alto nivel no dependen de clases de bajo nivel.

# Patrones de Diseño

-Repositorio: La clase 'GroceryRepository' actúa como un repositorio de datos.
-Estrategia: La clase 'CurrencyConverter' utiliza el patrón estrategia para permitir diferentes implementaciones de conversión de moneda.
-Fachada: La clase 'GroceryRepository' actúa como una fachada para las operaciones de la base de datos.
-Modelos de vista: El proyecto sigue una arquitectura similar al patrón MVC.

# Características de Arquitectura

1. El proyecto está dividido en componentes separados con responsabilidades específicas.
2. Los componentes están desacoplados gracias a la inyección de dependencias y el uso de interfaces y abstracciones.
3. El código está organizado en módulos separados que pueden ser reutilizados y mantenidos de manera independiente.
4. La arquitectura actual permite agregar nuevas funcionalidades y cambiar implementaciones sin afectar el código existente.
5. El proyecto cuenta con pruebas unitarias que facilitan la validación y el mantenimiento del código.

Si la aplicación migrara a una arquitectura de microservicios, las principales características serían:

1. Cada uno de los microservicios sería un componente independiente y desacoplado.
2. Podría escalarse de manera independiente según las necesidades.
3. Si un microservicio fallara, los demás seguirían funcionando.
4. Se podría trabajar en diferentes microservicios de forma paralela.
5. Cada microservicio podría probarse de forma aislada.

# Comando para configuración de BD Postgres
psql postgres
postgres=# CREATE DATABASE grocery_db;
CREATE DATABASE
postgres=# CREATE USER sebas WITH ENCRYPTED PASSWORD 'newpass';
postgres=# GRANT ALL PRIVILEGES ON DATABASE grocery_db TO sebas;
GRANT
postgres=# \q

#Probar proyecto
1. Correr el programa 'cr eate_db.py' para creat las tablas necesarias ddentro de la DB, limpiar las tablas actuales y cargar los datos.
2. Ejecutar el programa 'main.py' y abrir localhost:5000 para probar la funcionalidad del proyecto.