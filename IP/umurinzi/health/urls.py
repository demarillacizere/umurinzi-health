from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView 

urlpatterns = [
    url('^$',views.index,name='index'),
    url('accounts/register/', views.registration, name='register'),
    url('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url('^search/', views.search_results, name='search_results'),
    url('drug/(\d+)',views.get_details,name='get_details'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)