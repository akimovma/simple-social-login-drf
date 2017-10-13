from django.conf.urls import url

from .views import HomeView, GoogleLogin

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login')
]
