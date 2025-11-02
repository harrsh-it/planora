# PartyHub - Party Planning Website

A comprehensive Django-based party planning and event management platform with beautiful Tailwind CSS styling.

## Features

- **User Authentication**: Sign up, login, and user management
- **Party Packages**: Browse and select from various party types
- **Event Planning**: Customize events with services and special requests
- **Booking System**: Complete booking flow with confirmation codes
- **User Dashboard**: Track events, bookings, and spending
- **Admin Panel**: Manage all content and bookings
- **Testimonials**: Display customer reviews and ratings
- **Contact Form**: Customer inquiry management
- **Responsive Design**: Mobile-friendly interface
- **Beautiful UI**: Vibrant colors with Tailwind CSS

## Installation

### 1. Clone the Repository
\`\`\`bash
git clone <repository-url>
cd party-planning-website
\`\`\`

### 2. Create Virtual Environment
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

### 3. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Database Setup
\`\`\`bash
python manage.py migrate
\`\`\`

### 5. Create Superuser (Admin)
\`\`\`bash
python manage.py createsuperuser
\`\`\`

### 6. Run Development Server
\`\`\`bash
python manage.py runserver
\`\`\`

Visit `http://localhost:8000/` to see the website.

## Admin Panel Setup

1. Go to `http://localhost:8000/admin/`
2. Log in with your superuser credentials
3. Add Party Types, Services, and Testimonials

### Sample Data

**Party Types to Add:**
- Birthday Bash ($150 - 4 hours, up to 30 guests)
- Wedding Reception ($500 - 8 hours, up to 200 guests)
- Corporate Event ($300 - 6 hours, up to 100 guests)
- Kids Party ($100 - 3 hours, up to 20 guests)

**Services to Add:**
- Catering ($50-150)
- DJ & Music ($100-200)
- Decorations ($75-150)
- Photography ($150-300)
- Entertainment ($100-250)

## Project Structure

\`\`\`
party-planning-website/
├── config/              # Django settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── parties/             # Main app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── templates/           # HTML templates
│   ├── base.html
│   └── parties/
├── static/              # CSS, JS, images
└── manage.py
\`\`\`

## Key Models

- **PartyType**: Different party packages
- **Service**: Additional services available
- **EventPlan**: User's planned event
- **Booking**: Confirmed event booking
- **Testimonial**: Customer reviews
- **ContactMessage**: Contact form submissions

## Authentication

- Email-based login (users register with email)
- Session-based authentication
- Protected dashboard and booking pages
- Automatic redirect for authenticated users

## Database

- SQLite (development)
- Can be upgraded to PostgreSQL for production

## Styling

- Tailwind CSS v3
- Vibrant color palette (Pink, Purple, Cyan, Gold)
- Responsive mobile-first design
- Custom animations and transitions

## Deployment

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use PostgreSQL instead of SQLite
4. Set up proper SECRET_KEY
5. Configure static files collection
6. Use Gunicorn or similar WSGI server

\`\`\`bash
python manage.py collectstatic
\`\`\`

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please contact us at info@partyhub.com

---

**Made with ❤️ for event planning excellence**
