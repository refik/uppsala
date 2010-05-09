from django.conf import settings
from uppsala.shoutbox.models import shout
import hashlib


def get_latest_shouts(request):
    "A context processor that provides the latest shouts."
    
    latest_shouts = shout.objects.all().order_by('-pub_date')[:5]
    gravatars = []
    for x in latest_shouts:
        x.gravatar = hashlib.md5(x.user.email).hexdigest()
    return locals()
