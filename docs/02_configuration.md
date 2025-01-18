Podemos configurar la informacion de nuestra documentacion, como el titulo, la version y tags.

```python
from fastapi import FastAPI
app = FastAPI()
app.title = 'API de cocina"
app.version = "2.8.1"

@app.get('/', tags=['Cocineta'])
def home():
    return 'Hello world!"
```

Dentro de la terminal, contamos con el comando `uvicorn`, el cual es el servidor que se tiene ejecutando por defecto al utilizar FastAPI, en el, podemos configurar:

- `--port`: Puerto de escucha
- `--host`: IP de enlace al servidor, por defecto es `0.0.0.0`, por lo que cualquiera puede acceder
- `--workers`: Numero de procesos disponibles para manejar las solicitudes
- `--log-level`: Nivel de detalles de logs, algunos parametros son: `debug`, `info`, `warning`, `error`, `critical`.

Al momento de desarrollar, contamos con algunas banderas utiles:

- `--reload`: Recarga automaticamente el servidor al haber cambios en los archivos.
- `--reload-dirs`: Especifica directorios adicionales a monitorear para recargas.
- `--debug`: Activa el modo de depuración, proporcionando información más detallada en los logs.

Banderas para producción:

- `--factory`: Especifica una función que crea la aplicación FastAPI. Útil para configuraciones más complejas.
- `--forked`: Inicia cada trabajador en un proceso separado.
- `--uds`: Especifica un socket UNIX para la comunicación.

Otras banderas útiles:

- `--timeout-keep-alive`: Establece el tiempo máximo de inactividad para las conexiones keep-alive.
- `--limit-concurrency`: Limita el número máximo de solicitudes concurrentes.
- `--proxy-headers`: Habilita el soporte para encabezados proxy.

Ejemplo de comando:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 --log-level info --reload --reload-dirs templates static
```

Este comando iniciará tu aplicación en el puerto 8000, utilizando 4 procesos trabajadores, con logs a nivel de información, y recargará automáticamente la aplicación cuando se modifiquen los archivos en los directorios `templates` y `static`.