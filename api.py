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
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>API de Búsqueda</title>
        <style>
            body { font-family: 'Segoe UI', Arial, sans-serif; background: #f7f7f7; color: #222; margin: 0; padding: 0; }
            .container { max-width: 700px; margin: 40px auto; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px #0001; padding: 32px; }
            h1 { color: #226699; }
            table { width: 100%; border-collapse: collapse; margin-bottom: 24px; }
            th, td { border: 1px solid #ddd; padding: 8px 12px; }
            th { background: #f0f4fa; }
            code { background: #eee; padding: 2px 6px; border-radius: 4px; }
            .example { background: #f8f8e7; border-left: 4px solid #ffd700; padding: 12px; margin-bottom: 16px; }
            .footer { margin-top: 40px; font-size: 0.9em; color: #888; text-align: right; }
            @media (max-width: 600px) {
                .container { padding: 8px; }
                table, th, td { font-size: 0.95em; }
            }
        </style>
    </head>
    <body>
    <div class="container">
        <h1>API de Búsqueda</h1>
        <p>Realiza búsquedas en Internet usando DuckDuckGo: texto, noticias, imágenes y videos.<br>
        <b>Endpoints disponibles:</b></p>
        <table>
            <tr>
                <th>Tipo</th>
                <th>Endpoint</th>
                <th>Descripción</th>
            </tr>
            <tr>
                <td>General</td>
                <td><code><a href="/api/buscar?q=python">/api/buscar</a></code></td>
                <td>Búsqueda general de texto</td>
            </tr>
            <tr>
                <td>Noticias</td>
                <td><code><a href="/api/buscar/noticias?q=ciencia">/api/buscar/noticias</a></code></td>
                <td>Búsqueda de noticias</td>
            </tr>
            <tr>
                <td>Imágenes</td>
                <td><code><a href="/api/buscar/imagenes?q=tecnologia">/api/buscar/imagenes</a></code></td>
                <td>Búsqueda de imágenes</td>
            </tr>
            <tr>
                <td>Videos</td>
                <td><code><a href="/api/buscar/videos?q=robotica">/api/buscar/videos</a></code></td>
                <td>Búsqueda de videos</td>
            </tr>
        </table>
        <h3>Parámetros</h3>
        <ul>
            <li><code>q</code> <b>(requerido)</b>: Texto a buscar</li>
            <li><code>max_results</code> <b>(opcional, default=5)</b>: Número máximo de resultados</li>
        </ul>
        <h3>Ejemplos de Uso</h3>
        <div class="example">
            <b>Buscar noticias sobre IA:</b><br>
            <code>curl "http://localhost:5008/api/buscar/noticias?q=inteligencia+artificial&max_results=3"</code>
        </div>
        <div class="example">
            <b>Buscar imágenes de gatos:</b><br>
            <code>curl "http://localhost:5008/api/buscar/imagenes?q=gatos"</code>
        </div>
        <div class="example">
            <b>Probar en navegador:</b><br>
            <a href="/api/buscar?q=python">/api/buscar?q=python</a>
        </div>
        <div class="footer">
            Buscador TecCam API &mdash; Versión 1.0 &copy; 2025
        </div>
    </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    host = os.getenv('API_HOST', 'localhost')
    port = int(os.getenv('API_PORT', 5008))
    debug = os.getenv('API_DEBUG', 'False').lower() == 'true'
    app.run(host=host, port=port, debug=debug)
