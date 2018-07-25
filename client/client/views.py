from django.http import HttpResponse
from django.conf import settings


def home(request):
    user = request.user
    url = settings.CLIENT_SERVER
    return HttpResponse("Hi %s, <br/> Welcome. <a href='%s'>server url</a>" % (user, url))
