from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
def index(request):
    args = {
        'h1':'Cabecera',
        'p1' :'mi primer parrafo',
        }
    return render_to_response('index.html', args)

