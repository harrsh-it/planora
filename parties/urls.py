from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('party/<int:pk>/', views.party_detail, name='party_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('event-plan/create/', views.create_event_plan, name='create_event_plan'),
    path('booking/<int:pk>/', views.booking, name='booking'),
    path('booking-details/<int:booking_id>/', views.booking_details, name='booking_details'),
]
