"""First try out. don't mind the errors"""
from datetime import datetime
from django.http import HttpResponse

date = datetime.now()
HTML_STRING = f"<h1> Welcome to the note application </h1><br> Today is {date} " 


def home_view(request):
    return HttpResponse(HTML_STRING)