from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /blog/5/
    url(r'^blog', views.post_page, name='post_page'),
    url(r'^author', views.author, name='author'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)