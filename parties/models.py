from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class PartyType(models.Model):
    """Different types of parties available"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='party_types/')
    duration_hours = models.IntegerField(default=4)
    max_guests = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Service(models.Model):
    """Additional services for parties"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    icon = models.CharField(max_length=50, default='star')
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    
    def __str__(self):
        return self.name


class EventPlan(models.Model):
    """User's planned event"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_plans')
    party_type = models.ForeignKey(PartyType, on_delete=models.SET_NULL, null=True)
    services = models.ManyToManyField(Service, blank=True)
    guest_count = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])
    event_date = models.DateField()
    event_time = models.TimeField()
    venue = models.CharField(max_length=255)
    special_requests = models.TextField(blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.party_type} - {self.user.username}"

    def calculate_total(self):
        total = self.party_type.base_price if self.party_type else 0
        total += sum([service.price for service in self.services.all()])
        self.total_cost = total
        self.save()
        return total


class Booking(models.Model):
    """Event booking and payment"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    event_plan = models.OneToOneField(EventPlan, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)
    booking_date = models.DateTimeField(auto_now_add=True)
    confirmation_code = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ['-booking_date']

    def __str__(self):
        return f"Booking #{self.confirmation_code}"

    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            import uuid
            self.confirmation_code = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)


class Testimonial(models.Model):
    """Customer testimonials"""
    name = models.CharField(max_length=100)
    party_type = models.ForeignKey(PartyType, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating}★"


class ContactMessage(models.Model):
    """Contact form messages"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
