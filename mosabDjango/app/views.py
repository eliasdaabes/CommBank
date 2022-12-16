"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html'
    )

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

def forgotPassword(request):
    """Renders the forgotPassword page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/forgetPassword.html',
        {}
    )

def updatePassword(request):
    """Renders the forgotPassword page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/updatePassword.html',
        {}
    )

def list(request):
    """Renders the list page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/list.html',
        {}
    )

def managerSignIn(request):
    """Renders the list page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/managerSignIn.html',
        {}
    )

def secretarySignIn(request):
    """Renders the list page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/secretarySignIn.html',
        {}
    )

def volunteerSignIn(request):
    """Renders the list page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/volunteerSignIn.html',
        {}
    )