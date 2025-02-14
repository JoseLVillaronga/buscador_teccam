from duckduckgo_search import DDGS

# Prueba directa de ddg_news para ver la estructura completa
with DDGS() as ddgs:
    resultados = list(ddgs.news("tecnologia", max_results=1))
    print("\nEstructura completa de la respuesta de ddg_news:")
    import json
    print(json.dumps(resultados[0], indent=2, ensure_ascii=False))
