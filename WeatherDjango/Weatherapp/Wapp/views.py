from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
from .models import weatherdata
  
def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        ''' api key might be expired use your own api_key 
            place api_key in place of appid="01454684d32a738343f701c1622bddfe"  '''
  
        # source contain JSON data from API 
  
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&appid=01454684d32a738343f701c1622bddfe').read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
        temperature_kelvin = list_of_data['main']['temp']
        temperature_celsius = temperature_kelvin-273.15

        wdata = weatherdata()

        wdata.city = city
        wdata.country_code = str(list_of_data['sys']['country'])
        wdata.coord = str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat'])
        wdata.temp = str(list_of_data['main']['temp']) + 'k'
        wdata.pressure = str(list_of_data['main']['pressure'])
        wdata.humidity = str(list_of_data['main']['humidity'])
        wdata.save()

        bdata = weatherdata.objects.all().order_by('timestamp')
        
        # data for variable list_of_data 
        data = { 
            "bdata":bdata, 
            "city":city,       
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 

       

      
        print(data) 
    else: 
        data ={} 
    return render(request, "index.html",data) 

