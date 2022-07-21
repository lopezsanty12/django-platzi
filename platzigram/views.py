""" Platzigram view """

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """ Return a greeting """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f"Hello World! this is the current server time: {now}")

def hi(request):
    """ Hi """
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))