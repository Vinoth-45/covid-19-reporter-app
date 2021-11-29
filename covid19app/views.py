from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    data = True
    result = None
    globalsummary = None
    countries = None
    india = {
     "ID": "a22566f0-f337-4db6-b2ef-03801a178c79",
     "Country": "India",
     "CountryCode": "IN",
     "Slug": "india",
     "NewConfirmed": 7629,
     "TotalConfirmed": 34352312,
     "NewDeaths": 482,
     "TotalDeaths": 460747,
     "NewRecovered": 0,
     "TotalRecovered": 0,
     "Date": "2021-11-07T05:14:57.618Z",
     "Premium": { }
             }

    while data:
        try:
            result = requests.get('https://api.covid19api.com/summary')
            json = result.json()
            globalsummary = json['Global']
            countries = json['Countries']
            data = False

        except:
            data = True

    return render(request, 'index.html', {'globalsummary': globalsummary,
                                          'countries': countries,
                                          'india' : india})




