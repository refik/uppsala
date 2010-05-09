from django.conf import settings
from uppsala.radio import radio

def get_latest_radios(request):
    "A context processor that provides the latest radio stations" 
    stations = radio.stations()	
    return locals()
