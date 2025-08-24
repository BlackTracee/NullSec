import phonenumbers
from test import number
from phonenumbers import carrier, geocoder
from opencage.geocoder import OpenCageGeocode
import folium

# Faz o parsing do número
pepnumber = phonenumbers.parse(number)

# Pega o país
location_country = geocoder.country_name_for_number(pepnumber, 'pt')
print("País:", location_country)

# Pega a descrição mais detalhada (estado/cidade associada ao DDD)
location_city = geocoder.description_for_number(pepnumber, 'pt')
print("Região aproximada:", location_city)

# Pega a operadora
serviceprovider = carrier.name_for_number(pepnumber, 'pt')
print("Operadora:", serviceprovider)

# Usa a API do OpenCage para converter a região em coordenadas
key = '944709d076f94d72977655a555f0a479'  # sua chave de API
geocoder_api = OpenCageGeocode(key)

# Tenta localizar pela cidade + país
query = f"{location_city}, {location_country}"
results = geocoder_api.geocode(query)

if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    print("Latitude:", lat)
    print("Longitude:", lng)

    # Cria mapa interativo
    myMap = folium.Map(location=[lat, lng], zoom_start=10)
    folium.Marker([lat, lng], popup=f"{location_city} - {location_country}").add_to(myMap)

    myMap.save("mylocation.html")
    print("Mapa salvo em mylocation.html")
else:
    print("Não foi possível localizar a cidade/região.")

input("Pressione Enter para sair...")
