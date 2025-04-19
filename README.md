# Buscador TecCam API

API local para realizar búsquedas en Internet utilizando DuckDuckGo. Proporciona endpoints para búsqueda general, noticias, imágenes y videos. Soporta configuración de proxy para entornos corporativos.

## Características

- Búsqueda general de texto
- Búsqueda específica de noticias, imágenes y videos
- Soporte para proxy HTTP/HTTPS
- Configurable mediante variables de entorno
- Instalable como servicio del sistema
- API RESTful

## Requisitos Previos

- Python 3.x
- Acceso a sudo sin contraseña para la instalación del servicio
- Conexión a Internet (directa o mediante proxy)

## Instalación

1. Clonar o descargar este repositorio y navegar al directorio del proyecto:
```bash
cd buscador_teccam
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
source ./venv/bin/activate
```

3. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar el entorno:
```bash
# Copiar el archivo de configuración de ejemplo
cp .env.example .env

# Editar el archivo .env con tu configuración
nano .env
```

5. Instalar como servicio (opcional):
```bash
chmod +x install_service.sh
./install_service.sh
```

## Configuración

### Variables de Entorno

El sistema utiliza un archivo `.env` para la configuración. Las variables disponibles son:

#### Configuración del Proxy
```env
PROXY_HOST=proxy.example.com    # Host del proxy
PROXY_PORT=8080                 # Puerto del proxy
PROXY_USER=                     # Usuario del proxy (opcional)
PROXY_PASS=                     # Contraseña del proxy (opcional)
```

#### Configuración de la API
```env
API_HOST=localhost              # Host donde se ejecutará la API
API_PORT=5008                   # Puerto para la API
API_DEBUG=False                # Modo debug (True/False)
```

### Ejemplos de Configuración

1. **Sin Proxy**:
```env
PROXY_HOST=
PROXY_PORT=
API_HOST=localhost
API_PORT=5008
```

2. **Con Proxy Simple**:
```env
PROXY_HOST=proxy.empresa.com
PROXY_PORT=8080
API_HOST=localhost
API_PORT=5008
```

3. **Con Proxy Autenticado**:
```env
PROXY_HOST=proxy.empresa.com
PROXY_PORT=8080
PROXY_USER=usuario
PROXY_PASS=contraseña
API_HOST=localhost
API_PORT=5008
```

## Uso

### Como Servicio

Si has instalado la API como servicio, estará disponible automáticamente en `http://localhost:5008` (o en el puerto configurado en `.env`). El servicio se inicia automáticamente con el sistema.

Comandos útiles para gestionar el servicio:
```bash
# Ver estado del servicio
sudo systemctl status buscador-teccam.service

# Iniciar el servicio
sudo systemctl start buscador-teccam.service

# Detener el servicio
sudo systemctl stop buscador-teccam.service

# Reiniciar el servicio
sudo systemctl restart buscador-teccam.service

# Ver logs
sudo journalctl -u buscador-teccam.service
```

### Como Script

También puedes ejecutar la API manualmente:
```bash
python api.py
```

### Endpoints Disponibles

La API expone los siguientes endpoints para búsquedas en Internet. Puedes probarlos directamente desde tu navegador o con herramientas como `curl`.

| Tipo      | Endpoint                                 | Descripción                | Ejemplo de uso                                                                 |
|-----------|------------------------------------------|----------------------------|--------------------------------------------------------------------------------|
| General   | `/api/buscar?q=python`                   | Búsqueda general de texto  | [Abrir](http://localhost:5008/api/buscar?q=python)                             |
| Noticias  | `/api/buscar/noticias?q=ciencia`         | Búsqueda de noticias       | [Abrir](http://localhost:5008/api/buscar/noticias?q=ciencia)                   |
| Imágenes  | `/api/buscar/imagenes?q=gatos`           | Búsqueda de imágenes       | [Abrir](http://localhost:5008/api/buscar/imagenes?q=gatos)                     |
| Videos    | `/api/buscar/videos?q=robotica`          | Búsqueda de videos         | [Abrir](http://localhost:5008/api/buscar/videos?q=robotica)                    |

#### Parámetros

- `q` (**requerido**): Texto a buscar
- `max_results` (**opcional**, default=5): Número máximo de resultados

#### Ejemplos de Uso con curl

```bash
# Buscar noticias sobre inteligencia artificial
curl "http://localhost:5008/api/buscar/noticias?q=inteligencia+artificial&max_results=3"

# Buscar imágenes de gatos
curl "http://localhost:5008/api/buscar/imagenes?q=gatos"

# Buscar en navegador
# http://localhost:5008/api/buscar?q=python
```

## Solución de Problemas

### Problemas con el Proxy

1. **Error de conexión al proxy**:
   - Verificar que PROXY_HOST y PROXY_PORT sean correctos
   - Comprobar conectividad al proxy: `curl -v -x proxy.empresa.com:8080 http://example.com`

2. **Error de autenticación**:
   - Verificar que PROXY_USER y PROXY_PASS sean correctos
   - Asegurarse de que las credenciales tengan los permisos necesarios

3. **Timeout en las búsquedas**:
   - Verificar la conectividad general del proxy
   - Comprobar si hay restricciones de acceso a DuckDuckGo

### Problemas del Servicio

1. **El servicio no inicia**:
   - Verificar los logs: `sudo journalctl -u buscador-teccam.service`
   - Comprobar la configuración en `.env`
   - Verificar permisos del directorio y archivos

2. **Error al cargar la configuración**:
   - Verificar que existe el archivo `.env`
   - Comprobar permisos de lectura del archivo `.env`
   - Validar el formato de las variables en `.env`
