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

## Funcionamiento del Sistema

- Los módulos de Python se instalan usando el archivo requirements.txt generado con "pip freeze". Si presenta fallos iniciales, revisa que la versión de los módulos sea compatible.
- Pasos a seguir:
  1. Enciende la RPi y espera unos minutos a que levante el sistema operativo y genere el wifi.
  2. Conecta el ordenador al wifi de la RPi. En Windows, desactiva la reconexión automática a otras redes que tengan internet.
  3. Conecta la batería a los acelerómetros. Si usas las powerbank (rosas), asegúrate de que se enciendan (verifica las luces o actívalas manualmente).
  4. Abre el programa, carga el archivo acclist.txt y da play. Aunque el status en la interfaz no cambie visiblemente, comprueba en la carpeta data si los archivos se modifican.
  5. Asegúrate de que todos los powerbank estén encendidos antes de ejecutar el programa.
  6. Al finalizar, detén la recolección y verifica que todos los threads se hayan finalizado (puede ser necesario cerrar manualmente algunos procesos).

## Estructura del Proyecto

- `iniciarAcel_UDP_gui_OPENARMS.py`: Define la interfaz gráfica de usuario (GUI) utilizando PyQt5.
- `AcelGui_UDP_ndatos_OPENARMS.pyw`: Contiene la lógica principal de la aplicación, incluyendo la comunicación UDP y el manejo de hilos.
- `sql_server.py`: Módulo para la conexión y manejo de la base de datos MySQL. Deprecated.
- `data/`: Carpeta donde se guardan los archivos de datos generados por la aplicación.

