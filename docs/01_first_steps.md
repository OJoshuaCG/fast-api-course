Creamos un entorno virtual y lo activamos

```bash
python -m venv .venv

.venv\Scripts\activate
```

Instalamos FastAPI

```bash
pip install "fastapi[standard]"
```

Creamos nuestro script

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
```

Para poder visualizarlo en la web, ejecutamos el siguiente comando en la terminal

```bash
fastapi dev main.py
```

Existen distintas formas de poder visualizar la documentacion de nuestra API

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) - Swagger
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) - ReDoc
- [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json) - OpenAPI