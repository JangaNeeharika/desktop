from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum

from .models import Child
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Sponsor
from .models import OldAgePerson,OldAgeNeed
from .models import DemoClassRegistration
from .models import MealDonation
from django.contrib import messages
from datetime import datetime
from .forms import DemoClassForm
from .forms import DonationForm
from .models import GeneralChildNeed
from .forms import GeneralDonationForm
from .models import GeneralDonation
def donation_view(request):
    submitted = False

    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/donation?submitted=True')
    else:
        form = DonationForm()
        if 'submitted' in request.GET:
            submitted = True

    general_needs = GeneralChildNeed.objects.all()
    return render(request, 'donation.html', {
        'form': form,
        'submitted': submitted,
        'general_needs': general_needs
    })
def demo_class_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        skills = request.POST.get('skills')
        message = request.POST.get('message')
        
        DemoClassRegistration.objects.create(
            name=name,
            email=email,
            skills=skills,
            message=message,
            
        )
        submitted = True
        return render(request, 'demo.html', {'submitted': True})

def home(request):
    return render(request, 'home.html')

def food(request):
    bookings = MealDonation.objects.values('donation_date', 'meal_time')
    booked_slots = {}
    for entry in bookings:
        date = entry['donation_date'].strftime('%Y-%m-%d')
        booked_slots.setdefault(date, []).append(entry['meal_time'])
    return render(request, 'food.html', {'booked_slots': booked_slots})

def education(request):
    return render(request,'education.html')


def donation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        items = request.POST.get('items')
        delivery = request.POST.get('delivery')
        image = request.FILES.get('image')

        GeneralDonation.objects.create(
            name=name,
            email=email,
            address=address,
            items=items,
            delivery=delivery,
            image=image
        )
        return redirect('donation')  # Refresh or redirect to a success page

    general_needs = ChildrenNeed.objects.all()  # if you use children needs model
    return render(request, 'donation.html', {'general_needs': general_needs})


def oldage(request):
    elders = OldAgePerson.objects.all()
    return render(request, 'oldage.html', {'elders': elders})

def oldage1(request):
    needs = OldAgeNeed.objects.all()
    elders = OldAgePerson.objects.all()
    return render(request, 'oldage1.html', { 'needs':needs,'elders': elders})

def admin(request):
    return render(request,'admin.html')

def dashboard(request):
    return render(request,'dashboard.html')


def suport(request):
    return render(request,'suport.html')

def children(request):
    children=Child.objects.all()
    return render(request,'children.html',{'children':children})
def demo_class_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        skills = request.POST.get('skills')
        message = request.POST.get('message')

        DemoClassRegistration.objects.create(
            name=name,
            email=email,
            skills=skills,
            message=message
        )
        messages.success(request, 'Thank you for registering for demo classes!')
        return redirect('demo_classes')

    return render(request, 'demo.html')



def sponsor(request):
    children = Child.objects.all()
    return render(request, 'sponsor.html', {'children': children})

def sponsor_thank_you(request):
    return render(request, 'sponsor_thank_you.html')

def payment_success(request):
    return render(request, 'payment_success.html')


def meal_form_view(request):
    bookings = MealDonation.objects.all()
    booked = {}
    for b in bookings:
        date = b.donation_date.strftime('%Y-%m-%d')
        booked.setdefault(date, []).append(b.meal_time)
    return render(request, 'fodd.html', {'booked_slots': json.dumps(booked)})

from django.shortcuts import render, redirect
from .models import MealDonation
from datetime import datetime

def submit_food(request):
    if request.method == 'POST':
        name = request.POST.get('donor_name')
        email = request.POST.get('donor_email')
        phone = request.POST.get('donor_phone')
        date_str = request.POST.get('donation_date')
        occasion = request.POST.get('occasion')
        meal_time = request.POST.get('meal_time')
        combo = request.POST.get('combo')
        recipient = request.POST.get('recipient')

        # Convert date string to date object
        try:
            donation_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            return render(request, 'error.html', {"message": "Invalid date format"})

        # ✅ Check if slot already booked
        if MealDonation.objects.filter(donation_date=donation_date, meal_time=meal_time).exists():
            return render(request, 'already_booked.html', {
                'donation_date': donation_date,
                'meal_time': meal_time
            })

        # ✅ Save the donation
        MealDonation.objects.create(
            donor_name=name,
            donor_email=email,
            donor_phone=phone,
            donation_date=donation_date,
            occasion=occasion,
            meal_time=meal_time,
            combo=combo,
            recipient=recipient
        )

        return redirect('payment_success')

    return redirect('/')

def sponsor_child(request, child_id=None):
    if request.method == 'POST':
        child = get_object_or_404(Child, id=child_id) if child_id else None
        Sponsor.objects.create(
            child=child,
            donor_name=request.POST.get('donor_name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            amount=request.POST.get('amount'),
            message=request.POST.get('message')
        )
        return redirect('sponsor_thank_you')  # Optional: create a thank-you page
    return redirect('sponsor')


def oldage_home(request):
    if request.method == 'POST':
        form = GeneralDonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/oldage/?submitted=true')  # Redirect with a query param
    else:
        form = GeneralDonationForm()

    submitted = request.GET.get('submitted', False)
    elders = Elder.objects.all()
    needs = Need.objects.all()

    return render(request, 'oldage1.html', {
        'form': form,
        'elders': elders,
        'needs': needs,
        'submitted': submitted
    })
from .models import ContactMessage

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            contact_number=contact_number,
            email=email,
            message=message
        )
        return render(request, 'home.html', {'success': True})

    return render(request, 'home.html')


from .models import GalleryImage

def home(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'home.html', {'gallery_images': gallery_images})

from .models import GalleryImage

def infrastructure_gallery(request):
    images = GalleryImage.objects.filter(category='infrastructure')
    return render(request, 'gallery/infrastructure.html', {'images': images})

def children_gallery(request):
    images = GalleryImage.objects.filter(category='children')
    return render(request, 'gallery/children.html', {'images': images})

def donations_gallery(request):
    images = GalleryImage.objects.filter(category='donations')
    return render(request, 'gallery/donations.html', {'images': images})

def oldage_gallery(request):
    images = GalleryImage.objects.filter(category='oldage')
    return render(request, 'gallery/oldage.html', {'images': images})

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def chart_data(request):
    labels = []
    donation_data = []
    meal_data = []

    for month in range(1, 13):
        labels.append(date(2025, month, 1).strftime('%B'))  # Jan, Feb...
        donation_sum = GeneralDonation.objects.filter(date__month=month).aggregate(Sum('amount'))['amount__sum'] or 0
        meal_count = MealDonation.objects.filter(date__month=month).count()
        donation_data.append(donation_sum)
        meal_data.append(meal_count)

    return JsonResponse({
        'labels': labels,
        'donations': donation_data,
        'meals': meal_data,
    })