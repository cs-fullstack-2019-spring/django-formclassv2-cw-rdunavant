from django.shortcuts import render
from django.http import HttpResponse
from . forms import views
from django.http import include, index

# Create your views here.
def ApplicationForm(request):
    newForm = ApplicationForm()
    context = {
        "newForm": newForm
    }
    return render(request, "App/index.html")