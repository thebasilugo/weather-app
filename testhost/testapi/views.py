from django.shortcuts import render
import requests
import json

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
        edited_data ={'weather':data['weather'][0]['main'],'main': data['main'], 'visibility': data['visibility']}
        edited_data = json.dumps(edited_data)
        edited_data = json.loads(edited_data.replace("'", "\""))
        edited_data = json.dumps(edited_data)
        edited_data = json.loads(edited_data)
        context = {
            'weather': edited_data['weather'],
            'temp_min': edited_data['main']['temp_min'],
            'temp_max': edited_data['main']['temp_max'],
        }
        print(f'the data {edited_data}')
        return render(request, "index.html", context)


    return render(request, "index.html")
