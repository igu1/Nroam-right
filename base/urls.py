from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('packages/', views.packages, name='packages'),
    path('packages/<int:id>/detail', views.detail_package, name='detail-package'),
    path('service/', views.service, name='service'),
    path('signin/', views.signin, name='signin'),
    path('registration/', views.registration, name='registration'),
    path('agencies/<int:id>/', views.agencies, name='agencies'),
    path('logout', LogoutView.as_view(), name='logout')

]
