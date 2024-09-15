# advanced_api_project/settings.py

INSTALLED_APPS = [
    # Other Django apps
    'rest_framework',
    'api',  # Register your new app
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
