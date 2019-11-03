from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from smithsonian.api.views.users import FacebookLogin, GoogleLogin

admin.site.site_header = 'Smithsonian'

urlpatterns = [

    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    path('auth/', include('allauth.urls')),

    # LOGIN
    path('rest-auth/', include('rest_auth.urls')),
    # REGISTER
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # LOGIN / REGISTER with Facebook / Google
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),

    # Sightings, UserData urls
    path('api/', include('smithsonian.api.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
