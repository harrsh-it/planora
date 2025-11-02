from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import EventPlan, ContactMessage

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email


class EventPlanForm(forms.ModelForm):
    class Meta:
        model = EventPlan
        fields = ['party_type', 'services', 'guest_count', 'event_date', 'event_time', 'venue', 'special_requests']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2 border rounded-lg'}),
            'event_time': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full px-4 py-2 border rounded-lg'}),
            'guest_count': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg', 'min': 1}),
            'venue': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg', 'placeholder': 'Enter venue address'}),
            'special_requests': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-lg', 'rows': 4}),
            'party_type': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'services': forms.CheckboxSelectMultiple(),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg', 'placeholder': 'Your email'}),
            'subject': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded-lg', 'rows': 5, 'placeholder': 'Your message'}),
        }
