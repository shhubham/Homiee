from django.conf.urls import url,include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from list import views as list_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$',views.about),
    url(r'^$',list_views.about1,name="home"),
    url(r'^list/',include('list.urls')),
    url(r'^accounts/',include('accounts.urls')),


]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
