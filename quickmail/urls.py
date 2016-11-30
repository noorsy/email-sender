from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import auth
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^$', 'emailing.views.index'),
    url(r'^oauth2callback', 'emailing.views.auth_return'),
    url('^accounts/login/$', 'auth.login', {'template_name': 'plus/login.html'}),

    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'quickmail.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^upload/$', 'people.views.upload_file', name='upload'),
    url(r'^complete/$', 'people.views.complete_upload', name='complete'),


]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)