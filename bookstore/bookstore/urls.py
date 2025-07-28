from django.contrib import admin
from django.urls import path
from store import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('test/', views.test_view, name='test'),
    path('', views.test_view, name='home'), 
    path('logout/', views.logout_view, name='logout'),
    path('test/cart.html', views.cart, name='cart'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
