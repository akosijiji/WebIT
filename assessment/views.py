from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .filters import ClientFilter
from .models import Client
from .forms import ClientForm
from django.contrib import messages

def index(request):
    # latest_client_list = Client.objects.order_by('id')
    # context = {'latest_client_list': latest_client_list}
    # return render(request, 'assessment/index.html', context)
    client_list = Client.objects.all()
    # client_list = client_list.order_by('client_name', 'email_address', 'phone_number', 'suburb')
    client_filter = ClientFilter(request.GET, queryset=client_list)
    messages.info(request, request.GET)
    return render(request, 'assessment/index.html', {'filter': client_filter})

def create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/")
            except:
                pass
    else:
        form = ClientForm()
    return render(request, 'assessment/create.html', {'form': form})

def edit(request, id):
    client = Client.objects.get(id=id)
    return render(request, 'assessment/edit.html', {'client': client})

def update(request, id):
    client = Client.objects.get(id=id)
    form = ClientForm(request.POST, instance = client)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'assessment/edit.html', {'client': client})

def destroy(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect("/")