from django.views.generic import TemplateView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class HomeView(TemplateView):
    template_name = 'home.html'


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter