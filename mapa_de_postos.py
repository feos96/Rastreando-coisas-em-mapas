import requests
import folium
from geopy.geocoders import Nominatim
from folium.plugins import MarkerCluster, Fullscreen, MeasureControl

# Configuração inicial
print("Iniciando busca de postos de combustível no Ceará...")

# 1. Centralizar o mapa no Ceará
geolocator = Nominatim(user_agent="ceara_fuel_stations")
try:
    location = geolocator.geocode("Ceará, Brasil")
    ce_coords = [location.latitude, location.longitude]
    print(f"Coordenadas do Ceará: {ce_coords}")
except Exception as e:
    print(f"Erro ao geocodificar: {e}")
    ce_coords = [-5.4984, -39.3206]  # Coordenadas aproximadas do Ceará

# 2. Criar mapa base
mapa = folium.Map(location=ce_coords,
                  zoom_start=8,
                  tiles='OpenStreetMap',
                  control_scale=True)

# Adicionar cluster
marker_cluster = MarkerCluster().add_to(mapa)

# 3. Buscar postos na Overpass API
print("Consultando a API Overpass para postos no Ceará...")
overpass_url = "https://overpass-api.de/api/interpreter"
query = """
[out:json];
area["name"="Ceará"]["admin_level"="4"]->.searchArea;
(
  node["amenity"="fuel"](area.searchArea);
  way["amenity"="fuel"](area.searchArea);
  relation["amenity"="fuel"](area.searchArea);
);
out center;
"""

try:
    response = requests.get(overpass_url, params={'data': query}, timeout=120)
    response.raise_for_status()
    data = response.json()
    print(f"Encontrados {len(data['elements'])} postos no Ceará")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
    data = {"elements": []}

# 4. Processar e adicionar marcadores
print("Processando dados e criando marcadores...")
postos_processados = 0

for elemento in data['elements']:
    try:
        # Obter coordenadas
        if elemento['type'] == 'node':
            lat, lon = elemento['lat'], elemento['lon']
        elif 'center' in elemento:
            lat, lon = elemento['center']['lat'], elemento['center']['lon']
        else:
            continue

        # Informações
        tags = elemento.get('tags', {})
        nome = tags.get('name', 'Posto sem nome')
        marca = tags.get('brand', 'Marca não especificada')
        endereco = tags.get('addr:street', 'Endereço não disponível')

        popup_content = f"""
        <b>{nome}</b><br>
        <b>Marca:</b> {marca}<br>
        <b>Endereço:</b> {endereco}<br>
        """
        popup = folium.Popup(popup_content, max_width=250)

        folium.Marker(
            location=[lat, lon],
            popup=popup,
            icon=folium.Icon(color='red', icon='gas-pump', prefix='fa'),
            tooltip=nome
        ).add_to(marker_cluster)

        postos_processados += 1

    except Exception as e:
        print(f"Erro ao processar elemento {elemento.get('id')}: {e}")

# 5. Controles extras
folium.LayerControl().add_to(mapa)
Fullscreen(position='topright').add_to(mapa)
MeasureControl().add_to(mapa)

# 6. Salvar como HTML
print(f"Processamento concluído! {postos_processados} postos mapeados no Ceará.")
mapa.save("postos_ceara.html")
print("Mapa salvo como 'postos_ceara.html'. Abra esse arquivo no navegador para visualizar.")