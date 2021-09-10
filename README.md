# dashboard (Django app)
A auth ready dashboard to reuse in projects.

## Installation
Simply copy paste the app or clone whole project. This repo contains fresh copy of Django 3.2.

```
virtualenv venv

# linux/macos
source venv/bin.activate

#windows
venv\Scripts\activate
```
now install requirements
```
pip install -r requirements.txt
```

OR you can manually set it up.
## Install django-allauth
This app requires django-allauth package.
[Get source](https://django-allauth.readthedocs.io/en/latest/installation.html).
```
pip install django-allauth
```
## Install Laravel mix
Get Laravel Mix [here](https://laravel-mix.com/)
```
npm install laravel-mix --save-dev
cd static/resources/
npx mix
```
## Install npm packages
```
npm install
```

## URL settings
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('dashboard.urls')),
    path('admin/', admin.site.urls),
]
```
## Additional Settings
Add these configurations to settings.py
```
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL ="/accounts/login"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

# email verification
ACCOUNT_EMAIL_VERIFICATION="none"

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''


# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

```

