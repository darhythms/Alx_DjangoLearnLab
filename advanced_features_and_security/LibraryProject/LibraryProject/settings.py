AUTH_USER_MODEL = 'bookshelf.CustomUser'

DEBUG = False

SECURE_BROWSER_XSS_FILTER = True  # Enables XSS protection in supported browsers
X_FRAME_OPTIONS = 'DENY'  # Prevents your site from being rendered in a frame
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevents content-type sniffing by browsers

CSRF_COOKIE_SECURE = True  # CSRF cookie only sent over HTTPS
SESSION_COOKIE_SECURE = True  # Session cookie only sent over HTTPS

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

##############

# Redirect all non-HTTPS requests to HTTPS
SECURE_SSL_REDIRECT = True

# Enforce the use of HTTPS by setting the HSTS (HTTP Strict Transport Security) header
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Ensure session cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True

# Prevent the site from being framed and protect against clickjacking
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing a response away from the declared content-type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser's XSS filtering
SECURE_BROWSER_XSS_FILTER = True

# Define the header that Django should look for to determine if the request is over HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

