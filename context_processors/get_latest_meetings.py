from django.conf import settings
from uppsala.meet.models import Meet

def get_latest_meetings(request):
    "A context processor that provides the latest meeting suggestions" 
    meeting_suggestions = Meet.objects.all()	
    return locals()
