from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView 

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url('accounts/register/', views.registration, name='register'),
    url('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)