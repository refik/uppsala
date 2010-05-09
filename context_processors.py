from uppsala.shoutbox.models import shout
import hashlib


def get_latest_shouts(request):
    "A context processor that provides the latest shouts."
    
    latest_shouts_list = shout.objects.all().order_by('-pub_date')[:5]
    gravatars = []
    for x in latest_shouts_list:
        x.gravatar = hashlib.md5(x.user.email).hexdigest()
    return {
        'latest_shouts': latest_shouts_list,
    }
