from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    redirect_path = reverse('index')
    return HttpResponseRedirect(redirect_path)