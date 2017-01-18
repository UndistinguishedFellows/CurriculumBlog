from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /blog/5/
    url(r'^blog/(?P<post_id>[0-9]+)/$', views.post, name='post'),
    #url(r'^blog/', views.blog, name='blog'),
    url(r'^about', views.about, name='about'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)