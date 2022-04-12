from django.shortcuts import render
from . models import Page
#from django.http import HttpResponse


# Create your views here.
def index(request, pagename):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
    }
    # assert False
    #return HttpResponse("<h1> Digte fra sygesengen</h1")
    return render(request, 'pages/page.html', context)