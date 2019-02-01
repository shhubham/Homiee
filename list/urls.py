from django.conf.urls import url
from .import views

app_name='list'

urlpatterns = [
    url(r'^about/$',views.about1,name="about"),
    url(r'create/$',views.article_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$',views.details,name="data"),
    #url(r'^$',views.homepage, name="test"),
]
