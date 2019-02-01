from django.conf.urls import url
from .import views

app_name='accounts'

urlpatterns=[
    url(r'^signup/',views.signup_view, name="signup"),
    url(r'^log/$',views.log_view, name="log"),
    url(r'^logout/$',views.logout_view, name="logout"),

    #url(r'^login/',views.login_view, name="login")

]
