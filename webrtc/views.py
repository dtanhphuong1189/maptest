from django.shortcuts import render
from django.conf import settings

def caller(request):
    context = {
        'sip': settings.SIP_CONFIG
    }
    return render(request, 'webrtc/caller.html', context)

# Create your views here.
