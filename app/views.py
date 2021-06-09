"""
Definition of views.
"""

from django.contrib import admin
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return render(
             request,
             'app/index.html',
             {
                 'title':'Home Page',
                'year':datetime.now().year,
             })
    else:
         return HttpResponse('<p>Welcome to <a href="https://djangocas.dev">django-cas-ng</a>.</p><p><a href="/accounts/login">Login</a></p>')

    
    

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def index(request: HttpRequest) -> HttpResponse:
    header = '''<!DOCTYPE html>
<html>
  <head>
    <title>django-cas-ng example demo</title>
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0, minimum-scale=1.0">
  </head>
  <body>
  <h1>Welcome to django-cas-ng demo BLAAHHHHH</h1>'''

    footer = '''<p>Related post:</p>
    <ul>
        <li><a href="https://djangocas.dev/blog/django-cas-ng-example-project/">Step by step to setup a django-cas-ng example project</a></li>
    </ul>
    <hr><p><a href="https://djangocas.dev/">Project homepage</a></p>
  </body>
</html>'''

    if request.user.is_authenticated:
        body = """
        <p>You logged in as <strong>%s</strong>.</p>
        <p><a href="/accounts/logout">Logout</a></p>
         """ % request.user.username
    else:
        body = '<p><a href="/accounts/login">Login</a></p>'

    return HttpResponse(header + body + footer)