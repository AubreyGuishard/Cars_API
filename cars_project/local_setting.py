# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jg90fvt$8iczoo+b#m==lx9eng_1d8@*ai_#br5=0ak0tscji9'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': "localhost",
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
