<img src="assets/header.png" alt="Header" width="100%">

<h1><b>💻 Módulo Programador - Evidencia 4</b></h1>

<h2>🚧 Objetivo </h2>

Diseñar y desarrollar una clase en Python que represente un objeto con funcionalidad lógica, aplicando TDD, conceptos de POO y diseñando la base de datos correspondiente.

<h2>🚧 Instrucciones </h2>

1. __Selección y Diseño del Objeto:__
    - Elige un objeto de los dos propuestos para cada alumno
    - Define 3 comportamientos clave del objeto que involucren lógica de
programación (no solo getters/setters).
    - Incluye al menos un método estándar de definición def__. Ej. __ str__(self), __ len__(self),__ add__ (self, other), etc.

2. __Desarrollo guiado por pruebas (TDD):__
    - Escribe primero las pruebas unitarias.
    - Implementa la clase para que pase las pruebas.
    - Refactoriza en caso de ser necesario.

3. __Base de Datos:__
    - Diseña una base de datos que represente tu objeto.
    - Escribe la sentencia CREATE TABLE, definiendo PK, FK, etc, según
corresponda.
    - Crea 10 sentencias INSERT con datos de ejemplo.
    - Escribe 5 consultas de tipo SELECT.

4. __Documentación y Reflexión en Video:__
    - Graba un video de máximo 60 segundos donde:
        - Explique brevemente el código fuente demostrando cómo se aplican
los principios de abstracción y encapsulamiento en el código fuente.
        - Explique brevemente la experiencia con TDD.
        - Se debe observar en el video el programa en funcionamiento.
    - Tips para el video:
        - Sé conciso y ve al grano.
        - Muestra brevemente partes relevantes de tu código mientras explicas.
        - Asegúrate de que tu audio sea claro y comprensible.

5. __Entregables:__
    - Repositorio público en github que incluya:
        - Código Python (incluyendo pruebas).
        - Archivo SQL.
    - Video de 60 segundos a YouTube como "no listado" o Google Drive.
    - En la plataforma de la institución, entrega:
        - El enlace a tu repositorio de GitHub.
        - El enlace a tu video de YouTube (no listado) o Drive.

<h2>🚧 Restricciones y Consideraciones </h2>

- El video debe ser una grabación original del estudiante explicando su propio trabajo.
- La modalidad de entrega es individual.
- No sé admitirán modificaciones a los entregables fuera de la fecha de entrega.

<h2>🚧 Descripción del código </h2>

La clase `Montacarga.py` representa el objeto seleccionado. La misma en su interior tiene los comportamientos basicos de un montacarga.

- __pasillo:__ Indica la cantidad de pasillos que posee el edificio donde trabaja.
- __pasillo_actual:__ Indica el pasillo en el que se encuentra el montacarga.
- __carga_actual:__ Indica la carga que posee actualmente el montacarga.
- __carga_maxima:__ Indica la capacidad maxima del montacarga.
- __encendido:__ Indica si el montacarga se encuentra encendido o no.

<h2>🚧 Principios aplicados en el diseño </h2>

- __Abstracción:__ La clase `Montacarga` abstrae los detalles internos de su funcionamiento, proporcionando métodos claros para que el usuario pueda interactuar.
- __Encapsulamiento:__ Los datos y métodos relevantes están encapsulados dentro de la clase, y los atributos se protegen adecuadamente mediante validaciones.

<h2>🚧 Desarrollo guiado por pruebas (TDD) </h2>

- Para el desarrollo guiado por pruebas (TDD) se optó por la utilización de la biblioteca pytest.

- Las pruebas unitarias estan escritas en el archivo `test_montacarga.py`

- El archivo `montacarga.py` contiene el código fuente de la clase `Montacarga`. El mismo tambien contiene un fragmento del código para la prueba del objeto.

<br>

__Comando de Ejecución del Código Principal__
   ```bash
   python fundidora.py
   ```

__Comando de Ejecución de las Pruebas Unitarias__
   ```bash
   pytest test_montacarga.py
   ```

<h2>🚧 Base de Datos </h2>

- El archivo `bd_montacarga.sql` contiene la sentencia CREATE DATABASE, CREATE TABLE, definiendo PK y sus atributos. El mismo es el archivo de la base de datos correspondiente.

- El archivo contiene ademas 10 sentencias INSERT con datos de ejemplo.

- El archivo contiene ademas 5 consultas de tipo SELECT.

<h2>🚧 Vídeo explicativo de la evidencia </h2>

Para una demostración del funcionamiento del programa y una breve explicación sobre la aplicación de los principios de POO y TDD, adjunto link al siguiente video en YouTube:

[Video explicativo de la evidencia](https://youtu.be/-Hg_Ove1tyc)


