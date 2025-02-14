import sys
import subprocess
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def get_proxy_config():
    """
    Obtiene la configuración del proxy desde las variables de entorno.
    Retorna un diccionario con la configuración del proxy o None si no está configurado.
    """
    proxy_host = os.getenv('PROXY_HOST')
    proxy_port = os.getenv('PROXY_PORT')
    
    if not proxy_host or not proxy_port:
        return None
    
    proxy_user = os.getenv('PROXY_USER')
    proxy_pass = os.getenv('PROXY_PASS')
    
    if proxy_user and proxy_pass:
        proxy_url = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"
    else:
        proxy_url = f"http://{proxy_host}:{proxy_port}"
    
    return {
        'http': proxy_url,
        'https': proxy_url
    }

def instalar_paquete(paquete):
    """
    Instala un paquete mediante pip si no está ya instalado.
    """
    try:
        __import__(paquete)
    except ImportError:
        print(f"Instalando el paquete '{paquete}'...")
        subprocess.check_call(["python", "-m", "pip", "install", paquete])

# Aseguramos que duckduckgo_search esté instalado
instalar_paquete("duckduckgo_search")

# Importamos la clase DDGS (la interfaz actual para realizar búsquedas)
from duckduckgo_search import DDGS

def buscar(consulta, max_resultados=5):
    """
    Realiza una búsqueda general en Internet utilizando DuckDuckGo y devuelve los resultados en un diccionario.
    
    :param consulta: Texto a buscar.
    :param max_resultados: Número máximo de resultados a obtener.
    :return: Diccionario con la consulta y los resultados.
    """
    try:
        proxies = get_proxy_config()
        with DDGS(proxies=proxies) as ddgs:
            resultados_generador = ddgs.text(consulta, max_results=max_resultados)
            resultados_lista = list(resultados_generador)
    except Exception as e:
        print(f"Ocurrió un error durante la búsqueda: {e}")
        return {"consulta": consulta, "resultados": {}}
    
    resultados_dict = {}
    for i, res in enumerate(resultados_lista, start=1):
        resultados_dict[f"resultado_{i}"] = {
            "titulo": res.get("title", "Sin título"),
            "enlace": res.get("href", "Sin enlace"),
            "descripcion": res.get("body", "Sin descripción")
        }
    
    return {"consulta": consulta, "resultados": resultados_dict}

def buscar_noticias(consulta, max_resultados=5):
    """
    Realiza una búsqueda de noticias utilizando DuckDuckGo y devuelve los resultados en un diccionario.
    
    :param consulta: Texto a buscar.
    :param max_resultados: Número máximo de resultados a obtener.
    :return: Diccionario con la consulta y los resultados.
    """
    try:
        proxies = get_proxy_config()
        with DDGS(proxies=proxies) as ddgs:
            resultados_generador = ddgs.news(consulta, max_results=max_resultados)
            resultados_lista = list(resultados_generador)
    except Exception as e:
        print(f"Ocurrió un error durante la búsqueda de noticias: {e}")
        return {"consulta": consulta, "resultados": {}}
    
    resultados_dict = {}
    for i, res in enumerate(resultados_lista, start=1):
        resultados_dict[f"resultado_{i}"] = {
            "titulo": res.get("title", "Sin título"),
            "enlace": res.get("url", "Sin enlace"),
            "descripcion": res.get("body", "Sin descripción"),
            "fecha": res.get("date", "Sin fecha"),
            "fuente": res.get("source", "Fuente desconocida"),
            "imagen": res.get("image", "Sin imagen")
        }
    
    return {"consulta": consulta, "resultados": resultados_dict}

def buscar_imagenes(consulta, max_resultados=5):
    """
    Realiza una búsqueda de imágenes utilizando DuckDuckGo y devuelve los resultados en un diccionario.
    
    :param consulta: Texto a buscar.
    :param max_resultados: Número máximo de resultados a obtener.
    :return: Diccionario con la consulta y los resultados.
    """
    try:
        proxies = get_proxy_config()
        with DDGS(proxies=proxies) as ddgs:
            resultados_generador = ddgs.images(consulta, max_results=max_resultados)
            resultados_lista = list(resultados_generador)
    except Exception as e:
        print(f"Ocurrió un error durante la búsqueda de imágenes: {e}")
        return {"consulta": consulta, "resultados": {}}
    
    resultados_dict = {}
    for i, res in enumerate(resultados_lista, start=1):
        resultados_dict[f"resultado_{i}"] = {
            "titulo": res.get("title", "Sin título"),
            "enlace": res.get("link", "Sin enlace"),
            "imagen_url": res.get("image", "Sin URL de imagen"),
            "thumbnail": res.get("thumbnail", "Sin thumbnail"),
            "fuente": res.get("source", "Fuente desconocida"),
            "altura": res.get("height", "Desconocida"),
            "anchura": res.get("width", "Desconocida")
        }
    
    return {"consulta": consulta, "resultados": resultados_dict}

def buscar_videos(consulta, max_resultados=5):
    """
    Realiza una búsqueda de videos utilizando DuckDuckGo y devuelve los resultados en un diccionario.
    
    :param consulta: Texto a buscar.
    :param max_resultados: Número máximo de resultados a obtener.
    :return: Diccionario con la consulta y los resultados.
    """
    try:
        proxies = get_proxy_config()
        with DDGS(proxies=proxies) as ddgs:
            resultados_generador = ddgs.videos(consulta, max_results=max_resultados)
            resultados_lista = list(resultados_generador)
    except Exception as e:
        print(f"Ocurrió un error durante la búsqueda de videos: {e}")
        return {"consulta": consulta, "resultados": {}}
    
    resultados_dict = {}
    for i, res in enumerate(resultados_lista, start=1):
        resultados_dict[f"resultado_{i}"] = {
            "titulo": res.get("title", "Sin título"),
            "enlace": res.get("content", "Sin enlace"),  
            "descripcion": res.get("description", "Sin descripción"),
            "duracion": res.get("duration", "Duración desconocida"),
            "autor": res.get("publisher", "Autor desconocido"),
            "thumbnail": res.get("images", {}).get("large", "Sin thumbnail"),  
            "vistas": res.get("statistics", {}).get("viewCount", "Desconocido")  
        }
    
    return {"consulta": consulta, "resultados": resultados_dict}

if __name__ == "__main__":
    # Modo interactivo: se pide al usuario el texto de búsqueda y tipo de búsqueda
    print("\nTipos de búsqueda disponibles:")
    print("1. Búsqueda general")
    print("2. Búsqueda de noticias")
    print("3. Búsqueda de imágenes")
    print("4. Búsqueda de videos")
    
    tipo_busqueda = input("\nSeleccione el tipo de búsqueda (1-4): ")
    consulta_usuario = input("Ingrese el texto para buscar: ")
    
    # Realizar la búsqueda según la opción seleccionada
    if tipo_busqueda == "1":
        resultados = buscar(consulta_usuario)
    elif tipo_busqueda == "2":
        resultados = buscar_noticias(consulta_usuario)
    elif tipo_busqueda == "3":
        resultados = buscar_imagenes(consulta_usuario)
    elif tipo_busqueda == "4":
        resultados = buscar_videos(consulta_usuario)
    else:
        print("Opción no válida. Utilizando búsqueda general por defecto.")
        resultados = buscar(consulta_usuario)
    
    # Mostrar resultados
    print("\nResultados de la búsqueda:")
    for key, value in resultados.get("resultados", {}).items():
        print(f"\n{key}:")
        for campo, contenido in value.items():
            print(f"  {campo.capitalize()}: {contenido}")
