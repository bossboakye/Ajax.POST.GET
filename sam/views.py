from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .forms import ClientForm
from .models import Client

# Create your views here.

def indexView(request):
    form = ClientForm()
    clients = Client.objects.all()
    return render(request, "index.html", {"form": form, "clients": clients})

#def table(request):
#    table = Client.objects.all()
#    return render(request, 'tables.html', {"table": table})


def postClient(request):
    if request.is_ajax and request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            instance = form.save()
            ser_instance = serializers.serialize("json", [instance, ])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # errors
            return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": ""}, status=400)


def checkOwnerID(request):
    if request.is_ajax and request.method == 'GET':
        owner_ID = request.GET.get("owner_ID", None)
        if Client.objects.filter(owner_ID=owner_ID).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)


def checkContact(request):
    if request.is_ajax and request.method == 'GET':
        contact = request.GET.get("contact", None)
        if Client.objects.filter(contact=contact).exists():
            return JsonResponse({"valid": False}, status=200)
        else:
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)

