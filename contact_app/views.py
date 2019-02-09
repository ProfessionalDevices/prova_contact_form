from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessaggioModelForm
# Create your views here.

def contactView(request):
    if request.method == "POST":
        form = MessaggioModelForm(request.POST)
        if form.is_valid():
            nuovo_messaggio = form.save()
            return HttpResponse("Grazie per averci contattato!")
    else:
        form = MessaggioModelForm()
    context = {"form": form}
    return render(request, "contact_app/form_contatto.html", context) 
