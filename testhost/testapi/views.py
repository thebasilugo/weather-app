from django.shortcuts import render
import requests

def get_lon_lat(place):
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
    "q" : "Nigeria,abeokuta",
    "key": "1bf7cd2a2df44832b4b3ef23d2a0424c",
}
    response = requests.get(url, params=params)
    data = response.json()
    
    lat = data['results'][0]['geometry']['lat']
    lng = data['results'][0]['geometry']['lng']
    return lat , lng
    
# Create your views here.
def home(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        city = request.POST.get('city')
        place = f"{country}, {city}"
        lat, lon = get_lon_lat(place)

        para = {
            "lon": lon,
            "lat": lat,
            "APPID": "dca1f097290db4624ce9c2de09769ed5",
        }

        connection = requests.get("http://api.openweathermap.org/data/2.5/weather", params=para)
        data = connection.json()
        print(f'the data {data}')
        return render(request, "index.html", {'data': data})
        


    return render(request, "index.html")


