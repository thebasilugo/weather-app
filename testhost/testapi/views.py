from django.shortcuts import render
import requests

def get_lon_lat(place):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": place,
        "key": "YOUR_API_KEY"
    }
    response = requests.get(url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lng'], location['lat']
    else:
        return None

# Create your views here.
def home(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        city = request.POST.get('city')
        place = f"{country}, {city}"
        lon, lat = get_lon_lat(place)

        para = {
            "lon": lon,
            "lat": lat,
            "APPID": "dca1f097290db4624ce9c2de09769ed5",
        }

        connection = requests.get("http://api.openweathermap.org/data/2.5/weather", params=para)
        data = connection.json()
        
        

    return render(request, "index.html")


