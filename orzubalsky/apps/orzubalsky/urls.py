from django.conf.urls import patterns, include, url

# orzubalskydotcom application
urlpatterns = patterns('orzubalsky.views',
 
    url(r'page/(?P<url>[0-9A-Za-z]+)$', 'flatpage'),
    url(r'$', 'home', name='home'),
)

