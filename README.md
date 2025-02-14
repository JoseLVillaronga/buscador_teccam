# Buscador TecCam API

API local para realizar búsquedas en Internet utilizando DuckDuckGo. Proporciona endpoints para búsqueda general, noticias, imágenes y videos.

## Requisitos Previos

- Python 3.x
- Acceso a sudo sin contraseña para la instalación del servicio

## Instalación

1. Clonar o descargar este repositorio y navegar al directorio del proyecto:
```bash
cd buscador-teccam
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

4. Instalar como servicio (opcional):
```bash
chmod +x install_service.sh
./install_service.sh
```

## Uso

### Como Servicio

Si has instalado la API como servicio, estará disponible automáticamente en `http://localhost:5008`. El servicio se inicia automáticamente con el sistema.

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

1. **Búsqueda General**
```
GET http://localhost:5008/api/buscar?q=texto&max_results=5
```

2. **Búsqueda de Noticias**
```
GET http://localhost:5008/api/buscar/noticias?q=texto&max_results=5
```

3. **Búsqueda de Imágenes**
```
GET http://localhost:5008/api/buscar/imagenes?q=texto&max_results=5
```

4. **Búsqueda de Videos**
```
GET http://localhost:5008/api/buscar/videos?q=texto&max_results=5
```

### Parámetros

- `q`: (requerido) Texto a buscar
- `max_results`: (opcional, default=5) Número máximo de resultados

### Ejemplos de Uso

Usando curl:
```bash
# Búsqueda general
curl "http://localhost:5008/api/buscar?q=python&max_results=5"

# Búsqueda de noticias
curl "http://localhost:5008/api/buscar/noticias?q=tecnologia&max_results=5"

# Búsqueda de imágenes
curl "http://localhost:5008/api/buscar/imagenes?q=paisajes&max_results=5"

# Búsqueda de videos
curl "http://localhost:5008/api/buscar/videos?q=tutoriales&max_results=5"
```

## Estructura de Respuestas

Cada tipo de búsqueda devuelve un JSON con estructura específica:

### Búsqueda General
```json
{
  "consulta": "texto_buscado",
  "resultados": {
    "resultado_1": {
      "titulo": "...",
      "enlace": "...",
      "descripcion": "..."
    }
  }
}
```

### Búsqueda de Noticias
```json
{
  "consulta": "texto_buscado",
  "resultados": {
    "resultado_1": {
      "titulo": "...",
      "enlace": "...",
      "descripcion": "...",
      "fecha": "...",
      "fuente": "...",
      "imagen": "..."
    }
  }
}
```

### Búsqueda de Imágenes
```json
{
  "consulta": "texto_buscado",
  "resultados": {
    "resultado_1": {
      "titulo": "...",
      "enlace": "...",
      "imagen_url": "...",
      "thumbnail": "...",
      "fuente": "...",
      "altura": "...",
      "anchura": "..."
    }
  }
}
```

### Búsqueda de Videos
```json
{
  "consulta": "texto_buscado",
  "resultados": {
    "resultado_1": {
      "titulo": "...",
      "enlace": "...",
      "descripcion": "...",
      "duracion": "...",
      "autor": "...",
      "thumbnail": "...",
      "vistas": "..."
    }
  }
}
```

## Uso como Librería

También puedes usar las funciones de búsqueda directamente en tu código Python:

```python
import buscador_internet as bi

# Búsqueda general
resultados = bi.buscar("python programming")

# Búsqueda de noticias
noticias = bi.buscar_noticias("tecnología")

# Búsqueda de imágenes
imagenes = bi.buscar_imagenes("paisajes")

# Búsqueda de videos
videos = bi.buscar_videos("tutoriales python")
```
