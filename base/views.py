from django.shortcuts import render, redirect
from .models import Destination, TravelPackage, AgencyReview, FeaturedPackage, Agencie, NewsLetter, Reservation
from .forms import ReservationForm, ContactForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index(request):
    data = []
    if request.GET.get('q') != None:
        try:
            search_query = request.GET.get('q')
            return redirect(f'/packages?q={search_query}', data)
        except:
            pass
    if request.method == 'POST':
        newsletter = request.POST['newsletteremail']
        NewsLetter.objects.create(email=newsletter, user=request.user)

    return render(request, 'index.html', {
        'featured_packages': FeaturedPackage.objects.all(),
        'packages': TravelPackage.objects.all(),
        'destinations': Destination.objects.all(),
        'search': data,
        'agencies': Agencie.objects.all()
    })


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
        else:
            messages.error(request, form.errors)
    return render(request, 'contact.html', {})


def service(request):
    return render(request, 'service.html', {})


def testimonial(request):
    return render(request, 'testimonial.html', {})


def packages(request,):
    packages = {'data': [], 'status': True}
    try:
        search = request.GET.get('q')
        for x in TravelPackage.objects.filter(destination__icontains=search):
            packages['data'].append(x)
    except:
        packages['data'] = TravelPackage.objects.all()
        packages['status'] = False
    return render(request, 'package.html', {
        'packages': packages
    })


def detail_package(request, id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReservationForm(request.POST)
            done = False
            if Reservation.objects.filter(name=request.POST['name']).exists():
                if form.is_valid() and not done:
                    checked_from = form.save(commit=False)
                    checked_from.package = TravelPackage.objects.get(id=id)
                    form.save()
                    messages.success(
                        request, 'Your reservation has been sent!')
                else:
                    messages.error(request, form.errors)
            else:
                messages.error(request, "Name Already Exists!")
        else:
            return redirect('signin')
    return render(request, 'single.html', {
        'package': TravelPackage.objects.get(id=id),
    })


def signin(request):
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'signinpage.html', {})


def registration(request):
    if request.method == 'POST':
        # Retrieve form data
        agency_name = request.POST.get('agency_name')
        admin_name = request.POST.get('admin_name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        state = request.POST.get('state')
        district = request.POST.get('district')
        business_address = request.POST.get('business_address')
        company_description = request.POST.get('company_description')
        website_link = request.POST.get('website_link')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        form_data = {
            'username': agency_name,
            'password1': password1,
            'password2': password2,
            'email': email
        }
        form = UserCreationForm(data=form_data)
        if form.is_valid():
            form.save()
            x = User.objects.get(username=agency_name)
            group = Group.objects.get(name='travel_agency')
            x.groups.add(group)
            x.is_staff = True
            x.save()

            agency = Agencie.objects.create(
                user=x,
                agency_name=agency_name,
                admin_name=admin_name,
                contact_number=contact_number,
                state=state,
                district=district,
                business_address=business_address,
                company_description=company_description,
                website_link=website_link,
            )
            agency.save()
            return redirect('signin')
        else:
            print(form.errors)
    return render(request, 'registration.html', {})


def agencies(request, id):
    ag = Agencie.objects.get(id=id)
    package = TravelPackage.objects.filter(agency=id)
    reviews = AgencyReview.objects.filter(for_agency=ag)
    if request.method == 'POST':
        if request.POST['message'] != '':
            AgencyReview.objects.create(
                for_agency=ag, author=request.user, review=request.POST['message'])
    return render(request, 'agency.html', {
        'agency': ag,
        'reviews': reviews,
        'packages': package
    })
