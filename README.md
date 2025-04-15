# 🗺️ Mapa Interativo de Postos de Combustível no Ceará - Python + Folium

![Mapa Interativo](img/mapa.png)

Este projeto Python utiliza dados da Overpass API (OpenStreetMap) para mapear postos de combustível no estado do Ceará e exibi-los em um mapa interativo com recursos de clusterização e ferramentas adicionais como medição e visualização em tela cheia.

## 🚀 Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [Folium](https://python-visualization.github.io/folium/)
- [Geopy](https://geopy.readthedocs.io/)
- [Overpass API](https://overpass-api.de/)
- [OpenStreetMap](https://www.openstreetmap.org/)

## 🌍 O que mais é possível rastrear com a Overpass API?

A Overpass API permite consultar praticamente qualquer dado mapeado no OpenStreetMap! Com isso, você pode adaptar este projeto para rastrear:

- 🚑 Hospitais e postos de saúde (`amenity=hospital`, `amenity=clinic`)
- 🏫 Escolas e universidades (`amenity=school`, `amenity=university`)
- 🏦 Bancos e caixas eletrônicos (`amenity=bank`, `amenity=atm`)
- 🛒 Supermercados e feiras (`shop=supermarket`, `shop=greengrocer`)
- 🚌 Paradas de ônibus e estações (`highway=bus_stop`, `railway=station`)
- ⚽ Quadras esportivas, praças, parques (`leisure=pitch`, `leisure=park`)
- 🏨 Hotéis e pousadas (`tourism=hotel`, `tourism=guest_house`)

Basta ajustar a *query* da Overpass API para mudar o tipo de estabelecimento que você quer mapear. A estrutura do código pode ser reaproveitada facilmente!

📚 Você pode explorar mais tags no [TagInfo do OSM](https://taginfo.openstreetmap.org/).

## 📌 Funcionalidades do código

- Busca automática da localização do estado do Ceará (via Geopy/Nominatim)
- Consulta à API Overpass para localizar postos de combustível
- Geração de mapa interativo com:
  - Marcadores agrupados (cluster)
  - Popups com nome, marca e endereço do posto
  - Controles de zoom, medição de distâncias e tela cheia
- Exportação para HTML para visualização no navegador

## 🛠️ Instalação e Execução

### 1. Clone o repositório ou baixe o arquivo `.py`

git clone https://github.com/seuusuario/mapa-postos-ceara.git
cd mapa-postos-ceara

### 2. Instale as dependências

Use o `pip` para instalar as bibliotecas necessárias:

pip install -r requirements.txt

## 🤝 Contribuições

Contribuições são bem-vindas! Fique à vontade para abrir issues ou pull requests com melhorias, correções ou novas funcionalidades.

---

Desenvolvido com 💻 por [Erick Sousa](https://www.linkedin.com/in/erick-sousa-b4183a214/)

📬 Contato: erickoliveira859@gmail.com
