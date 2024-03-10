from django.shortcuts import render, redirect
from .models import Destination, TravelPackage
from .forms import ContactForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index(request):
    data = []
    if request.GET.get("q") != None and request.GET.get("d") != None:
        try:
            search_query = request.GET.get("q")
            return redirect(
                f"/packages?q={search_query}&d={request.GET.get('d')}", data
            )
        except:
            pass
    return render(
        request,
        "index.html",
        {
            "packages": TravelPackage.objects.all(),
            "search": data,
        },
    )


def about(request):
    return render(request, "about.html", {})


def bot(request):
    return render(request, "chatbot.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent!")
        else:
            messages.error(request, form.errors)
    return render(request, "contact.html", {})


def service(request):
    return render(request, "service.html", {})


def testimonial(request):
    return render(request, "testimonial.html", {})


def packages(
    request,
):
    packages = {"data": [], "status": True}
    try:
        search = request.GET.get("q")
        no_of_days = request.GET.get("d")
        for x in TravelPackage.objects.filter(
            destination__icontains=search, duration_days=no_of_days
        ):
            packages["data"].append(x)
    except:
        packages["data"] = TravelPackage.objects.all()
        packages["status"] = False
    return render(request, "package.html", {"packages": packages})


def detail_package(request, id):
    travel = TravelPackage.objects.get(id=id)
    totel_price = travel.price
    location = travel.title

    if request.method == "POST":
        selected_destinations = request.POST.getlist("states[]")
        travel.destinations.clear()
        for destination_id in selected_destinations:
            destination = Destination.objects.get(id=destination_id)
            travel.destinations.add(destination)

            
    for x in travel.destinations.all():
        totel_price += x.price
    return render(
        request,
        "single.html",
        {
            "package": travel,
            "totel_price":totel_price,
            'selected_destinations': travel.destinations.all(),
            "destinations": Destination.objects.filter(location=location),
        },
    )


def signin(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "signinpage.html", {})
