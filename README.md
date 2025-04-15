# 🗺️ Mapa Interativo de Postos de Combustível no Ceará - Python + Folium

Este projeto Python utiliza dados da Overpass API (OpenStreetMap) para mapear postos de combustível no estado do Ceará e exibi-los em um mapa interativo com recursos de clusterização e ferramentas adicionais como medição e visualização em tela cheia.

## 🚀 Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [Folium](https://python-visualization.github.io/folium/)
- [Geopy](https://geopy.readthedocs.io/)
- [Overpass API](https://overpass-api.de/)
- [OpenStreetMap](https://www.openstreetmap.org/)

## 📌 Funcionalidades

- Busca automática da localização do estado do Ceará (via Geopy/Nominatim)
- Consulta à API Overpass para localizar postos de combustível
- Geração de mapa interativo com:
  - Marcadores agrupados (cluster)
  - Popups com nome, marca e endereço do posto
  - Controles de zoom, medição de distâncias e tela cheia
- Exportação para HTML para visualização no navegador

## 🛠️ Instalação e Execução

### 1. Clone o repositório ou baixe o arquivo `.py`

```bash
git clone https://github.com/seuusuario/mapa-postos-ceara.git
cd mapa-postos-ceara