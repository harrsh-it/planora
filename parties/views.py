from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import PartyType, Service, EventPlan, Booking, Testimonial, ContactMessage
from .forms import SignUpForm, EventPlanForm, ContactForm


def home(request):
    """Home page with featured parties"""
    party_types = PartyType.objects.all()[:6]
    testimonials = Testimonial.objects.all()[:3]
    context = {
        'party_types': party_types,
        'testimonials': testimonials,
    }
    return render(request, 'parties/home.html', context)


def services(request):
    """Services and party types listing"""
    party_types = PartyType.objects.all()
    context = {'party_types': party_types}
    return render(request, 'parties/services.html', context)


def party_detail(request, pk):
    """Detailed view of a specific party type"""
    party_type = get_object_or_404(PartyType, pk=pk)
    context = {'party_type': party_type}
    return render(request, 'parties/party_detail.html', context)


def about(request):
    """About page"""
    return render(request, 'parties/about.html')


def contact(request):
    """Contact page with form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! We will contact you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'parties/contact.html', context)


def signup(request):
    """User registration"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('dashboard')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = SignUpForm()
    
    context = {'form': form}
    return render(request, 'parties/signup.html', context)


def login_view(request):
    """User login"""
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
        except:
            messages.error(request, 'An error occurred. Please try again.')
    
    return render(request, 'parties/login.html')


def logout_view(request):
    """User logout"""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    """User dashboard"""
    event_plans = request.user.event_plans.all()
    bookings = request.user.bookings.all()
    total_spent = sum([booking.payment_amount for booking in bookings])
    
    context = {
        'event_plans': event_plans,
        'bookings': bookings,
        'total_spent': total_spent,
    }
    return render(request, 'parties/dashboard.html', context)


@login_required(login_url='login')
def create_event_plan(request):
    """Create new event plan"""
    if request.method == 'POST':
        form = EventPlanForm(request.POST)
        if form.is_valid():
            event_plan = form.save(commit=False)
            event_plan.user = request.user
            event_plan.save()
            form.save_m2m()
            event_plan.calculate_total()
            messages.success(request, 'Event plan created! Proceed to booking.')
            return redirect('booking', pk=event_plan.pk)
    else:
        form = EventPlanForm()
    
    context = {'form': form}
    return render(request, 'parties/create_event_plan.html', context)


@login_required(login_url='login')
def booking(request, pk):
    """Booking confirmation page"""
    event_plan = get_object_or_404(EventPlan, pk=pk, user=request.user)
    
    # Check if booking already exists
    existing_booking = Booking.objects.filter(event_plan=event_plan).first()
    if existing_booking:
        return redirect('booking_details', booking_id=existing_booking.pk)
    
    if request.method == 'POST':
        booking = Booking.objects.create(
            user=request.user,
            event_plan=event_plan,
            payment_amount=event_plan.total_cost,
            advance_payment=event_plan.total_cost * 1,
            status='confirmed'
        )
        messages.success(request, f'Booking confirmed! Your confirmation code is {booking.confirmation_code}')
        return redirect('booking_details', booking_id=booking.pk)
    
    services_total = sum([service.price for service in event_plan.services.all()])
    
    context = {
        'event_plan': event_plan,
        'services_total': services_total,
        'advance_payment': event_plan.total_cost * 2,
    }
    return render(request, 'parties/booking.html', context)


@login_required(login_url='login')
def booking_details(request, booking_id):
    """Booking details and confirmation"""
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    context = {'booking': booking}
    return render(request, 'parties/booking_details.html', context)
