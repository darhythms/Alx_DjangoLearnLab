AUTH_USER_MODEL = 'bookshelf.CustomUser'

DEBUG = False

SECURE_BROWSER_XSS_FILTER = True  # Enables XSS protection in supported browsers
X_FRAME_OPTIONS = 'DENY'  # Prevents your site from being rendered in a frame
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents content-type sniffing by browsers

CSRF_COOKIE_SECURE = True  # CSRF cookie only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Session cookie only sent over HTTPS

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

