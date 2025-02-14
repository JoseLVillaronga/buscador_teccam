from flask import Flask, request, jsonify
import buscador_internet as bi
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

@app.route('/api/buscar', methods=['GET'])
def buscar():
    """Endpoint para búsqueda general"""
    query = request.args.get('q', '')
    max_results = request.args.get('max_results', 5, type=int)
    if not query:
        return jsonify({"error": "El parámetro de búsqueda 'q' es requerido"}), 400
    return jsonify(bi.buscar(query, max_results))

@app.route('/api/buscar/noticias', methods=['GET'])
def buscar_noticias():
    """Endpoint para búsqueda de noticias"""
    query = request.args.get('q', '')
    max_results = request.args.get('max_results', 5, type=int)
    if not query:
        return jsonify({"error": "El parámetro de búsqueda 'q' es requerido"}), 400
    return jsonify(bi.buscar_noticias(query, max_results))

@app.route('/api/buscar/imagenes', methods=['GET'])
def buscar_imagenes():
    """Endpoint para búsqueda de imágenes"""
    query = request.args.get('q', '')
    max_results = request.args.get('max_results', 5, type=int)
    if not query:
        return jsonify({"error": "El parámetro de búsqueda 'q' es requerido"}), 400
    return jsonify(bi.buscar_imagenes(query, max_results))

@app.route('/api/buscar/videos', methods=['GET'])
def buscar_videos():
    """Endpoint para búsqueda de videos"""
    query = request.args.get('q', '')
    max_results = request.args.get('max_results', 5, type=int)
    if not query:
        return jsonify({"error": "El parámetro de búsqueda 'q' es requerido"}), 400
    return jsonify(bi.buscar_videos(query, max_results))

@app.route('/')
def home():
    """Página de inicio con documentación básica de la API"""
    return """
    <h1>API de Búsqueda</h1>
    <p>Endpoints disponibles:</p>
    <ul>
        <li><code>GET /api/buscar?q=texto&max_results=5</code> - Búsqueda general</li>
        <li><code>GET /api/buscar/noticias?q=texto&max_results=5</code> - Búsqueda de noticias</li>
        <li><code>GET /api/buscar/imagenes?q=texto&max_results=5</code> - Búsqueda de imágenes</li>
        <li><code>GET /api/buscar/videos?q=texto&max_results=5</code> - Búsqueda de videos</li>
    </ul>
    <p>Parámetros:</p>
    <ul>
        <li><code>q</code>: (requerido) Texto a buscar</li>
        <li><code>max_results</code>: (opcional, default=5) Número máximo de resultados</li>
    </ul>
    """

if __name__ == '__main__':
    host = os.getenv('API_HOST', 'localhost')
    port = int(os.getenv('API_PORT', 5008))
    debug = os.getenv('API_DEBUG', 'False').lower() == 'true'
    app.run(host=host, port=port, debug=debug)
