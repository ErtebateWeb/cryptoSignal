from django.contrib import admin
from django.urls import path,include
from .views import home_page, about_page, contact_page, login_page, register_page

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about-us', about_page),
    path('contact-us', contact_page),
    path('login', login_page),
    path('register', register_page),
    path('cryptosignal/',include("cryptosignal.urls"))

]


if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)