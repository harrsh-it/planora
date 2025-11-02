from django.contrib import admin
from .models import PartyType, Service, EventPlan, Booking, Testimonial, ContactMessage


@admin.register(PartyType)
class PartyTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_price', 'max_guests', 'duration_hours']
    search_fields = ['name', 'description']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']


@admin.register(EventPlan)
class EventPlanAdmin(admin.ModelAdmin):
    list_display = ['user', 'party_type', 'event_date', 'guest_count', 'total_cost']
    list_filter = ['event_date', 'party_type']
    search_fields = ['user__username', 'venue']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['confirmation_code', 'user', 'status', 'payment_amount', 'booking_date']
    list_filter = ['status', 'booking_date']
    search_fields = ['confirmation_code', 'user__username']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'party_type', 'rating']
    list_filter = ['rating', 'created_at']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'subject']
