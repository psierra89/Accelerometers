# Acc Controller

Este proyecto es una aplicación de control de acelerómetros utilizando PyQt5 y UDP para la comunicación. La aplicación permite iniciar y detener la recolección de datos de acelerómetros, guardar los datos en archivos y bases de datos, y visualizar el estado de los acelerómetros.

## Requisitos

- Python 3.x
- PyQt5
- MySQLdb (opcional, para guardar datos en una base de datos MySQL)
- Matplotlib (opcional, para visualización de datos en tiempo real)

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:
    ```sh
    python AcelGui_UDP_ndatos_OPENARMS.pyw
    ```

2. Usa la interfaz gráfica para:
    - Abrir un archivo de lista de acelerómetros (acclist.txt IP:PORT:NAME).
    - Iniciar y detener la recolección de datos.
    - Guardar los datos en archivos.

## Estructura del Proyecto

- `iniciarAcel_UDP_gui_OPENARMS.py`: Define la interfaz gráfica de usuario (GUI) utilizando PyQt5.
- `AcelGui_UDP_ndatos_OPENARMS.pyw`: Contiene la lógica principal de la aplicación, incluyendo la comunicación UDP y el manejo de hilos.
- `sql_server.py`: Módulo para la conexión y manejo de la base de datos MySQL. Deprecated.
- `data/`: Carpeta donde se guardan los archivos de datos generados por la aplicación.

