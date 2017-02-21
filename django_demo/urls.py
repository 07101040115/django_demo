from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^polls_generic/', include('polls_generic.urls', namespace='polls_generic')),
    url(r'^admin/', include(admin.site.urls)),
  
]
